# TCP 3-Way Handshake Explained

The Transmission Control Protocol (TCP) is one of the most widely used protocols for communication in networks. A key feature of TCP is the **3-way handshake** that ensures reliable communication between two devices before data is transmitted.

## What is the 3-Way Handshake?

The 3-Way Handshake is a process used by TCP to establish a connection between a client and a server. It involves three steps:

1. **SYN (Synchronize)**
   - The client sends a SYN packet to the server to initiate a connection.
   
2. **SYN-ACK (Synchronize-Acknowledgment)**
   - The server responds with a SYN-ACK packet to acknowledge the client's request.
   
3. **ACK (Acknowledgment)**
   - The client responds with an ACK packet to confirm that the connection has been established.

### Why is the 3-Way Handshake Important?

The handshake ensures that both the client and server are ready for communication. It also allows each side to synchronize their sequence numbers, which helps in tracking the data during transmission.

## Visual Representation

The following diagram illustrates the sequence of events during a TCP 3-Way Handshake:


