# This is the test code for a basic smear
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/basic_smear.py


# importing libraries
from stepper import Stepper
from input_io import Input_io
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
    # near_switch.init_pin()
    # near_switch.wait()
    # while near_switch.event() == False:
        # slide.move_steps(1, 50, cw)
    # near_switch.remove_event()

    read_value = 0
    while read_value != 1:
        slide.move_steps(1, 50, cw)
        read_value = near_switch.read()
    print("Home Position")


# main function to move motor
def main():

    slide.enable()
    # asking for linear spped
    print("Please enter linear speed of smear")
    input_mms = slide_ui.linear_speed()
    input_rpm = input_mms * mms2rpm

    # slide loading interface
    print("\nPlease load slide")
    input("Press any key after slide is loaded\n")

    # moving motor to blood dispensing site
    # print("Moving to blood dispensing site")
    # slide.move_linear(100, 50, ccw, slide_circum)
    print("Please dipense blood at target location")
    input("Press any key after blood is dispensed")

    # moving motor for smearing stage
    print("Preparing to wick blood")
    # slide.move_linear(175, 80, cw, slide_circum)
    slide.move_linear(40, 90, cw, slide_circum)
    print("Waiting for blood to wick\n")

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

    # time.sleep(1.5)
    input("Press any key after blood has wicked")
    # print(input_dir[1])
    print("Smearing blood")
    # slide.rotate(input_rot, rpm, input_dir[0])
    slide.move_linear(60, input_rpm, input_dir, slide_circum)
    print("Completed smear\n")

    slide.disable()
    # asking to repeat process
    while True:
        try:
            cont = str(input("Press enter if you're loading another slide\nOR\nPress n to stop: "))
        except ValueError:
            print("Error: Invalid Value")
            continue
        if cont == "":
            # home()
            main()
            break
        elif cont == "n":
            break
        else:
            print("Press enter to repeat\nOR\nPress n to stop: ")
            continue


if __name__ == "__main__":

    # initializing  classes
    # print("\n\nInitializing Classes")
    slide = Stepper(config.slide_pins)
    near_switch = Input_io(config.limit_near_pin, "fall", "pull_up")
    far_switch = Input_io(config.limit_far_pin, "fall", "pull_up")
    slide_ui = UserI()

    # initializing pins
    # print("Initializing Pins")
    slide.init_pins()
    near_switch.init_pin()
    far_switch.init_pin()

    # confirming power
    # input("Press any key after motors are connected to power")

    # setting stepper motor micro steps
    # print("Setting Micro Steps for linear guide")
    # input_micro = int(input("Enter motor micro steps: "))
    # input_micro = slide_ui.micro_steps()
    input_micro = 1
    slide.micro_steps(input_micro)

    # moving to origin
    # print("Moving to home position")
    # home()

    # welcome introduction
    print("Hi there, this a sample run for the Blood Smearing Device")
    print("This run is only for a Proof of Concept Presentation\n")

    # moving linear guide for smearing process
    # print("Preparing to make smear")
    main()
    # slide.disable()

    # moving linear guide to start position
    # print("Moving linear guide to start position")
    # slide.move_linear(185, 40, ccw, slide_circum)

    # # asking to repeat process
    # while True:
    #     try:
    #         cont = str(input("Press enter if you're loading another slide\nOR\nPress n to stop: "))
    #     except ValueError:
    #         print("Error: Invalid Value")
    #         continue
    #     if cont == "":
    #         # home()
    #         main()
    #         break
    #     elif cont == "n":
    #         break
    #     else:
    #         print("Press enter to repeat\nOR\nPress n to stop: ")
    #         continue

    # cleaning up pins
    # print("Cleaning up pins.")
    print("Closing Program")
    slide.cleanup()
    near_switch.cleanup()
    far_switch.cleanup()