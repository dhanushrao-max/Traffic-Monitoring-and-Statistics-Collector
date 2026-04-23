import matplotlib.pyplot as plt
import csv

time_vals = []
packets = []
bytes_ = []

with open("traffic_stats.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header

    for row in reader:
        time_vals.append(float(row[0]))
        packets.append(int(row[1]))
        bytes_.append(int(row[2]))

plt.plot(time_vals, packets, label="Packets")
plt.plot(time_vals, bytes_, label="Bytes")

plt.xlabel("Time")
plt.ylabel("Count")
plt.title("Traffic Monitoring")
plt.legend()

plt.show()