# TCP 3-Way Handshake Examples

This document provides examples of how the TCP 3-Way Handshake can be observed and analyzed in network traffic.


## Example 1: Simple 3-Way Handshake Capture

In the following capture, we see the typical three steps of the handshake:

1. **SYN packet**: The client sends a SYN packet to the server, requesting a connection.
2. **SYN-ACK packet**: The server responds with a SYN-ACK packet, acknowledging the request.
3. **ACK packet**: The client confirms the connection with an ACK packet.
