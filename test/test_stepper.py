# test_stepper.py
# This is test code for testing a stepper motor
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_stepper.py


# importing libraries
from stepper import Stepper
from digital_io import Digital_Io  # NEVER DELETE
from analog_in import Analog_In  # NEVER DELETE
import config


# declaring constants
stepper_circum = 72  # [mm]
stepper_step = 4  # micro step configuration

def move2home(mms):
    rpm = slide.convert_mms2rpm(mms)
    while home_switch.read() == 1:
        slide.move_steps(1, rpm, "cw")
    return 1

def move2end(mms):
    rpm = slide.convert_mms2rpm(mms)
    while end_switch.read() == 1:
        slide.move_steps(1, rpm, "ccw")
    return 0

def main():
    # function: main test function
    home = 1
    while True:
        try:
            input_mms = str(input(
                "\nEnter linear slide speed [0-200 mm/s] \
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

    main()

    print("\nClosing Program")
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    slide.cleanup()
