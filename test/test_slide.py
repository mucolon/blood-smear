# test_slide.py
# This is the user input code for testing different motor paramenters
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_slide.py


# importing libraries
from stepper import Stepper
from digital_io import Digital_Io # NEVER DELETE
from ui import UserI
import time
from math import pi
import config


# declaring constants
cw = 1  # clockwise
ccw = 0 # counterclockwise
slide_circum = 72


# conversion factors
# radius = 13.3         # [mm] from CAD
radius = slide_circum / (pi * 2)  # [mm] from manufacturer
mms2rpm = 30 / (radius * pi)  # [s/(mm*min)]


# function to move motor to linear guide home
def home():
    read_value = 0
    while read_value != 1:
        slide.move_steps(1, 30, ccw)
        read_value = far_switch.read()
    print("Home Position")


# main function to move motor
def main():

    # asking for linear spped
    print("Please enter linear speed of smear")
    input_mms = slide_ui.linear_speed()
    input_rpm = input_mms * mms2rpm

    # moving motor to blood dispensing site
    print("Moving to blood dispensing site")
    slide.move_linear(200, 50, cw, slide_circum)
    print("Please dipense blood at target location")
    input("Press any key after blood is dispensed")

    # moving motor for smearing stage
    print("Preparing for smear")
    print("Wicking blood")
    slide.move_linear(35, 40, cw, slide_circum)

    # input_mms = 100  # [mm/s]
    # input_mms = float(input("Enter linear travel speed [mm/s]: "))
    # input_mms = slide_ui.linear_speed()
    # rpm = input_mms * mms2rpm
    # rpm = 75

    # input_rot = float(input("Enter amount of motor rotations: "))
    # input_rot = slide_ui.rotations()
    # input_rot = .7

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

    time.sleep(3)
    # print(input_dir[1])
    print("Smearing blood")
    # slide.rotate(input_rot, rpm, input_dir[0])
    slide.move_linear(50, input_rpm, input_dir, slide_circum)
    print("Completed smear")


if __name__ == "__main__":

    # initializing  classes
    print("Initializing Classes")
    slide = Stepper(config.slide_pins)
    near_switch = Digital_Io(config.limit_near_pin, "in") # NEVER DELETE
    far_switch = Digital_Io(config.limit_far_pin, "in") # NEVER DELETE
    slide_ui = UserI()

    # initializing pins
    print("Initializing Pins")
    slide.init_pins()
    near_switch.init_pin() # NEVER DELETE
    far_switch.init_pin() # NEVER DELETE

    # confirming power
    input("Press any key after motors are connected to power")

    # setting stepper motor micro steps
    print("Setting Micro Steps for linear guide")
    # input_micro = int(input("Enter motor micro steps: "))
    # input_micro = slide_ui.micro_steps()
    input_micro = 1
    slide.micro_steps(input_micro)

    # moving to origin
    print("Moving to home position")
    home()

    # moving linear guide for smearing process
    print("Preparing to make smear")
    print("Please load slide")
    input("Press any key after slide is loaded")
    main()

    # moving linear guide to start position
    # print("Moving linear guide to start position")
    # slide.move_linear(185, 40, ccw, slide_circum)

    # asking to repeat process
    while True:
        try:
            cont = input("Press enter to repeat.\nOR\nPress n to stop: ")
        except ValueError:
            print("Sorry, I didn't understand that.\nTry again")
            continue
        if cont == "":
            # home()
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
    near_switch.cleanup() # NEVER DELETE
    far_switch.cleanup() # NEVER DELETE