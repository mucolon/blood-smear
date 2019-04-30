# This file declares a class to take all user inputs


# declaring UI class to handle user inputs
class UserI:

    # function to ask for motor speed
    def linear_speed(self):
        while True:
            try:
                self.linSpeed = float(input("Enter linear travel speed [mm/s]: "))
            except ValueError:
                print("Sorry, I didn't understand that.\nTry again.")
                continue
            if self.linSpeed > 200:
                print("Sorry, the max linear speed is 200 mm/s\nTry again.")
                continue
            else:
                break
        return self.linSpeed

    # function to ask for motor rotations
    def rotations(self):
        while True:
            try:
                self.rot = float(input("Enter amount of motor rotations: "))
            except ValueError:
                print("Sorry, I didn't understand that.\nTry agian.")
                continue
            if self.rot > 2.8:
                print("Sorry, the max number of rotations is 2.8\nTry again.")
                continue
            else:
                break
        return self.rot

    # function to ask for motor direction
    def direction(self):
        while True:
            try:
                self.string_dir = input("Enter motor direction [cw or ccw]: ")
            except ValueError:
                print("Sorry, I didn't understand that.\nTry agian.")
                continue
            if (self.string_dir != "cw") or (self.string_dir != "ccw"):
                print("Error: Invalid input. cw for clockwise. ccw for counterclockwise")
                continue
            else:
                break
        if self.string_dir == "cw":
            self.dir = 1
            self.dir_text = "Spining Clockwise"
        else:
            self.dir = 0
            self.dir_text = "Spining Counterclockwise"
        return self.dir, self.dir_text

    # function to ask for motor micro steps
    def micro_steps(self):
        while True:
            try:
                self.microStep = int(input("Enter motor micro steps (type 0 for help): "))
            except ValueError:
                print("Sorry, I didn't understand that.\nTry again.")
                continue
            if self.microStep == 0:
                print("1 micro step = 200 pulses")
                print("2 micro steps = 400 pulses")
                print("4 micro steps = 800 pulses")
                print("8 micro steps = 1600 pulses")
                print("16 micro steps = 3200 pulses")
                print("32 micro steps = 6400 pulses")
                continue
            elif self.microStep is not 1:
                print("Error: Invalid value (type 0 for help)")
                continue
            elif self.microStep is not 2:
                print("Error: Invalid value (type 0 for help)")
                continue
            elif self.microStep is not 4:
                print("Error: Invalid value (type 0 for help)")
                continue
            elif self.microStep is not 8:
                print("Error: Invalid value (type 0 for help)")
                continue
            elif self.microStep is not 16:
                print("Error: Invalid value (type 0 for help)")
                continue
            elif self.microStep is not 32:
                print("Error: Invalid value (type 0 for help)")
                continue
            elif if self.microStep == 1:
                break
            elif if self.microStep == 2:
                break
            elif if self.microStep == 4:
                break
            elif if self.microStep == 8:
                break
            elif if self.microStep == 16:
                break
            elif if self.microStep == 32:
                break
            else:
                break
        return self.microStep