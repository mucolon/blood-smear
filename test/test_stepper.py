# test_stepper.py
# This is test code for testing a stepper motor
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_stepper.py


# importing libraries
import sys
sys.path.insert(0, "/home/debian/blood-smear/lib")
from stepper import Stepper
from digital_io import Digital_Io  # NEVER DELETE
from analog_in import Analog_In  # NEVER DELETE
import config


# declaring constants
stepper_circum = 72  # [mm]
stepper_step = 32  # micro step configuration


def move2home(mms):
    # function: moves slide to home position
    # function return: int 1 to identify slide at home position
    rpm = slide.convert_mms2rpm(mms)
    while home_switch.read() == 1:
        slide.move_steps(1, rpm, "cw")
    return 1


def move2end(mms):
    # function: moves slide to end position
    # function return: int 0 to identify slide at end position
    rpm = slide.convert_mms2rpm(mms)
    while end_switch.read() == 1:
        slide.move_steps(1, rpm, "ccw")
    return 0


def side2side():
    # function: moves slide side to side
    home = 1
    while True:
        try:
            input_mms = str(input(
                "\nEnter linear slide speed [0-1000 mm/s] \
                \n OR n to exit: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if input_mms == "n":
            break
        elif home == 1:
            mms = float(input_mms)
            home = move2end(mms)
            continue
        elif home == 0:
            mms = float(input_mms)
            home = move2home(mms)
            continue
        elif float(input_mms) < 0:
            print("Error: Input speed cannot be negative")
            continue
        elif float(input_mms) > 1000:
            print("Error: Input speed cannot be greater than 1000 mm/s")
            continue


def rotate():
    # function: moves slide one complete rotation at a time
    while True:
        try:
            response = str(input(
                "\nPress [ENTER] to move 1 revolution towards the end or [b] to move 1 revolution towards home or [n] to exit: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if response == "n":
            break
        elif response == "":
            slide.rotate(1, 100, "cw")
            continue
        elif response == "b":
            slide.rotate(1, 100, "ccw")
            continue
        else:
            print("Error: Try again")
            continue


if __name__ == "__main__":

    # initializing  classes
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    slide = Stepper(config.slide_pins, stepper_circum, stepper_step)
    force_pwr = Digital_Io(config.force_pins, "out", 0)  # NEVER DELETE
    force_sig = Analog_In(config.force_pins)  # NEVER DELETE

    # confirming power
    input("Press any key after motors are connected to power")

    move2home(100)

    while True:
        try:
            response = str(
                input("\nEnter test name [s=side2side, r=rotation]: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if response == "s":
            side2side()
            break
        elif response == "r":
            rotate()
            break
        else:
            print("Error: Try again")
            continue

    print("\nClosing Program")
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    slide.cleanup()
