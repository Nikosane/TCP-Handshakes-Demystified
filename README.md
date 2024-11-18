# TCP-Handshakes-Demystified

# Exploring the TCP 3-Way Handshake

This repository provides a detailed exploration of the **TCP 3-way handshake**, a critical process in establishing reliable communication over the Internet. The project includes real-world packet captures, detailed protocol analysis, and Python scripts for simulation and analysis.

## What is the TCP 3-Way Handshake?

The TCP 3-way handshake is a sequence of packets exchanged between a client and server to establish a reliable connection. It involves three steps:
1. **SYN**: The client sends a synchronization packet to start the connection.
2. **SYN+ACK**: The server acknowledges the client's request and sends its own synchronization request.
3. **ACK**: The client acknowledges the server's response, completing the handshake.

---

## Features

- Detailed explanation of the TCP handshake process.
- Real-world `.pcap` file demonstrating the handshake.
- Python scripts for:
  - Simulating the handshake using Scapy.
  - Analyzing existing packet captures programmatically.

---

## Repository Contents

- **captures/**: Packet captures of TCP handshakes.
- **scripts/**: Python scripts for handshake simulation and analysis.
- **docs/**: Detailed explanations and examples of the handshake process.

---

## Getting Started

### Requirements
- Wireshark or Tshark
- Python 3.x
- [Scapy library](https://scapy.net/)

### Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Exploring-TCP-3-Way-Handshake.git
   cd Exploring-TCP-3-Way-Handshake

2. Open the .pcap file in Wireshark:
```
wireshark captures/tcp_handshake.pcap
```
Run the Python scripts:
  -  Simulate the handshake:
     ```
     python scripts/simulate_handshake.py
     ```
  -  Analyze a .pcap file:
     ```
     python scripts/analyze_handshake.py
     ```

---

## Example Outputs

Packet breakdown of a handshake:
```
Packet 1: SYN (Seq: 0)
Packet 2: SYN+ACK (Seq: 0, Ack: 1)
Packet 3: ACK (Seq: 1, Ack: 1)
```
Round-trip time (RTT) calculation from a capture:
```
RTT: 0.124 ms
```
