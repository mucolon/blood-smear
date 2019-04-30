# This is the test code for a basic smear
#
# run program with this line of code below
# sudo python3 basic_smear.py


# importing libraries
from stepper import Stepper
from input_io import Input_io
from ui import UserI
# import Adafruit_BBIO.GPIO as GPIO
# import Adafruit_BBIO.PWM as PWM
import time
from math import pi
import config


# declaring constants
cw = 1  # clockwise
ccw = 0 # counterclockwise


# conversion factors
# radius = 13.3         # [mm] from CAD
radius = 72 / (pi * 2)  # [mm] from manufacturer
mms2rpm = 30 / (radius * pi)  # [s/(mm*min)]


# main function to move motor
def main():

    # input_mms = 100  # [mm/s]
    # input_mms = float(input("Enter linear travel speed [mm/s]: "))
    input_mms = slide_ui.linear_speed()
    rpm = input_mms * mms2rpm
    # rpm = 75

    # input_rot = float(input("Enter amount of motor rotations: "))
    input_rot = slide_ui.rotations()

    # input_dir = input("Enter motor direction [cw or ccw]: ")
    # if input_dir == "cw":
    #     input_dir = cw
    #     dir_text = "Spining Clockwise"
    # elif input_dir == "ccw":
    #     input_dir = ccw
    #     dir_text = "Spining Counterclockwise"
    # else:
    #     print("Error: Invalid input. cw for clockwise. ccw for counterclockwise")
    input_dir = slide_ui.direction()

    time.sleep(1)
    print(input_dir[1])
    slide.rotate(input_rot, rpm, input_dir[0])
    print("Completed rotations")


if __name__ == "__main__":

    # initializing  classes
    print("Initializing Classes")
    slide = Stepper(config.slide_pins)
    near_switch = Input_io(config.limit_near_pin)
    far_switch = Input_io(config.limit_far_pin)
    slide_ui = UserI()

    # initializing pins
    print("Initializing Pins")
    slide.init_pins()
    near_switch.init_pin()
    far_switch.init_pin()

    # setting stepper motor micro steps
    print("Setting Micro Steps")
    # input_micro = int(input("Enter motor micro steps: "))
    input_micro = slide_ui.micro_steps()
    slide.micro_steps(1)

    # moving motor
    main()

    # asking to repeat process
    while True:
        try:
            cont = input("Press enter to repeat\nOR\nPress n to stop: ")
        except ValueError:
            print("Sorry, I didn't understand that.\nTry again.")
            continue
        if cont == "":
            main()
        elif cont == "n":
            break
        else:
            print("Press enter to repeat\nOR\nPress n to stop: ")
            continue

    # cleaning up pins
    print("Cleaning up pins")
    slide.cleanup()