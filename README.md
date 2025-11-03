# Elevator Management System (Python Simulation)

A Python-based **Elevator Management System** that simulates multiple elevators in a building.  
It handles floor requests, assigns the optimal elevator, and tracks elevator states — all in real-time using multithreading.

---

##  Features

- 🏙️ Simulates **multiple elevators** in a multi-floor building  
- 🎯 Automatically **assigns the nearest idle elevator** for each request  
- 🔄 Tracks **elevator states** — idle, moving, or doors open  
- 🧠 Uses **OOP concepts** (classes, enums, encapsulation)  
- ⏱️ Realistic **timing simulation** using `time.sleep()`  
- ⚙️ Supports **concurrent elevator movement** using Python `threading`  

---

## Project Structure

Elevator-Management-System/
│
├── elevator_system.py # Main simulation code
├── README.md # Project documentation

---

## How It Works

1. The user specifies:
   - Number of elevators  
   - Number of floors  

2. The system listens for commands:
request <floor> <up/down> → Call an elevator to that floor
status → Show elevator positions and states
quit → Exit simulation


3. The controller picks the **closest idle elevator** and moves it toward the requested floor.  
4. Each elevator moves independently and updates its state during the simulation.

---

## 💻 Example Run (Sample Output)

```bash
=== Elevator Management System — Simulation ===
Enter number of elevators: 2
Enter number of floors in building: 10

Commands:
request <floor> <up/down>  → Call an elevator to that floor
status                     → Show elevator positions and states
quit                       → Exit simulation

Enter command: request 6 up

[Controller] Assigning Elevator 1 to floor 6 (up)
Elevator 1 starting from floor 1 to 6 ↑
Elevator 1 at floor 2...
Elevator 1 at floor 3...
Elevator 1 at floor 4...
Elevator 1 at floor 5...
Elevator 1 at floor 6...
🚪 Elevator 1 doors opening at floor 6
🔒 Elevator 1 doors closing at floor 6

Enter command: status
===== Elevator Status =====
Elevator 1: Floor 6, State: idle
Elevator 2: Floor 1, State: idle
============================

Enter command: quit
Shutting down system...

---
