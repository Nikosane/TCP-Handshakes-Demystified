from scapy.all import *

# Define source and destination
src_ip = "192.168.1.100"
dst_ip = "192.168.0.109"
dst_port = 80

# SYN
syn = IP(src=src_ip, dst=dst_ip) / TCP(sport=RandShort(), dport=dst_port, flags="S")
syn_ack = sr1(syn)

# SYN+ACK
ack = IP(src=src_ip, dst=dst_ip) / TCP(sport=syn_ack[TCP].sport, dport=dst_port, flags="A", seq=syn_ack.ack, ack=syn_ack.seq + 1)
send(ack)

print("TCP 3-Way Handshake simulated successfully!")