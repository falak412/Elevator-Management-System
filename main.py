from enum import Enum
import time
import threading

# Enums
class ElevatorState(Enum):
    IDLE = "idle"
    MOVING_UP = "moving_up"
    MOVING_DOWN = "moving_down"
    DOORS_OPEN = "doors_open"

class Direction(Enum):
    UP = "up"
    DOWN = "down"

# Elevator Class
class Elevator:
    def __init__(self, eid, total_floors):
        self.id = eid
        self.current_floor = 1
        self.state = ElevatorState.IDLE
        self.total_floors = total_floors
        self.lock = threading.Lock()

    def distance(self, target_floor):
        return abs(self.current_floor - target_floor)

    def move_to(self, target_floor):
        with self.lock:
            if self.state != ElevatorState.IDLE:
                print(f"Elevator {self.id} is busy ({self.state.value}).")
                return

            if target_floor == self.current_floor:
                print(f"Elevator {self.id} already at floor {target_floor}")
                self.open_doors()
                return

            self.state = ElevatorState.MOVING_UP if target_floor > self.current_floor else ElevatorState.MOVING_DOWN
            direction_symbol = "↑" if self.state == ElevatorState.MOVING_UP else "↓"
            print(f"Elevator {self.id} starting from floor {self.current_floor} to {target_floor} {direction_symbol}")

        while self.current_floor != target_floor:
            time.sleep(1)
            self.current_floor += 1 if self.state == ElevatorState.MOVING_UP else -1
            print(f"Elevator {self.id} at floor {self.current_floor}...")

        self.open_doors()

    def open_doors(self):
        with self.lock:
            self.state = ElevatorState.DOORS_OPEN
            print(f"🚪 Elevator {self.id} doors opening at floor {self.current_floor}")
            time.sleep(2)
            self.close_doors()

    def close_doors(self):
        self.state = ElevatorState.IDLE
        print(f"🔒 Elevator {self.id} doors closing at floor {self.current_floor}")

# Controller Class
class ElevatorController:
    def __init__(self, num_elevators, total_floors):
        self.elevators = [Elevator(i + 1, total_floors) for i in range(num_elevators)]
        self.total_floors = total_floors

    def assign_elevator(self, floor, direction):
        idle_elevators = [e for e in self.elevators if e.state == ElevatorState.IDLE]

        if not idle_elevators:
            print("⚠️  All elevators are busy. Please wait...")
            return

        best_elevator = min(idle_elevators, key=lambda e: e.distance(floor))
        print(f"\n[Controller] Assigning Elevator {best_elevator.id} to floor {floor} ({direction.value})")
        threading.Thread(target=best_elevator.move_to, args=(floor,), daemon=True).start()

    def show_status(self):
        print("\n===== Elevator Status =====")
        for e in self.elevators:
            print(f"Elevator {e.id}: Floor {e.current_floor}, State: {e.state.value}")
        print("============================")

# Simulation
def main():
    print("\n=== Elevator Management System — Simulation ===")
    num_elevators = int(input("Enter number of elevators: "))
    total_floors = int(input("Enter number of floors in building: "))

    controller = ElevatorController(num_elevators, total_floors)
    print("\nCommands:")
    print("  request <floor> <up/down>  → Call an elevator to that floor")
    print("  status                     → Show elevator positions and states")
    print("  quit                       → Exit simulation")

    while True:
        cmd = input("\nEnter command: ").lower().split()
        if not cmd:
            continue

        if cmd[0] == "quit":
            print("Shutting down system...")
            break

        elif cmd[0] == "status":
            controller.show_status()

        elif cmd[0] == "request" and len(cmd) == 3:
            try:
                floor = int(cmd[1])
                direction = Direction.UP if cmd[2] == "up" else Direction.DOWN
                if 1 <= floor <= total_floors:
                    controller.assign_elevator(floor, direction)
                else:
                    print(f"Invalid floor number. Choose between 1 and {total_floors}.")
            except:
                print("Invalid request format. Example: request 5 up")

        else:
            print("Unknown command. Use: request <floor> <up/down>, status, quit")

if __name__ == "__main__":
    main()
