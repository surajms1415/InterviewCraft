import json
import re

file_path = "frontend-app/src/data/cs_notes.json"

def make_id(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Restructure all existing subjects from "sections" to "topics"
    for subject_key, subject_data in data.items():
        if "sections" in subject_data:
            subject_data["topics"] = []
            for sec in subject_data["sections"]:
                title = sec["subtitle"]
                content = sec["content"]
                
                # Migrate existing sections into the new topic format with single card
                topic_id = make_id(title)
                
                topic_obj = {
                    "id": topic_id,
                    "title": title,
                    "description": content[:100] + "..." if len(content) > 100 else content,
                    "cards": [
                        {
                            "type": "text",
                            "heading": "Overview",
                            "content": content
                        }
                    ]
                }
                subject_data["topics"].append(topic_obj)
            del subject_data["sections"]

    # Now manually inject the incredibly detailed TCP 3-Way Handshake into CN
    tcp_topic = {
        "id": "tcp-3-way-handshake",
        "title": "TCP 3-Way Handshake",
        "description": "Master how modern networks establish reliable connections.",
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
    }
    
    # Insert it properly into CN topics (let's say as the second item, right after OSI model)
    # Find index of TCP/IP or just insert at index 1
    tcp_ip_idx = next((i for i, t in enumerate(data["cn"]["topics"]) if "tcp" in t["id"]), -1)
    if tcp_ip_idx != -1:
        # replace the old TCP/IP vs OSI model with our highly detailed subset, or just add
        data["cn"]["topics"].insert(tcp_ip_idx + 1, tcp_topic)
    else:
        data["cn"]["topics"].insert(1, tcp_topic)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        
    print("Schema restructured to deeply nested cards successfully.")
except Exception as e:
    print(f"Error: {e}")
