import json
import os

cs_topics_path = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\data\cs_topics.json'
examples_path = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\data\examples.json'

with open(cs_topics_path, 'r', encoding='utf-8') as f:
    topics_data = json.load(f)
    
with open(examples_path, 'r', encoding='utf-8') as f:
    examples_data = json.load(f)

# Update CN topics
cn_topics = {
    "title": "Computer Networks (CN)",
    "description": "Comprehensive networking principles from OSI models to Routing algorithms and Error Detection techniques.",
    "categories": [
        {
            "name": "1. Network Models (OSI vs TCP/IP)",
            "topics": [
                {"name": "OSI Physical & Data Link", "explanation": "Physical: Raw bit transmission, Topologies (Mesh, Star). Data Link: Node-to-node frame delivery, MAC addressing, Flow Control, Error checking."},
                {"name": "OSI Network & Transport", "explanation": "Network: IP logical addressing and Routing (Source to Destination). Transport: Process-to-process delivery, ensuring reliability (TCP) or speed (UDP)."},
                {"name": "OSI Upper Layers", "explanation": "Session: Dialogue control. Presentation: Data translation/encryption/compression. Application: Network services (HTTP/SMTP)."},
                {"name": "TCP/IP Model", "explanation": "4 Layers: Application (merges OSI top 3), Transport, Internet (Network), Network Access (merges bottom 2)."}
            ]
        },
        {
            "name": "2. Network Topologies",
            "topics": [
                {"name": "Mesh & Star", "explanation": "Mesh: Every node interconnected (Highly reliable, very expensive). Star: All nodes connect to central hub (Easy to install, single point of failure)."},
                {"name": "Bus & Ring", "explanation": "Bus: Single shared backbone cable (Cheap, collisions happen). Ring: Circular data path (Simple, one failure breaks ring)."}
            ]
        },
        {
            "name": "3. Data Link Layer (Flow & Error Control)",
            "topics": [
                {"name": "Flow Control (ARQ)", "explanation": "Stop-and-Wait: Wait for ACK before sending next. Go-Back-N: Retransmit failed frame and all subsequent. Selective Repeat: Retransmit only the failed frame."},
                {"name": "Error Detection & MAC", "explanation": "Detect: CRC, Checksum. Correct: Hamming Code. MAC: CSMA/CD (Wired Ethernet Collision Detection), CSMA/CA (Wireless Collision Avoidance)."}
            ]
        },
        {
            "name": "4. Network Layer (IP & Routing)",
            "topics": [
                {"name": "IPv4 Classes & Subnetting", "explanation": "Class A (Large), B (Medium), C (Small). Subnetting borrows bits from Host ID to create manageable sub-networks."},
                {"name": "Routing Algorithms", "explanation": "Distance Vector (DVR): Uses Bellman-Ford, shares full table with neighbors. Link State (LSR): Uses Dijkstra, shares link states with whole network."}
            ]
        },
        {
            "name": "5. Essential Protocols",
            "topics": [
                {"name": "TCP vs UDP", "explanation": "TCP: Connection-oriented, reliable, 3-way handshake (SYN, SYN-ACK, ACK). UDP: Connectionless, fast, unreliable."},
                {"name": "ARP, ICMP, DNS & DHCP", "explanation": "ARP maps IP to MAC. ICMP used for diagnostics (Ping). DNS translates names to IP. DHCP auto-assigns IPs."}
            ]
        }
    ]
}

# Update CN examples
cn_examples = {
    "title": "Computer Networks (CN)",
    "description": "Deep-dive examples into Subnetting and Routing algorithms.",
    "categories": [
        {
            "name": "1. IPv4 Subnetting Example",
            "topics": [
                {
                    "name": "Calculating Subnet details from CIDR",
                    "explanation": "Understanding how to find the Network Address, Broadcast Address, and Range of Host IPs given an IP block.",
                    "example": "Given IP block: 192.168.1.10 /28\n\nStep 1: Understand the CIDR (/28).\nTotal IP bits = 32. Network bits = 28. Host bits = 32 - 28 = 4 bits.\n\nStep 2: Subnet Mask.\n28 ones: 11111111.11111111.11111111.11110000 => 255.255.255.240\n\nStep 3: Block Size (Magic Number).\n256 - 240 = 16. Subnets increment by 16 (0, 16, 32, ...).\n\nStep 4: Find the Subnet.\nThe IP ends in 10. The nearest multiple of 16 below 10 is 0.\nNetwork Address = 192.168.1.0\nBroadcast Address (one less than next subnet 16) = 192.168.1.15\n\nStep 5: Usable Host IP Range.\n192.168.1.1 to 192.168.1.14 (Total 14 usable hosts)."
                }
            ]
        },
        {
            "name": "2. Routing Algorithms",
            "topics": [
                {
                    "name": "Distance Vector vs Link State",
                    "explanation": "Comparative execution of routing protocols.",
                    "example": "Distance Vector (e.g. RIP):\n- Based on Bellman-Ford algorithm.\n- A node shares its ENTIRE routing table, but ONLY with its immediate neighbors.\n- Can suffer from the 'Count to Infinity' problem.\n\nLink State (e.g. OSPF):\n- Based on Dijkstra's Shortest Path algorithm.\n- A node shares information about its IMMEDIATE neighbors, but broadcasts it to the ENTIRE network.\n- Faster convergence, immune to Count to Infinity."
                }
            ]
        }
    ]
}

topics_data['cn'] = cn_topics
examples_data['cn'] = cn_examples

with open(cs_topics_path, 'w', encoding='utf-8') as f:
    json.dump(topics_data, f, indent=4)
with open(examples_path, 'w', encoding='utf-8') as f:
    json.dump(examples_data, f, indent=4)

print("Updated CN theory and examples from GFG!")
