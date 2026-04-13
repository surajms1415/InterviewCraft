import json

cs_topics_path = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\data\cs_topics.json'

with open(cs_topics_path, 'r', encoding='utf-8') as f:
    topics_data = json.load(f)

# Deep dive into CN theory
cn_topics = {
    "title": "Computer Networks (CN)",
    "description": "Comprehensive, highly detailed networking principles covering protocol stacks, transmission mechanics, and critical handshakes.",
    "categories": [
        {
            "name": "1. OSI Model - Lower Layers (Hardware/Network)",
            "topics": [
                {"name": "Layer 1: Physical Layer", "explanation": "Converts logical bits into a physical signal (electrical, optical, radio). Responsible for topology (Star, Mesh, Bus), transmission mode (Simplex, Half-Duplex, Full-Duplex), and bit synchronization. Devices: Hubs, Repeaters, Cables."},
                {"name": "Layer 2: Data Link Layer (DLL)", "explanation": "Ensures node-to-node data transfer. Data is packaged into 'Frames'. \nKey Functions:\n• Framing & MAC Addressing (Physical 48-bit address).\n• Error Control: Adds CRC or Checksum to detect damaged frames.\n• Flow Control: Stop & Wait, Sliding Window protocols.\nDevices: Switches, Bridges."},
                {"name": "Layer 3: Network Layer", "explanation": "Handles host-to-host delivery across multiple networks. Data is packaged into 'Packets'.\nKey Functions:\n• Logical Addressing: Assigns IP addresses (IPv4 / IPv6).\n• Routing: Uses algorithms (Distance Vector, Link State) to find the shortest path.\nProtocols: IP, ICMP, ARP. Devices: Routers."}
            ]
        },
        {
            "name": "2. OSI Model - Upper Layers (Host/Software)",
            "topics": [
                {"name": "Layer 4: Transport Layer", "explanation": "Process-to-process delivery. Data is packaged into 'Segments'.\nKey Functions:\n• Segmentation and Reassembly.\n• Connection Control: TCP (reliable) vs UDP (unreliable fast).\n• Port Addressing: Identifies which application (e.g., Port 80 for HTTP) receives the data."},
                {"name": "Layer 5: Session Layer", "explanation": "Establishes, maintains, and terminates connections (sessions) between local and remote applications. Uses checkpoints to resume failed data transfers. Example: Authentication and authorization."},
                {"name": "Layer 6: Presentation Layer", "explanation": "The 'Translator' for the network. Prepares data for the Application Layer.\nKey Functions:\n• Translation: ASCII to EBCDIC.\n• Encryption: SSL/TLS secures the data.\n• Compression: Reduces data size."},
                {"name": "Layer 7: Application Layer", "explanation": "Directly interacts with the user. Provides network services to applications.\nProtocols: HTTP (Web), FTP (File Transfer), SMTP (Email), DNS (Domain lookup)."}
            ]
        },
        {
            "name": "3. TCP/IP Model & The 3-Way Handshake",
            "topics": [
                {"name": "TCP/IP vs OSI", "explanation": "The practical 4-layer model used in the modern Internet.\n• Application Layer (Combines OSI L5, L6, L7)\n• Transport Layer (OSI L4)\n• Internet Layer (OSI L3)\n• Network Access Layer (Combines OSI L1, L2)."},
                {"name": "TCP 3-Way Handshake (Connection Setup)", "explanation": "Process to establish a reliable TCP connection before sending data.\n1) SYN: Client sends SYN (Synchronize) packet to Server.\n2) SYN-ACK: Server receives SYN, allocates buffers, sends back SYN-ACK.\n3) ACK: Client receives SYN-ACK, replies with ACK (Acknowledge). Connection is now ESTABLISHED."},
                {"name": "TCP Connection Termination (4-Way Handshake)", "explanation": "1) FIN: Client says 'I am done sending'.\n2) ACK: Server acknowledges.\n3) FIN: Server says 'I am also done'.\n4) ACK: Client acknowledges. Connection CLOSED."},
                {"name": "TCP vs UDP", "explanation": "TCP (Transmission Control Protocol): Connection-oriented, guarantees delivery, strict ordering, performs error checking & flow control (Sliding Window). Slow.\nUDP (User Datagram Protocol): Connectionless, fire-and-forget, no guarantees, fast. Used for VoIP, streaming, gaming."}
            ]
        },
        {
            "name": "4. IP Addressing & Subnetting Basics",
            "topics": [
                {"name": "IPv4 Classes", "explanation": "32-bit logical address. \n• Class A: 1.0.0.0 to 126.x.x.x (Huge networks)\n• Class B: 128.0.0.0 to 191.255.x.x (Medium)\n• Class C: 192.0.0.0 to 223.255.255.x (Small, Max 254 hosts)\n• Private IP Ranges: 10.x.x.x (A), 172.16.x.x (B), 192.168.x.x (C)."},
                {"name": "MAC Address vs IP Address", "explanation": "MAC (Media Access Control) is a 48-bit physical address permanently burned into the NIC. IP Address is a 32-bit logical address assigned by the network dynamically."}
            ]
        },
        {
            "name": "5. Core Network Protocols",
            "topics": [
                {"name": "DNS (Domain Name System)", "explanation": "The 'Phonebook' of the internet. Translates human-readable domain names (www.google.com) into machine IP addresses (142.250.190.46). Uses UDP Port 53."},
                {"name": "DHCP (Dynamic Host Configuration)", "explanation": "Automatically assigns IP addresses to devices. Uses DORA process: Discover (Client), Offer (Server), Request (Client), Acknowledge (Server)."},
                {"name": "ARP & ICMP", "explanation": "ARP (Address Resolution Protocol): Finds the MAC Address associated with a known IP Address locally. \nICMP (Internet Control Message Protocol): Used for diagnostics and error reporting. e.g., 'Ping' uses ICMP Echo Request/Reply."}
            ]
        }
    ]
}

topics_data['cn'] = cn_topics

with open(cs_topics_path, 'w', encoding='utf-8') as f:
    json.dump(topics_data, f, indent=4)

print("Updated CN granular details!")
