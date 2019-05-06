# ui.py
# This file declares a class to take all user inputs


# declaring UI class to handle user inputs
class UserI:

    # function to ask for motor speed
    def linear_speed(self):
        while True:
            try:
                self.linSpeed = float(input("Enter linear travel speed [0-200 mm/s]: "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.linSpeed > 200:
                print("Error: Max linear speed is 200 mm/s")
                continue
            elif self.linSpeed < 0:
                print("Error: Linear speed can't be negative")
                continue
            else:
                break
        return self.linSpeed

    # function to ask for motor rotations
    def rotations(self):
        while True:
            try:
                self.rot = float(input("Enter amount of motor rotations [0-2.9]: "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.rot > 2.9:
                print("Error: Max rotations is 2.9")
                continue
            elif self.rot < 0:
                print("Error: Rotations can't be negative")
                continue
            else:
                break
        return self.rot

    # function to ask for motor direction
    def direction(self):
        while True:
            try:
                self.string_dir = str(input("Enter motor direction [cw or ccw]: "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if (self.string_dir != "cw") or (self.string_dir != "ccw"):
                print("Error: Invalid input\ncw for clockwise\nccw for counterclockwise")
                continue
            else:
                break
        if self.string_dir == "cw":
            self.dir = 1
            # self.dir_text = "Spinning Clockwise"
        else:
            self.dir = 0
            # self.dir_text = "Spinning Counterclockwise"
        return self.dir #, self.dir_text

    # function to ask for motor micro steps
    def micro_steps(self):
        while True:
            try:
                self.microStep = int(input("Enter motor micro steps (type 0 for help): "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.microStep == 0:
                print("1 micro step = 200 pulses")
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

    def linear_dist(self):
        while True:
            try:
                self.dist = int(input("Enter linear distance [0-210 mm]: "))
            except ValueError:
                print("Error: Invalid Input")
                continue
            if self.dist > 210:
                print("Error: Max linear distance is 210")
                continue
            elif self.rot < 0:
                print("Error: Linear distance can't be negative")
                continue
            else:
                break
        return self.dist