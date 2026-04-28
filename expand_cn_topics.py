import json

file_path = "frontend-app/src/data/cs_notes.json"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # We will completely overwrite the 'cn' topics to match the detailed multi-card request
    data["cn"]["topics"] = [
        {
            "id": "osi-model",
            "title": "OSI Model",
            "description": "Open Systems Interconnection - 7 Layer Model",
            "cards": [
                {
                    "type": "text",
                    "heading": "Application Layer (Layer 7)",
                    "content": "The Application Layer is the topmost layer and closest to the end user. It provides network services directly to applications.\n\n• **Data Unit:** Data\n• **Protocols:** HTTP, HTTPS, FTP, SMTP, DNS, DHCP, Telnet, SSH\n• **Devices:** Gateways, Firewalls\n\n**Key Functions:**\n- Network Virtual Terminal\n- File Transfer, Access, and Management (FTAM)\n- Mail Services\n- Directory Services\n\n**Example:** When you open a web browser and visit a website, you're using HTTP/HTTPS protocols."
                },
                {
                    "type": "text",
                    "heading": "Presentation Layer (Layer 6)",
                    "content": "The Presentation Layer acts as a translator between the network and application. It handles data formatting, encryption, and compression.\n\n• **Data Unit:** Data\n• **Protocols:** SSL/TLS, JPEG, MPEG, GIF, ASCII, EBCDIC\n• **Devices:** Gateway\n\n**Key Functions:**\n- Translation: Converting data formats (ASCII ↔ EBCDIC)\n- Encryption/Decryption: SSL/TLS encryption\n- Compression: Reducing data size for transmission\n\n**Example:** When you see the lock icon in your browser, SSL/TLS at the Presentation Layer is encrypting your data."
                },
                {
                    "type": "text",
                    "heading": "Session Layer (Layer 5)",
                    "content": "The Session Layer establishes, manages, and terminates sessions between applications. It acts like a dialog controller.\n\n• **Data Unit:** Data\n• **Protocols:** NetBIOS, PPTP, RPC, SQL, NFS\n• **Devices:** Gateway\n\n**Key Functions:**\n- Session Establishment, Maintenance, and Termination\n- Synchronization: Using checkpoints\n- Dialog Control: Half-duplex or Full-duplex\n\n**Session Modes:**\n- Simplex: One-way communication\n- Half-Duplex: Two-way, one at a time\n- Full-Duplex: Two-way simultaneous"
                },
                {
                    "type": "text",
                    "heading": "Transport Layer (Layer 4)",
                    "content": "The Transport Layer provides end-to-end communication between processes. It's responsible for reliable data transfer.\n\n• **Data Unit:** Segment (TCP) / Datagram (UDP)\n• **Protocols:** TCP, UDP, SCTP, DCCP\n• **Devices:** Gateway, Firewall\n\n**Key Functions:**\n- Segmentation and Reassembly\n- Connection Control (TCP) or Connectionless (UDP)\n- Flow Control & Error Control\n- Port Addressing\n\n**Port Numbers:** HTTP: 80, HTTPS: 443, FTP: 21, SSH: 22, SMTP: 25, DNS: 53"
                },
                {
                    "type": "text",
                    "heading": "Network Layer (Layer 3)",
                    "content": "The Network Layer handles logical addressing and routing. It determines the best path for data to travel across networks.\n\n• **Data Unit:** Packet\n• **Protocols:** IP, ICMP, IGMP, IPsec, ARP, RARP\n• **Devices:** Router, Layer 3 Switch\n\n**Key Functions:**\n- Logical Addressing (IP Addresses)\n- Routing: Finding optimal path (RIP, OSPF, BGP)\n- Packet Forwarding\n- Fragmentation and Reassembly"
                },
                {
                    "type": "text",
                    "heading": "Data Link Layer (Layer 2)",
                    "content": "The Data Link Layer provides node-to-node data transfer and handles physical addressing (MAC addresses).\n\n• **Data Unit:** Frame\n• **Protocols:** Ethernet, PPP, HDLC, Frame Relay, ATM\n• **Devices:** Switch, Bridge, NIC\n\n**Key Functions:**\n- Framing: Encapsulating packets into frames\n- Physical Addressing: MAC addresses (48-bit)\n- Error Detection: CRC (Cyclic Redundancy Check)\n- Access Control: CSMA/CD, CSMA/CA"
                },
                {
                    "type": "text",
                    "heading": "Physical Layer (Layer 1)",
                    "content": "The Physical Layer is the lowest layer, dealing with actual physical transmission of raw bits over a medium.\n\n• **Data Unit:** Bits\n• **Protocols:** Ethernet Physical, USB, Bluetooth, RS-232\n• **Devices:** Hub, Repeater, Cables\n\n**Key Functions:**\n- Bit Synchronization: Clock synchronization\n- Bit Rate Control: Transmission speed\n- Physical Topologies: Star, Bus, Ring, Mesh\n- Transmission Modes: Simplex, Half-duplex, Full-duplex"
                }
            ]
        },
        {
            "id": "tcp-3-way-handshake",
            "title": "TCP 3-Way Handshake",
            "description": "The process used in a TCP/IP network to establish a reliable connection.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Introduction",
                    "content": "The TCP 3-Way Handshake is the process used in a TCP/IP network to establish a connection between a client and a server. It is a multi-step process that requires both the client and server to exchange synchronization and acknowledgment packets before real data transmission begins.\n\nThink of it as a formal introduction: **'I want to talk'** → **'I heard you, I'm ready too'** → **'Great, let's start.'**"
                },
                {
                    "type": "text",
                    "heading": "The Objective of the Handshake",
                    "content": "Before sending data, the two machines must agree on:\n\n• **Initial Sequence Numbers (ISN):** To keep data packets in the correct order.\n• **Window Size:** To manage flow control (how much data can be sent before an acknowledgment is needed).\n• **Connection State:** Ensuring both sides are ready and willing to communicate."
                },
                {
                    "type": "text",
                    "heading": "Step 1: SYN (Synchronize)",
                    "content": "The client (the initiator) wants to establish a connection with the server. It sends a segment with the SYN flag set.\n\n• **Action:** The client picks a random Initial Sequence Number (ISN), let's call it X.\n• **Packet Details:** The packet contains `SYN=1`, `ACK=0`, and `Sequence Number = X`.\n• **State:** The client enters the `SYN-SENT` state. The server receives this and knows a client wants to start a connection."
                },
                {
                    "type": "text",
                    "heading": "Step 2: SYN-ACK (Synchronize-Acknowledgment)",
                    "content": "The server receives the client’s request. If its port is open and it has resources, it agrees to the connection by sending a SYN-ACK message.\n\n• **Acknowledgment (ACK):** The server acknowledges the client's sequence number by sending back `Acknowledgment Number = X + 1`. This tells the client, *'I received X, and I’m expecting X+1 next.'*\n• **Synchronization (SYN):** The server picks its own random Initial Sequence Number, let's call it Y.\n• **Packet Details:** `SYN=1`, `ACK=1`, `Sequence Number = Y`, and `Ack Number = X + 1`.\n• **State:** The server enters the `SYN-RECEIVED` state."
                },
                {
                    "type": "text",
                    "heading": "Step 3: ACK (Acknowledgment)",
                    "content": "The client receives the server’s SYN-ACK. Now the client must confirm that it received the server’s sequence number.\n\n• **Action:** The client responds with an ACK packet. It increments the server's sequence number Y to Y+1.\n• **Packet Details:** `SYN=0`, `ACK=1`, `Sequence Number = X + 1`, and `Acknowledgment Number = Y + 1`.\n• **State:** The client enters the `ESTABLISHED` state. Once the server receives it, it also enters the `ESTABLISHED` state."
                },
                {
                    "type": "table",
                    "heading": "Summary Table for Placements",
                    "content": "",
                    "headers": ["Step", "Initiator", "Flags", "Seq No", "Ack No", "Description"],
                    "rows": [
                        ["1. SYN", "Client", "SYN=1", "X", "—", "Hey, can we connect? Here is my starting number X."],
                        ["2. SYN-ACK", "Server", "SYN=1, ACK=1", "Y", "X+1", "I hear you (X+1). I'm ready too, here is my number Y."],
                        ["3. ACK", "Client", "ACK=1", "X+1", "Y+1", "Got it (Y+1). We are connected!"]
                    ]
                },
                {
                    "type": "faq",
                    "heading": "Critical Interview Questions",
                    "questions": [
                        {
                            "q": "Why is it a '3-way' handshake and not 2-way?",
                            "a": "A 2-way handshake would only prove that the server heard the client. The 3rd step (ACK) is required to prove to the server that the client is still there and heard the server's response. This prevents 'half-open' connections that waste server resources."
                        },
                        {
                            "q": "What is a SYN Flood Attack?",
                            "a": "An attacker sends thousands of SYN requests (Step 1) but never sends the final ACK (Step 3). The server keeps resources 'reserved' in the SYN-RECEIVED state for these fake connections until it runs out of memory and crashes."
                        },
                        {
                            "q": "What are ISNs and why are they random?",
                            "a": "Initial Sequence Numbers are random to prevent 'Sequence Number Guessing' attacks, where a hacker could inject fake data into a session if they knew exactly what number came next."
                        }
                    ]
                }
            ]
        },
        {
            "id": "tcp-ip",
            "title": "TCP/IP Protocol Suite",
            "description": "The four-layer network model that powers the modern internet.",
            "cards": [
                {
                    "type": "text",
                    "heading": "TCP/IP vs OSI Overview",
                    "content": "The TCP/IP model condenses the OSI into 4 functional layers that represent practical implementation rather than theoretical purity.\n\n• **Network Access Layer:** Maps to physical & data link layers.\n• **Internet Layer:** Maps to network layer.\n• **Transport Layer:** Maps directly to transport layer.\n• **Application Layer:** Maps to session, presentation, and application layers."
                },
                {
                    "type": "text",
                    "heading": "Application Layer (TCP/IP)",
                    "content": "Unlike the OSI model, this layer handles all high-level protocols, data representation, and session management tasks.\n\n• **Protocols:** HTTP(S), FTP, SMTP, DNS, SSH.\n• **Usage:** Direct interface for user applications requesting network services."
                },
                {
                    "type": "text",
                    "heading": "Transport Layer (TCP/IP)",
                    "content": "Provides reliable or unreliable data delivery depending on the required protocol.\n\n• **TCP:** Reliable, connection-oriented, acknowledges data, ensures ordered delivery.\n• **UDP:** Unreliable, connectionless, fast, no acknowledgments. Ideal for video and gaming."
                },
                {
                    "type": "text",
                    "heading": "Internet Layer (TCP/IP)",
                    "content": "Responsible for logical transmission across different networks via routing.\n\n• **Core Protocol:** Internet Protocol (IPv4/IPv6).\n• **Companion Protocols:** ICMP (for ping/errors), ARP (resolves IP to MAC)."
                },
                {
                    "type": "text",
                    "heading": "Network Access Layer (TCP/IP)",
                    "content": "Handles hardware-level transmission and physical addressing to send raw data bits over physical media.\n\n• **Responsibilities:** MAC addressing, CSMA/CD, signaling, physical cabling."
                }
            ]
        },
        {
            "id": "network-devices",
            "title": "Network Devices",
            "description": "Hardware mechanisms used to connect and route data across computers.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Hub (Layer 1)",
                    "content": "A basic, non-intelligent device that broadcasts data to all connected ports.\n\n• **Operation:** Multiport repeater. When it receives a signal, it copies it out to all other ports.\n• **Drawback:** High collision rates and extreme security vulnerabilities since all nodes see all traffic."
                },
                {
                    "type": "text",
                    "heading": "Switch (Layer 2)",
                    "content": "An intelligent multiport device that learns MAC addresses and sends data only to the specific intended port.\n\n• **Operation:** Consults its internal MAC Address Table to forward frames.\n• **Advantage:** Eliminates collisions via full-duplex transmission and improves security."
                },
                {
                    "type": "text",
                    "heading": "Router (Layer 3)",
                    "content": "A highly intelligent edge device that connects multiple different IP networks together.\n\n• **Operation:** Inspects destination IP addresses and consults Routing Tables to determine the optimal path for packets.\n• **Usage:** Connects a LAN to a WAN (like the internet)."
                },
                {
                    "type": "text",
                    "heading": "Gateway & Firewall",
                    "content": "Advanced security and translation nodes.\n\n• **Gateway:** Translates traffic between utterly different network architectures (e.g., LAN to external Cloud architecture).\n• **Firewall:** Hardware or software that strictly filters incoming and outgoing packets based on predefined security rules."
                }
            ]
        },
        {
            "id": "ip-addressing",
            "title": "IP Addressing",
            "description": "Logical systems required to identify machines globally on a network.",
            "cards": [
                {
                    "type": "text",
                    "heading": "IPv4 Overview",
                    "content": "The fourth version of the Internet Protocol, still heavily used globally.\n\n• **Format:** 32-bit address, represented in four decimal octets (e.g., 192.168.1.1).\n• **Capacity:** Provides approximately 4.3 billion unique addresses, which are now exhausted."
                },
                {
                    "type": "text",
                    "heading": "IPv4 Classes & Subnetting",
                    "content": "Addresses are broken down into Network and Host portions.\n\n• **Class A:** Massive networks (0.0.0.0 to 127.255.255.255).\n• **Class B:** Medium networks (128.0.0.0 to 191.255.255.255).\n• **Class C:** Small networks (192.0.0.0 to 223.255.255.255).\n• **Subnetting (CIDR):** Replaced legacy classes to allow dynamic allocation of bits via prefix length like /24."
                },
                {
                    "type": "text",
                    "heading": "IPv6 Overview",
                    "content": "The modern iteration of IP addressing designed to solve the exhaustion problem.\n\n• **Format:** 128-bit hexadecimal address containing 8 groups of 4 hex digits (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).\n• **Enhancements:** Offers essentially infinite unique addresses, built-in IPSec encryption, and no need for NAT (Network Address Translation)."
                }
            ]
        },
        {
            "id": "network-security",
            "title": "Network Security Topics",
            "description": "Defending network infrastructure and transmission from cyber threats.",
            "cards": [
                {
                    "type": "text",
                    "heading": "DDoS (Distributed Denial of Service)",
                    "content": "A malicious attempt to disrupt normal traffic of a targeted server by overwhelming it with a flood of Internet traffic.\n\n• **Mechanism:** Botnets send thousands of requests concurrently.\n• **Impact:** The server runs out of memory or compute resources, preventing legitimate users from accessing it."
                },
                {
                    "type": "text",
                    "heading": "Man-in-the-Middle (MitM) Attacks",
                    "content": "An attacker secretly relays and possibly alters the communication between two parties who believe they are directly communicating.\n\n• **Mechanism:** Often occurs via ARP poisoning or malicious open Wi-Fi hotspots.\n• **Countermeasure:** Enforcing TLS/SSL certificates and encrypted communication tunnels."
                },
                {
                    "type": "text",
                    "heading": "VPNs & IPsec",
                    "content": "Creating secure connections over untrusted networks.\n\n• **Virtual Private Network:** Establishes encrypted tunnels passing through the internet.\n• **IPsec:** A suite of protocols to secure IP communications by authenticating and encrypting each IP packet of a session."
                }
            ]
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        
    print("Re-populated CN data with extensive multi-card details.")
except Exception as e:
    print(f"Error: {e}")
