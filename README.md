# Traffic-Monitoring-and-Statistics-Collector-using-Software-Defined-Networking-SDN-
# 🚦 Traffic Monitoring and Statistics Collector using SDN

## 📌 Project Overview

This project implements a Software Defined Networking (SDN) based traffic monitoring system using a centralized controller. The system is built using Mininet for network simulation and POX controller for managing network behavior.

The controller dynamically installs flow rules, enforces firewall policies, and periodically collects traffic statistics such as packet count and byte count. The collected data is stored in a CSV file and visualized using graphs.

---

## 🎯 Objectives

- Implement SDN architecture using Mininet and POX
- Design flow-based forwarding using OpenFlow
- Monitor traffic statistics (packet_count, byte_count)
- Apply firewall rules
- Generate CSV reports
- Visualize traffic using graphs

---

## 🧠 Key Concepts

- Software Defined Networking (SDN)
- OpenFlow Protocol
- Match-Action Flow Tables
- Centralized Network Control
- Flow Statistics Monitoring

---

## 🏗️ System Architecture

```
Hosts → Switch (OpenFlow) → Controller (POX) → CSV + Graph
```

📸 **Architecture Diagram:**  
<br>
<img width="1536" height="1024" alt="ChatGPT Image Apr 23, 2026, 10_53_34 PM" src="https://github.com/user-attachments/assets/c2561626-4e94-4a97-8d61-7ba6f7c609de" />

<br>
---

## ⚙️ Technologies Used

- Python  
- POX Controller  
- Mininet  
- OpenFlow Protocol  
- Matplotlib  

---

## 🚀 How It Works

1. Network is created using Mininet  
2. Switch connects to POX controller  
3. Unknown packets trigger PacketIn events  
4. Controller installs flow rules (FlowMod)  
5. Switch forwards packets using installed rules  
6. Flow entries maintain counters:
   - Packet Count  
   - Byte Count  
7. Controller periodically requests statistics  
8. Data is:
   - Printed in terminal  
   - Stored in CSV file  
9. Graph is generated from CSV data  

---

## 🔥 Features

- Dynamic flow rule installation  
- MAC learning-based forwarding  
- Firewall (blocking specific traffic)  
- Periodic traffic monitoring  
- CSV logging of statistics  
- Graph visualization  

---

## 🛡️ Firewall Implementation

The controller blocks traffic from **h1 → h2**

---

## 📂 Project Structure

```
.
├── traffic_monitor.py
├── plot_graph.py
├── traffic_stats.csv
├── README.md
└── Report
```

---

## ▶️ How to Run

### 1. Start Controller
```
cd ~/pox
./pox.py log.level --DEBUG openflow.of_01 traffic_monitor
```

### 2. Start Mininet (new terminal)
```
sudo mn --controller=remote,ip=127.0.0.1,port=6633 --switch ovs,protocols=OpenFlow10
```

### 3. Generate Traffic
```
pingall
```
or
```
h1 ping -c 10 h2
```

---

## 📊 Output

### 🔹 Terminal Output  
<br>
<img width="1733" height="937" alt="Screenshot 2026-04-23 230649" src="https://github.com/user-attachments/assets/43937b12-497d-4a71-a9d2-9ad2e7c516d3" />
<br>
POX controller displaying real-time traffic statistics including packet count and byte count collected from OpenFlow switches.
<br>

<img width="1320" height="702" alt="Screenshot 2026-04-23 230718" src="https://github.com/user-attachments/assets/1b38fced-ae51-489a-ab3b-6d5da9479b0d" />
<br>
Mininet simulation showing successful network creation and connectivity test using pingall with 0% packet loss.
<br>

### 🔹 CSV File  
<br>
<img width="1853" height="974" alt="Screenshot 2026-04-23 231136" src="https://github.com/user-attachments/assets/e6cd2f16-b853-4b9f-8528-dfde91e0abfc" />
<br>
Graphical representation of network traffic showing variation of packet count and byte count over time.
<br>

### 🔹 Graph Output
<br>
<img width="645" height="551" alt="Screenshot 2026-04-23 231050" src="https://github.com/user-attachments/assets/82cedbbb-7819-46de-860e-21085f0b3101" />
<br>
CSV file storing time-based traffic statistics including packet count and byte count collected by the controller.
<br>
---

## 📈 Sample CSV Format

```
Time,Packets,Bytes
1712345678,10,840
1712345683,20,1680
```

---

## 📊 Graph Explanation

- X-axis → Time  
- Y-axis → Traffic  
- Lines represent:
  - Packet count  
  - Byte count  

---

## ✅ Results

- Controller-switch communication established  
- Flow rules installed dynamically  
- Traffic statistics collected successfully  
- Firewall rule applied correctly  
- Data stored and visualized  

---

## ⚠️ Limitations

- Works only in simulated environment  
- Basic firewall implementation  
- No graphical dashboard  

---

## 🚀 Future Enhancements

- Web-based dashboard  
- Advanced traffic analysis  
- Multi-switch topology  
- Real-time alerts  

---

## 📚 References

- https://mininet.org/  
- https://github.com/noxrepo/pox  
- https://opennetworking.org/  

---

## 👨‍💻 Author

- Name: Dhanush Rao
- Course: Computer Networks  

---

## ⭐ Final Note

This project demonstrates centralized control, real-time traffic monitoring, and flexible network management using SDN.
