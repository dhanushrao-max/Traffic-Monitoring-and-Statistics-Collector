from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer
import time
import csv
import os

log = core.getLogger()

mac_to_port = {}

# Create CSV file if not exists
if not os.path.exists("traffic_stats.csv"):
    with open("traffic_stats.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "Packets", "Bytes"])

# Switch connection event
def _handle_ConnectionUp(event):
    log.info("Switch connected: %s", event.connection)

# Packet handling (forwarding + firewall + flow rules)
def _handle_PacketIn(event):
    packet = event.parsed
    if not packet:
        return

    dpid = event.connection.dpid

    if dpid not in mac_to_port:
        mac_to_port[dpid] = {}

    # Learn MAC
    mac_to_port[dpid][packet.src] = event.port

    # 🔥 FIREWALL: block h1 → h2
    if packet.src.toStr() == "00:00:00:00:00:01" and packet.dst.toStr() == "00:00:00:00:00:02":
        print("BLOCKED: h1 → h2")
        return

    # Decide output port
    if packet.dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][packet.dst]
    else:
        out_port = of.OFPP_FLOOD

    # Install flow rule (enables counters)
    flow_mod = of.ofp_flow_mod()
    flow_mod.match = of.ofp_match.from_packet(packet, event.port)
    flow_mod.actions.append(of.ofp_action_output(port=out_port))
    event.connection.send(flow_mod)

    # Send packet immediately
    packet_out = of.ofp_packet_out()
    packet_out.data = event.ofp
    packet_out.actions.append(of.ofp_action_output(port=out_port))
    packet_out.in_port = event.port
    event.connection.send(packet_out)

# Handle flow statistics
def _handle_FlowStatsReceived(event):
    for stat in event.stats:
        packets = stat.packet_count
        bytes_ = stat.byte_count

        print("Packets:", packets, "Bytes:", bytes_)

        # Save to CSV
        with open("traffic_stats.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([time.time(), packets, bytes_])

# Request stats periodically
def request_stats():
    for connection in core.openflow._connections.values():
        connection.send(of.ofp_stats_request(
            body=of.ofp_flow_stats_request()))

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    core.openflow.addListenerByName("FlowStatsReceived", _handle_FlowStatsReceived)

    Timer(5, request_stats, recurring=True)