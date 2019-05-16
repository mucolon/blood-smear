# ui.py
# This file declares a class to take all user inputs


# declaring UI class to handle user inputs
class UserI:

    # function to ask for motor load's speed
    def linear_speed(self):
        while True:
            try:
                self.linSpeed = float(input("\nEnter linear travel speed of the motor's load [0-200 mm/s]: "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.linSpeed > 200:
                print("Error: Max linear speed is 200 mm/s")
                continue
            elif self.linSpeed < 0:
                print("Error: Linear speed cannot be negative")
                continue
            else:
                break
        return self.linSpeed

    # function to ask for motor rotations
    def rotations(self):
        while True:
            try:
                self.rot = float(input("\nEnter amount of motor rotations [0-2.9]: "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.rot > 2.9:
                print("Error: Max rotations is 2.9")
                continue
            elif self.rot < 0:
                print("Error: Rotations cannot be negative")
                continue
            else:
                break
        return self.rot

    # function to ask for motor direction
    def direction(self):
        while True:
            try:
                print("\nNo quotation marks necessary")
                self.dir = str(input("Enter motor direction [cw or ccw]: "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.dir == "cw":
                break
            elif self.dir == "ccw":
                break
            else:
                print("Error: Invalid input\ncw for clockwise\nccw for counterclockwise")
                continue
        return self.dir

    # function to ask for motor micro step count
    def micro_steps(self):
        while True:
            try:
                self.microStep = int(input("\nEnter motor micro step count (enter 0 for help): "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.microStep == 0:
                print("\n1 micro step = 200 pulses")
                print("2 micro steps = 400 pulses")
                print("4 micro steps = 800 pulses")
                print("8 micro steps = 1600 pulses")
                print("16 micro steps = 3200 pulses")
                print("32 micro steps = 6400 pulses")
                print("Check motor driver for configured micro step count")
                continue
            elif self.microStep not in (1, 2, 4, 8, 16, 32):
                print("Error: Invalid value (type 0 for help)")
                continue
            else:
                break
        return self.microStep

    # function to ask for the motor's load linear travel distance
    def linear_dist(self):
        while True:
            try:
                self.dist = float(input("Enter linear travel distance of motor's load [0-210 mm]: "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.dist > 210:
                print("Error: Max linear tavel distance is 210")
                continue
            elif self.rot < 0:
                print("Error: Linear travel distance cannot be negative")
                continue
            else:
                break
        return self.dist