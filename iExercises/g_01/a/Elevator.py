# Write a program that simulates an elevator. The elevator should keep track of its current floor (starting at floor 0) and have a method go_to_floor that moves the elevator to a specified floor. If the elevator is already on the requested floor, it should print a message indicating the elevator is already on that floor. Otherwise, it should print a message saying it is going to the requested floor. Implement this in an Elevator class and demonstrate it by calling the method for different floors.

class Elevator:
    def __init__(self):
        self.current_floor = 0

    def go_to_floor(self, floor):
        if self.current_floor == floor:
            print(f"Elevator is in floor {floor}")
            # self.current_floor = floor
        else:
            print(f"Going to floor {floor}")
            self.current_floor = floor

elevator = Elevator()
elevator.go_to_floor(3)
elevator.go_to_floor(0)