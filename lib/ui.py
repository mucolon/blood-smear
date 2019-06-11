# ui.py
# This file declares a class to take all user inputs


class UserI:

    def linear_speed(self):
        # function: ask for motor load's speed
        while True:
            try:
                self.linSpeed = float(
                    input("\nEnter linear travel speed of the motor's load [0-1000 mm/s]: "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.linSpeed > 1000:
                print("Error: Max linear speed is 1000 mm/s")
                continue
            elif self.linSpeed < 0:
                print("Error: Linear speed cannot be negative")
                continue
            else:
                break
        return self.linSpeed

    def rotations(self):
        # function: ask for motor rotations
        while True:
            try:
                self.rot = float(
                    input("\nEnter amount of motor rotations [0-2.9]: "))
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

    def direction(self):
        # function: ask for motor direction
        while True:
            try:
                self.dir = str(input("Enter motor direction [cw or ccw]: "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.dir == "cw":
                break
            elif self.dir == "ccw":
                break
            else:
                print("Error: Invalid input\
                    \n[cw] for clockwise\
                    \n[ccw] for counter-clockwise")
                continue
        return self.dir

    def micro_steps(self):
        # function: ask for motor micro step count
        while True:
            try:
                self.microStep = int(
                    input("\nEnter motor micro step count (enter 0 for help): "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.microStep == 0:
                print("\n1 micro step = 200 pulses")
                print("2 micro steps = 400 pulses")
                print("4 micro steps = 800 pulses")
                print("8 micro steps = 1600 pulses")
                print("10 micro steps = 2000 pulses")
                print("16 micro steps = 3200 pulses")
                print("32 micro steps = 6400 pulses")
                print("Check motor driver for configured micro step count")
                continue
            elif self.microStep not in (1, 2, 4, 8, 10, 16, 32):
                print("Error: Invalid value (type 0 for help)")
                continue
            else:
                break
        return self.microStep

    def linear_dist(self):
        # function: ask for the motor's load linear travel distance
        while True:
            try:
                self.dist = float(
                    input("Enter linear travel distance of motor's load [0-210 mm]: "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.dist > 210:
                print("Error: Max linear travel distance is 210")
                continue
            elif self.rot < 0:
                print("Error: Linear travel distance cannot be negative")
                continue
            else:
                break
        return self.dist
