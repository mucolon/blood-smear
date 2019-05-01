# This is the test code for a basic smear
#
# run program with this line of code below
# sudo python3 basic_smear.py


# importing libraries
from stepper import Stepper
from input_io import Input_io
from ui import UserI
import Adafruit_BBIO.GPIO as GPIO
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


# function to move motor to linear guide home
def home():
    while far_switch.event() != True:
        slide.move_steps(1, 50, ccw)
    print("Home Position")


# main function to move motor
def main():

    # asking for linear spped
    print("Please enter linear speed of smear.")
    input_mms = slide_ui.linear_speed()
    rpm = input_mms * mms2rpm

    # moving motor to blood dispensing site
    print("Moving to blood dispensing site.")
    slide.rotate(1, 50, cw)
    print("Please dipense blood at target location.")
    input("Press any key after blood is dispensed.")

    # moving motor for smearing stage
    print("Preparing for smear.")
    print("Wicking blood")
    slide.rotate(1, 50, cw)

    # input_mms = 100  # [mm/s]
    # input_mms = float(input("Enter linear travel speed [mm/s]: "))
    # input_mms = slide_ui.linear_speed()
    # rpm = input_mms * mms2rpm
    # rpm = 75

    # input_rot = float(input("Enter amount of motor rotations: "))
    # input_rot = slide_ui.rotations()
    input_rot = .7

    # input_dir = input("Enter motor direction [cw or ccw]: ")
    # if input_dir == "cw":
    #     input_dir = cw
    #     dir_text = "Spining Clockwise"
    # elif input_dir == "ccw":
    #     input_dir = ccw
    #     dir_text = "Spining Counterclockwise"
    # else:
    #     print("Error: Invalid input. cw for clockwise. ccw for counterclockwise")
    # input_dir = slide_ui.direction()
    input_dir = ccw

    time.sleep(1)
    # print(input_dir[1])
    print("Smearing blood")
    # slide.rotate(input_rot, rpm, input_dir[0])
    slide.rotate(input_rot, rpm, input_dir)
    print("Completed smear")


if __name__ == "__main__":

    # initializing  classes
    print("Initializing Classes")
    slide = Stepper(config.slide_pins)
    near_switch = Input_io(config.limit_near_pin, "fall")
    far_switch = Input_io(config.limit_far_pin, "fall")
    slide_ui = UserI()

    # confirming power
    input("Press any key after motors are connected to power.")

    # initializing pins
    print("Initializing Pins")
    slide.init_pins()
    near_switch.init_pin()
    far_switch.init_pin()

    # initializing limit switches
    # print("Initilizing Limit Switches")

    # setting stepper motor micro steps
    print("Setting Micro Steps")
    # input_micro = int(input("Enter motor micro steps: "))
    # input_micro = slide_ui.micro_steps()
    input_micro = 1
    slide.micro_steps(input_micro)

    # moving to origin
    print("Moving to home position.")
    home()

    # moving motor
    print("Preparing to make smear.")
    print("Please load slide.")
    input("Press any key after slide is loaded.")
    main()

    # asking to repeat process
    while True:
        try:
            cont = input("Press enter to repeat.\nOR\nPress n to stop: ")
        except ValueError:
            print("Sorry, I didn't understand that.\nTry again")
            continue
        if cont == "":
            main()
            break
        elif cont == "n":
            break
        else:
            print("Press enter to repeat.\nOR\nPress n to stop: ")
            continue

    # cleaning up pins
    print("Cleaning up pins.")
    slide.cleanup()
    near_switch.cleanup()
    far_switch.cleanup()