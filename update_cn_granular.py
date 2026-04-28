import json

file_path = "frontend-app/src/data/cs_notes.json"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ip_addressing_topic = {
        "id": "ip-addressing",
        "title": "IP Addressing",
        "description": "Logical systems required to identify machines globally on a network.",
        "cards": [
            {
                "type": "table",
                "heading": "1. IPv4 Classful Addressing (The Legacy System)",
                "content": "IPv4 uses a 32-bit address space (~4.3 billion addresses). Originally, the internet was divided into five 'Classes' to accommodate different organization sizes.",
                "headers": ["Class", "Range (First Octet)", "Default Subnet Mask", "Use Case"],
                "rows": [
                    ["Class A", "1 – 126", "255.0.0.0 (/8)", "Large Networks: Designed for governments and ISPs. It offers 16 million addresses per network."],
                    ["Class B", "128 – 191", "255.255.0.0 (/16)", "Medium Networks: Designed for large universities and corporations. Offers 65,534 addresses."],
                    ["Class C", "192 – 223", "255.255.255.0 (/24)", "Small Networks: Designed for small businesses. Offers only 254 usable host addresses."],
                    ["Class D", "224 – 239", "N/A", "Multicast: Used for sending data from one source to a specific group."],
                    ["Class E", "240 – 255", "N/A", "Experimental: Reserved for research and future use by IETF/IANA."]
                ]
            },
            {
                "type": "list",
                "heading": "Special IPv4 Addresses to Remember",
                "content": "• **0.0.0.0:** Represents 'any' network or the default route.\n• **127.0.0.1 (Loopback):** Used to test the network stack on your own local machine.\n• **169.254.x.x (APIPA):** Assigned automatically by the OS when the DHCP server is unreachable.\n• **255.255.255.255:** The 'Limited Broadcast' address."
            },
            {
                "type": "list",
                "heading": "2. IPv6: The Modern Protocol",
                "content": "IPv6 was created to solve the exhaustion of IPv4 addresses. It uses a 128-bit address space, represented in Hexadecimal (8 groups of 4 hex digits, separated by colons).\n\n**Characteristics of IPv6:**\n• **Massive Space:** 2^128 addresses (roughly 340 undecillion).\n• **Hexadecimal Notation:** Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334.\n• **Address Compression:** Leading zeros can be omitted, and consecutive groups of zeros can be replaced with `::` (only once per address).\n• **Stateless Address Autoconfiguration (SLAAC):** Devices can generate their own IP address using their MAC address (EUI-64 process) without needing a DHCP server."
            },
            {
                "type": "list",
                "heading": "3. Advantages of IPv6 over IPv4",
                "content": "In a technical round, focus on these five points to show deep knowledge:\n\n• **A. End-to-End Connectivity (No more NAT):** In IPv4, we use NAT to hide multiple private devices behind one public IP. In IPv6, every single device on earth can have a unique, public IP address, restoring true peer-to-peer communication.\n• **B. Efficient Routing (Fixed Header Size):** IPv4 headers vary in size (20 to 60 bytes). IPv6 has a fixed header size of 40 bytes. Because the header is predictable, routers can process packets much faster in hardware.\n• **C. Elimination of Broadcasts:** IPv4 uses Broadcast ('everyone listen!'), which creates massive noise. IPv6 replaces this with Multicast and Anycast.\n• **D. Built-in Security (IPSec):** In IPv4, IPSec is an 'add-on.' In IPv6, IPSec support is a mandatory, integrated feature.\n• **E. Quality of Service (QoS) Support:** IPv6 headers include a Flow Label field. This allows routers to identify and prioritize specific traffic flows (like video streams) without inspecting the encrypted payload."
            },
            {
                "type": "table",
                "heading": "4. Key Differences Table",
                "content": "",
                "headers": ["Feature", "IPv4", "IPv6"],
                "rows": [
                    ["Address Size", "32-bit", "128-bit"],
                    ["Format", "Dotted Decimal (192.168.1.1)", "Hexadecimal (2001:db8::1)"],
                    ["Number of Addresses", "~4.3 Billion", "~340 Undecillion"],
                    ["Configuration", "Manual or DHCP", "SLAAC or DHCPv6"],
                    ["Security", "Optional (IPSec)", "Mandatory/Built-in"],
                    ["Broadcast", "Yes", "No (uses Multicast/Anycast)"],
                    ["NAT", "Required for scaling", "Not needed"]
                ]
            },
            {
                "type": "faq",
                "heading": "Interviewer's Deep Dive Question",
                "questions": [
                    {
                        "q": "What is Anycast in IPv6?",
                        "a": "Anycast is a communication method where multiple servers share the same IP address. A request sent to an Anycast address is routed to the 'nearest' or 'best' server in the group. This is heavily used by CDNs and DNS root servers to reduce latency globally."
                    }
                ]
            }
        ]
    }

    network_security_topic = {
        "id": "network-security",
        "title": "Network Security Topics",
        "description": "Defending network infrastructure and transmission from cyber threats.",
        "cards": [
            {
                "type": "text",
                "heading": "1. Firewalls: The Gatekeepers",
                "content": "A firewall is a security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules.\n\n**Packet Filtering (Layer 3 & 4)**\n• **How it works:** Inspects the header of a packet (Source IP, Dest IP, Protocol, Port).\n• **Pros:** Extremely fast because it doesn't look at payload. Happens at hardware level.\n• **Cons:** Stateless and easily fooled (e.g., malicious script sent through Port 80).\n\n**Application Firewall / WAF (Layer 7)**\n• **How it works:** Deep Packet Inspection (DPI). Looks at the payload data. WAF understands web traffic (HTTP).\n• **Pros:** Highly secure; protects against XSS and SQL Injection.\n• **Cons:** Slow and resource-intensive because it has to read inside every packet."
            },
            {
                "type": "text",
                "heading": "2. Hashing vs. Encryption: Integrity vs. Confidentiality",
                "content": "One of the most common interview traps is confusing these two.\n\n**Hashing (One-Way Function)**\n• **Purpose:** Integrity. Ensure file/password hasn't been tampered with.\n• **Mechanism:** Input run through an algorithm (SHA-256) to produce fixed-length string fingerprint.\n• **Key Characteristic:** Irreversible. Cannot de-hash.\n• **Use Case:** Sites store hashes, not passwords. When you type password, site hashes it and compares.\n\n**Encryption (Two-Way Function)**\n• **Purpose:** Confidentiality. Ensure only authorized parties can read data.\n• **Mechanism:** Use algorithm (AES) + Key to scramble data.\n• **Key Characteristic:** Reversible.\n• **Symmetric:** Same key to lock and unlock (Fast, e.g., AES).\n• **Asymmetric:** Public Key to lock, Private Key to unlock (Secure, e.g., RSA)."
            },
            {
                "type": "list",
                "heading": "3. DDoS (Distributed Denial of Service)",
                "content": "If a DoS attack is one person shouting at you so you can't hear, a DDoS is a stadium full of people shouting simultaneously.\n\n**The Mechanics:** Attacker infects thousands of unprotected devices (Zombies/Bots) forming a Botnet.\n**The Goal:** Overwhelm bandwidth/CPU so legitimate users receive 'Service Unavailable'.\n\n**Defense Strategies:**\n• **Rate Limiting:** Rule stating 'One IP can only make 10 requests/sec.'\n• **CDN (Content Delivery Network):** Cloudflare absorbs the 'shouting' across worldwide servers.\n• **Blackhole Routing:** Shunting all traffic to a black hole to save network (causes downtime)."
            },
            {
                "type": "faq",
                "heading": "4. Bonus: IDS vs. IPS (Placement Specific)",
                "questions": [
                    {
                        "q": "What's the difference between detection and prevention?",
                        "a": "IDS (Intrusion Detection System): Like a security camera. Watches traffic and alerts admin. It does NOT stop the attack.\n\nIPS (Intrusion Prevention System): Like a security guard. Sits 'inline' and instantly drops packets to stop the threat in real-time."
                    }
                ]
            }
        ]
    }

    # Replace the topics
    for i, topic in enumerate(data["cn"]["topics"]):
        if topic["id"] == "ip-addressing":
            data["cn"]["topics"][i] = ip_addressing_topic
        elif topic["id"] == "network-security":
            data["cn"]["topics"][i] = network_security_topic

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Updated IP Addressing and Network Security topics accurately!")
except Exception as e:
    print(f"Error: {e}")
