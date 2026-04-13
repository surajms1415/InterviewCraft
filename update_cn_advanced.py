import json

filepath = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\data\cs_topics.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find cn and add these to categories
cn_categories = data['cn']['categories']

advanced_tcp_handshake = {
    "name": "6. TCP 3-Way Handshake (Deep Dive)",
    "topics": [
        {"name": "What & Why?", "explanation": "Before sending data, TCP must ensure both client and server are ready, sync sequence numbers, and establish reliability. Without it: data may be lost, duplicate packets confuse the system."},
        {"name": "Step 1: Client -> SYN", "explanation": "Client sends SYN=1, seq=x (random number, e.g. 100). Meaning: 'I want to start communication, my starting sequence is 100'. Random seq prevents old packet confusion."},
        {"name": "Step 2: Server -> SYN + ACK", "explanation": "Server replies SYN=1, ACK=1, seq=y (e.g. 300), ack=x+1 (101). Meaning: 'Received your request (ack 101), ready. My sequence is 300'. Acknowledges client and starts its own connection."},
        {"name": "Step 3: Client -> ACK", "explanation": "Client sends ACK=1, seq=101, ack=y+1 (301). Meaning: 'Received your response, connection established'. Data transfer begins."},
        {"name": "Interview Q: SYN Flood Attack", "explanation": "Attacker sends many SYN requests but never completes handshake. Server resources get exhausted waiting for the final ACKs."}
    ]
}

network_flows = {
    "name": "7. Advanced Network Mechanics & Flows",
    "topics": [
        {"name": "TCP vs UDP (Analogy)", "explanation": "TCP (Reliable): Like sending an important document via courier. Connection established, sent in order, ack sent, lost data is resent. No data loss.\nUDP (Unreliable): Like shouting in a crowd. No confirmation, no guarantee, fast. Used for Video streaming / Gaming."},
        {"name": "What happens when you type google.com?", "explanation": "1. DNS Resolution: Checks cache -> local DNS -> root -> TLD -> authoritative server. Returns IP.\n2. TCP Connection: 3-way handshake established.\n3. HTTP Request: Browser sends GET / HTTP/1.1.\n4. Server Response: Sends HTML/CSS/JS.\n5. Browser Rendering: Parses code and shows webpage."},
        {"name": "ARP & Routing Logic", "explanation": "ARP: 'Who has this IP? I have -> here is my MAC'. Needed to send data strictly in a local network.\nRouting: Data doesn't go direct. Laptop -> Router -> ISP -> Internet -> Server. Routers check IPs and forward like Google Maps."},
        {"name": "Flow vs Congestion Control", "explanation": "Flow Control: Sender is fast, receiver is slow. Solution: Control sending rate (Sliding Window).\nCongestion Control: Too much traffic in the network itself. Solution: TCP reduces speed, gradually increases (Like traffic signals)."},
        {"name": "HTTP vs HTTPS & Sockets", "explanation": "HTTP is plaintext (hackable). HTTPS is secure/encrypted via SSL/TLS.\nSocket Programming: Endpoint communication. Server creates socket & listens. Client connects. Data exchanged (Used in Chat apps)."}
    ]
}

cn_categories.append(advanced_tcp_handshake)
cn_categories.append(network_flows)

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
print("Updated CN advanced topics")
