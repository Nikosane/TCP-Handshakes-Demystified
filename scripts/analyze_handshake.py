from scapy.all import rdpcap

# Read the pcap file
packets = rdpcap("captures/tcp_handshake.pcap")

# Extract handshake packets
for packet in packets:
    if packet.haslayer("TCP"):
        tcp = packet["TCP"]
        print(f"Packet: {packet.summary()}, Seq: {tcp.seq}, Ack: {tcp.ack}, Flags: {tcp.flags}")
