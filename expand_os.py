import json

file_path = "frontend-app/src/data/cs_notes.json"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    os_topics = [
        {
            "id": "what-is-os",
            "title": "Main Functions of an OS",
            "description": "Think of these as the Department Managers of a company.",
            "cards": [
                {
                    "type": "list",
                    "heading": "Core Functions",
                    "content": "**Process Management:** The OS keeps track of all running programs (Processes). It uses a Scheduler to decide which process gets the CPU and for how long.\n\n**Memory Management:** The OS manages the RAM. It tracks which parts are in use and by whom. It also uses Virtual Memory to let you run programs larger than your actual RAM.\n\n**File System Management:** It maps logical files to physical storage locations (HDD/SSD). It manages permissions (who can read/write).\n\n**I/O Management:** The OS uses Device Drivers to talk to hardware like keyboards, mice, and printers. It provides Buffering and Caching to speed up slow devices.\n\n**Security & Protection:** It ensures that Process A cannot peek into the memory of Process B and that unauthorized users cannot access files."
                }
            ]
        },
        {
            "id": "os-types",
            "title": "Types of Operating Systems (Evolution)",
            "description": "How operating systems have evolved to handle different workloads and architectures.",
            "cards": [
                {
                    "type": "table",
                    "heading": "Evolution of OS",
                    "content": "",
                    "headers": ["System Type", "Logic", "Real-World Context"],
                    "rows": [
                        ["Batch OS", "Users leave jobs with an operator; jobs are grouped by type.", "High-volume, repetitive tasks (Payroll, Bank statements)."],
                        ["Multiprogramming", "When one job waits for I/O, the CPU picks another. Keeps CPU busy.", "Early mainframe systems to maximize expensive CPU time."],
                        ["Multitasking", "CPU switches so fast between jobs that it feels like they run together.", "Modern PCs (running Chrome, Spotify, and Word at once)."],
                        ["Real-Time (RTOS)", "Logic is based on Time. The result must be correct and delivered on time.", "Hard RTOS: Airbag systems, Pacemakers. Soft RTOS: Video Streaming."],
                        ["Distributed OS", "Multiple independent CPUs appear as a single machine to the user.", "Large-scale server clusters, Cloud computing."],
                        ["Embedded OS", "Stripped-down OS for specific tasks with limited power/RAM.", "Microwave ovens, IoT devices, Car ECUs."]
                    ]
                }
            ]
        },
        {
            "id": "kernel-and-system-calls",
            "title": "Core Concepts: Kernel & System Calls",
            "description": "These are the most fundamental \"under-the-hood\" concepts often asked in technical rounds.",
            "cards": [
                {
                    "type": "text",
                    "heading": "The Kernel",
                    "content": "The Kernel is the heart of the OS. It is the first program loaded when the computer starts and remains in the RAM until the system shuts down.\n\n**Function:** It manages the communication between software and hardware.\n\n**Privilege:** It runs in Kernel Mode (Ring 0), giving it full access to all hardware. User applications run in User Mode, which is restricted for security."
                },
                {
                    "type": "list",
                    "heading": "Types of Kernels",
                    "content": "**Monolithic Kernel:** All OS services (File system, drivers, memory management) run in a single large process in kernel space.\n• **Pros:** Very fast (no communication overhead).\n• **Cons:** If one service crashes (like a printer driver), the whole system crashes. (e.g., Linux).\n\n**Microkernel:** Only the absolute essentials (scheduling, basic IPC) stay in the kernel. Everything else (drivers, file systems) runs as \"user services.\"\n• **Pros:** Highly stable and secure. If a driver crashes, the kernel survives.\n• **Cons:** Slower due to constant message passing between user and kernel space. (e.g., L4, Minix).\n\n**Hybrid Kernel:** A mix of both, trying to balance speed and stability. (e.g., Windows NT, macOS)."
                },
                {
                    "type": "text",
                    "heading": "System Calls",
                    "content": "A System Call is the programmatic way a computer program requests a service from the kernel.\n\n**Mechanism:** Since user apps cannot touch hardware directly, they use a \"System Call\" to ask the Kernel to do it for them.\n\n**Example:** When you write `printf(\"Hello\")` in C, it eventually triggers a `write()` system call to send data to the monitor.\n\n**Types:** Process Control (fork), File Management (open, read), Device Management, Information Maintenance, and Communication."
                }
            ]
        },
        {
            "id": "interrupts",
            "title": "Interrupts: The OS \"Wake-up Call\"",
            "description": "An Interrupt is a signal sent to the processor by hardware or software indicating an event that needs immediate attention.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Mechanics",
                    "content": "When an interrupt occurs, the CPU suspends its current activities, saves its state (registers and program counter), and executes a small piece of code called the Interrupt Service Routine (ISR) or Interrupt Handler."
                },
                {
                    "type": "list",
                    "heading": "Types of Interrupts",
                    "content": "**1. Hardware Interrupts:** Triggered by external devices (e.g., a mouse click, a keyboard press, or a hard drive finishing a data read).\n**2. Software Interrupts (Traps):** Triggered by errors (like division by zero) or specifically by a program using a System Call to request kernel services.\n**3. Vectored vs. Non-Vectored:** In Vectored interrupts, the device supplies the address of the ISR. In Non-vectored, the ISR address is fixed at a specific memory location."
                }
            ]
        },
        {
            "id": "os-structure-booting",
            "title": "OS Structure & Booting",
            "description": "Architectural configurations and booting sequences of operating systems.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Operating System Structures",
                    "content": "**1. Simple Structure (MS-DOS):** No clear separation between layers. Applications can access hardware directly. Not secure.\n\n**2. Layered Structure:** Each layer uses services of lower layer. Easy to debug and maintain but slower due to multiple layers.\n\n**3. Modular Structure (Linux):** Core kernel + loadable modules. Modules can be loaded/unloaded at runtime. Flexible and efficient."
                },
                {
                    "type": "text",
                    "heading": "Booting Process",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>1. Power On\n   │\n2. BIOS/UEFI runs POST (Power-On Self Test)\n   │\n3. Load bootloader from boot device\n   │\n4. Bootloader loads kernel into memory\n   │\n5. Kernel initializes hardware\n   │\n6. Start init process (PID 1) and Load system services\n   │\n7. Display login prompt</pre>"
                }
            ]
        },
        {
            "id": "process-vs-thread",
            "title": "Process vs. Thread: The Deep Dive",
            "description": "This is a high-frequency interview topic. Think of a Process as a \"Container\" and a Thread as a \"Worker\" inside that container.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Process",
                    "content": "A process is a program in execution. It is an independent entity with its own dedicated memory space (Heap, Stack, Data).\n\n**Characteristics:** High overhead to create, high overhead for Context Switching, and very secure (one process cannot easily crash another).\n\n**Communication:** Processes use IPC (Inter-Process Communication) like Pipes, Sockets, or Shared Memory."
                },
                {
                    "type": "text",
                    "heading": "Thread",
                    "content": "A thread is a \"Lightweight Process.\" It is the smallest unit of CPU utilization. Multiple threads can exist within a single process.\n\n**Shared Resources:** Threads share the Code, Data, and OS Resources (like open files) of their parent process, but they have their own Registers, Program Counter, and Stack.\n\n**Characteristics:** Low overhead, extremely fast communication (since they share memory), but less stable (if one thread crashes and corrupts memory, the whole process dies)."
                },
                {
                    "type": "table",
                    "heading": "Comparison Summary",
                    "content": "",
                    "headers": ["Feature", "Process", "Thread"],
                    "rows": [
                        ["Definition", "An independent program in execution.", "A segment of a process (Worker)."],
                        ["Memory", "Isolated memory space.", "Shared memory space with sibling threads."],
                        ["Context Switching", "Slow (must save/load entire address space).", "Fast (only registers and stack change)."],
                        ["Stability", "Highly stable (Isolated).", "One thread can crash the whole process."]
                    ]
                }
            ]
        },
        {
            "id": "cpu-scheduling",
            "title": "CPU Scheduling Algorithms",
            "description": "The OS uses these algorithms to decide which process in the 'Ready Queue' gets the CPU next to keep it as busy as possible (CPU Utilization) and minimize wait time.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Key Terminology",
                    "content": "**Arrival Time:** When the process enters the ready queue.\n**Burst Time:** Time required by the process for execution on the CPU.\n**Completion Time:** When the process finishes execution.\n**Waiting Time:** (Turnaround Time – Burst Time).\n**Turnaround Time:** Total time taken from arrival to completion (Completion Time – Arrival Time).\n**Response Time:** Time from arrival until the process gets the CPU for the first time."
                },
                {
                    "type": "text",
                    "heading": "1. First-Come, First-Served (FCFS)",
                    "content": "The simplest algorithm. It works on the FIFO (First-In, First-Out) principle.\n\n**Logic:** The process that requests the CPU first gets it first.\n**Nature:** Non-preemptive (Once a process starts, it won't stop until finished).\n**The Problem:** Convoy Effect. If a process with a very high burst time arrives first, all short processes behind it are blocked, leading to poor average waiting time."
                },
                {
                    "type": "text",
                    "heading": "2. Shortest Job First (SJF)",
                    "content": "This algorithm links the length of the process's next CPU burst to the scheduling decision.\n\n**Logic:** Pick the process with the smallest burst time.\n**Nature:** Can be Non-preemptive or Preemptive.\nPreemptive SJF is called **Shortest Remaining Time First (SRTF)**. If a new process arrives with a burst time shorter than the remaining time of the current process, the current one is kicked out.\n**Pros:** Theoretically optimal; provides the minimum average waiting time.\n**Cons:** Hard to predict the next burst time; can lead to Starvation of long processes."
                },
                {
                    "type": "text",
                    "heading": "3. Priority Scheduling",
                    "content": "Each process is assigned a priority (usually an integer).\n\n**Logic:** CPU is allocated to the process with the highest priority (lowest integer usually means highest priority).\n**Problem:** Starvation (Indefinite Blocking). A low-priority process may never run if high-priority processes keep arriving.\n**Solution:** Aging. Gradually increase the priority of processes that have been waiting in the queue for a long time."
                },
                {
                    "type": "text",
                    "heading": "4. Round Robin (RR)",
                    "content": "Designed specifically for time-sharing systems.\n\n**Logic:** Each process is assigned a small unit of time called a Time Quantum (usually 10-100ms). The CPU moves in a circle through the ready queue.\n**Nature:** Preemptive.\n**Performance:** Heavily dependent on the time quantum.\n• If the quantum is too large, it behaves like FCFS.\n• If too small, context switching overhead becomes massive."
                },
                {
                    "type": "text",
                    "heading": "5. Multilevel Queue Scheduling",
                    "content": "This divides the ready queue into several separate queues (e.g., Foreground/Interactive and Background/Batch).\n\n**Logic:** Each queue has its own scheduling algorithm (e.g., Foreground uses RR, Background uses FCFS).\n**Nature:** Fixed priority. The foreground queue must be empty before the background queue can run."
                },
                {
                    "type": "text",
                    "heading": "6. Multilevel Feedback Queue (MLFQ)",
                    "content": "Unlike the standard Multilevel Queue, this allows processes to move between queues.\n\n**Logic:** If a process uses too much CPU time, it is moved to a lower-priority queue. If a process waits too long in a lower queue, it is moved up (Aging).\n**Goal:** To separate processes based on their CPU burst characteristics."
                },
                {
                    "type": "text",
                    "heading": "Comparative Example",
                    "content": "Assume we have 3 processes arriving at time 0 with Burst Times: P1=24 ms, P2=3 ms, P3=3 ms.\n\n**FCFS Analysis:**\nOrder: P1 -> P2 -> P3. Wait Times: P1=0, P2=24, P3=27. **Average Wait = 17 ms**.\n\n**SJF (Non-preemptive) Analysis:**\nOrder: P2 -> P3 -> P1 (Shortest first). Wait Times: P2=0, P3=3, P1=6. **Average Wait = 3 ms**.\n\n**Round Robin (TQ=4) Analysis:**\nOrder: P1(4) -> P2(3) -> P3(3) -> P1(remaining 20). Wait Times: P1 gets CPU at 0, then again at 10. P2 waits 4. P3 waits 7. **Average Wait ≈ 5.6 ms**."
                }
            ]
        },
        {
            "id": "process-synchronization",
            "title": "Process Synchronization",
            "description": "Process synchronization solves the Race Condition, ensuring that multiple processes don't inconsistently modify shared data.",
            "cards": [
                {
                    "type": "text",
                    "heading": "1. The Race Condition",
                    "content": "A **Race Condition** occurs when multiple processes access and manipulate the same data concurrently, and the final outcome depends on the execution order.\n\n**Example:** Balance = $100. Thread A reads $100, prepares to add $50. Thread B reads $100, prepares to withdraw $20. Thread A writes $150. Thread B writes $80. Result: The $50 deposit is lost due to overwriting."
                },
                {
                    "type": "text",
                    "heading": "2. The Critical Section & Its Requirements",
                    "content": "In any multi-threaded application, the code accessing shared resources is called the **Critical Section**. To avoid Race Conditions, synchronization must satisfy these three mandatory requirements:\n\n**I. Mutual Exclusion (The 'One-at-a-Time' Rule):** If Process P1 is executing in its critical section, no other processes can execute in theirs. *Why:* Without this, data corruption is guaranteed.\n\n**II. Progress (The 'No Unnecessary Waiting' Rule):** If no process is in the critical section and some processes want to enter, only those not in their 'remainder section' can decide who enters next. *Why:* Ensures the decision is made immediately and isn't blocked by uninterested processes.\n\n**III. Bounded Waiting (The 'No Starvation' Rule):** There must be a limit on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter. *Why:* Prevents Starvation so a process doesn't wait forever while 'faster' processes cut in line."
                },
                {
                    "type": "text",
                    "heading": "3. Semaphores: The Deep Dive",
                    "content": "A **Semaphore** is a protected integer variable that acts as a signal to manage concurrent processes. It is accessed via two atomic operations: `wait()` and `signal()`.\n\n**A. Binary Semaphore (The Mutex):** Can only be 0 or 1.\n• **How it works:** Starts at 1. When entering a critical section, `wait()` makes it 0. Others find it 0 and sleep. When finished, `signal()` makes it 1 and wakes a sleeper.\n• **Where/Why it's used:** Used for *Mutual Exclusion* to protect a single shared resource (e.g., one printer) from being accessed by >1 thread at a time.\n\n**B. Counting Semaphore (The Resource Manager):** Any non-negative integer (0 to N).\n• **How it works:** Initialized to the number of resources (e.g., S=5). When taking a resource, `wait()` drops S. When S=0, next process waits. Once done, `signal()` increments S.\n• **Where/Why it's used:** Used for *Resource Management* of a \"pool\" of identical resources (e.g., 10 database connections)."
                },
                {
                    "type": "text",
                    "heading": "4. The Producer-Consumer Problem",
                    "content": "A classic synchronization challenge involving a fixed-size buffer where a Producer adds data and a Consumer removes it.\n\n**Problems to Solve:**\n• **Buffer Overflow:** Producer shouldn't add if full.\n• **Buffer Underflow:** Consumer shouldn't remove if empty.\n• **Race Condition:** Both shouldn't touch the buffer at the same exact microsecond.\n\n**The 3 Semaphores (Tools):**\n• `mutex`: A binary semaphore (initially 1) ensures only one person touches the buffer.\n• `empty`: A counting semaphore (initially N) tracks empty slots.\n• `full`: A counting semaphore (initially 0) tracks filled slots."
                },
                {
                    "type": "text",
                    "heading": "5. Step-by-Step Logic",
                    "content": "**The Producer's Logic:**\n1. `Wait(empty)`: Decrements empty count. If full (empty=0), waits.\n2. `Wait(mutex)`: Locks the buffer.\n3. **Add Item** to the buffer.\n4. `Signal(mutex)`: Unlocks the buffer.\n5. `Signal(full)`: Increments full count. \"There's food ready!\"\n\n**The Consumer's Logic:**\n1. `Wait(full)`: Decrements full count. If empty (full=0), waits.\n2. `Wait(mutex)`: Locks the buffer.\n3. **Remove Item** from the buffer.\n4. `Signal(mutex)`: Unlocks the buffer.\n5. `Signal(empty)`: Increments empty count. \"I freed up a spot!\""
                }
            ]
        },
        {
            "id": "deadlock",
            "title": "Deadlock",
            "description": "A situation where processes are waiting for resources held by each other, creating an infinite cycle.",
            "cards": [
                {
                    "type": "text",
                    "heading": "1. The 4 Necessary Conditions (Coffman Conditions)",
                    "content": "For a deadlock to exist, all four of these conditions must be true simultaneously. If you can break even one, deadlock becomes impossible.\n\n**Mutual Exclusion:** At least one resource must be held in a non-shareable mode (Only one process can use it at a time).\n**Hold and Wait:** A process must be holding at least one resource and waiting to acquire additional resources held by others.\n**No Preemption:** Resources cannot be forcibly taken. The process must release them voluntarily.\n**Circular Wait:** A set of processes exists such that P0 is waiting for P1, P1 is waiting for P2, and Pn is waiting for P0. This forms a closed loop."
                },
                {
                    "type": "text",
                    "heading": "2. Handling Deadlock: The 4 Strategies",
                    "content": "**I. Deadlock Prevention (The Strict Rule-Maker):** Break one Coffman condition. *Mutual Exclusion:* Make resources shareable. *Hold and Wait:* Request all resources at the beginning. *No Preemption:* Release current resources if a new request fails. *Circular Wait:* Force ordered resource requests.\n\n**II. Deadlock Avoidance (The Banker's Algorithm):** OS looks at every request and asks if it leaves the system in a *Safe State*. Maintains tables for Available, Max Need, and Currently Allocated.\n\n**III. Deadlock Detection & Recovery (The Detective):** OS lets deadlocks happen, detects cycles via Resource Allocation Graph (RAG), and recovers via *Process Termination* or *Resource Preemption*.\n\n**IV. Deadlock Ignorance (The Ostrich Algorithm):** OS pretends deadlocks don't exist. Mathematical cost of Banker's Algorithm is too high for general PCs. If a hang happens, user restarts the app/PC."
                }
            ]
        },
        {
            "id": "ipc",
            "title": "Inter-Process Communication (IPC)",
            "description": "IPC allows processes to communicate and synchronize securely.",
            "cards": [
                {
                    "type": "text",
                    "heading": "1. The Two Primary Models of IPC",
                    "content": "**I. Shared Memory Model:** A region of memory is shared by processes. Process A creates it, Process B attaches to it.\n• **Pros:** Extremely fast (memory speeds, no Kernel involvement for every message).\n• **Cons:** Hard to implement. Requires synchronization (Semaphores) to prevent race conditions.\n\n**II. Message Passing Model:** Processes exchange messages via a Kernel \"mailbox\" or \"buffer\". Process A uses `send()`, Process B uses `receive()`.\n• **Pros:** Easier in distributed systems. More secure because Kernel manages synchronization.\n• **Cons:** Slower. Every communication requires a System Call and context switch."
                },
                {
                    "type": "list",
                    "heading": "2. Common IPC Techniques",
                    "content": "**A. Pipes (Ordinary and Named):** For related processes. Ordinary Pipes: Unidirectional, die when process finishes. Named Pipes (FIFOs): Bi-directional, persist as files.\n**B. Sockets:** Most flexible. For processes on same or different machines. Identified by IP/Port.\n**C. Message Queues:** Linked list of messages in kernel. Asynchronous (sender doesn't wait).\n**D. Signals:** Notifications sent to a process (e.g., Ctrl+C sends SIGINT). Simplest but limited."
                },
                {
                    "type": "text",
                    "heading": "3. Direct vs. Indirect Communication",
                    "content": "**Direct Communication:** Each process must explicitly name the recipient or sender. e.g., `send(P, message)`, `receive(Q, message)`.\n\n**Indirect Communication:** Messages are sent to and received from mailboxes/ports. e.g., `send(mailbox_A, message)`. Sender doesn't care who picks it up, as long as they access mailbox A."
                },
                {
                    "type": "list",
                    "heading": "4. Synchronization in IPC",
                    "content": "**Blocking (Synchronous):** The sender is blocked until the message is received. Receiver is blocked until message is available.\n**Non-blocking (Asynchronous):** The sender sends the message and resumes work immediately. Receiver retrieves either a valid message or a null."
                }
            ]
        }
    ]

    data["os"]["topics"] = os_topics

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Updated Operating Systems section with full exhaustive scope!")
except Exception as e:
    print(f"Error: {e}")
