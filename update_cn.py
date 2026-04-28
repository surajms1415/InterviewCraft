import json

file_path = "frontend-app/src/data/cs_notes.json"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    data["cn"]["sections"] = [
        {
            "subtitle": "OSI Model (7 Layers)",
            "content": "The Open Systems Interconnection model defines 7 layers for networking (Please Do Not Throw Sausage Pizza Away):\n1. Physical: Raw bit transmission over media (Cat5e, Fiber, Bluetooth). Uses Hubs/Repeaters.\n2. Data Link: Node-to-node frame transfer via MAC addresses. Uses Switches/Bridges.\n3. Network: Logical addressing & routing via Packets using IP/ICMP. Uses Routers.\n4. Transport: End-to-end reliable data transfer (TCP/UDP). Segmentation.\n5. Session: Establishes & terminates connection dialogs (NetBIOS, PPTP).\n6. Presentation: Data translation, compression, and encryption (SSL/TLS, JPEG).\n7. Application: Topmost layer for end-user network services (HTTP, FTP, SSH)."
        },
        {
            "subtitle": "TCP/IP vs OSI Model",
            "content": "The TCP/IP model condenses the OSI into 4 functional layers:\n- Network Access Layer (maps to Physical & Data Link)\n- Internet Layer (maps to Network)\n- Transport Layer (maps to Transport)\n- Application Layer (maps to Session, Presentation, Application)\nUnlike OSI, TCP/IP is the practical, implemented framework of the modern internet."
        },
        {
            "subtitle": "Network Devices",
            "content": "Core hardware to route network traffic:\n- Hub (Layer 1): Broadcasts data to all ports. High collision rate.\n- Switch (Layer 2): Sends data to specific MAC addresses. Intelligent.\n- Router (Layer 3): Directs traffic between disparate IP networks.\n- Gateway: Translates protocols between entirely different networks.\n- Firewall: Filters incoming/outgoing traffic based on security rules."
        },
        {
            "subtitle": "IP Addressing (IPv4 & IPv6)",
            "content": "Every device requires a unique IP to communicate.\n- IPv4: 32-bit address (e.g., 192.168.1.1). Offers ~4.3 billion addresses. Contains a Network ID and Host ID. Divided into Classes (A, B, C, D, E) or Subnetted using CIDR blocks.\n- IPv6: 128-bit address (e.g., fe80::1ff:fe23:4567:890a). Designed to solve IPv4 exhaustion, offering near-infinite addresses. Native IPSec security."
        },
        {
            "subtitle": "Common Network Protocols",
            "content": "- HTTP/HTTPS (Port 80/443): Web traffic transmission (secured via TLS).\n- FTP (Port 21): File Transfer Protocol.\n- SSH (Port 22): Secure shell for encrypted remote connection.\n- SMTP (Port 25): Simple Mail Transfer Protocol for sending email.\n- DNS (Port 53): Domain Name System to resolve domain names to IP addresses.\n- DHCP (Port 67/68): Dynamically assigns IP addresses to devices on a network."
        },
        {
            "subtitle": "Network Security & Cyber Threats",
            "content": "Protecting the integrity of networks:\n- DDoS (Distributed Denial of Service): Overwhelming a server with requests so legitimate traffic fails.\n- Man-in-the-Middle (MitM): Interjecting between user and server to steal data.\n- Phishing: Social engineering to glean login credentials.\n- VPN (Virtual Private Network): Encrypts network tunnels securely.\n- SSL/TLS Handshake: Exchanges cipher suites and encrypts payload in transport."
        }
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        
    print("CN Data Updated Successfully!")
except Exception as e:
    print(f"Error: {e}")
