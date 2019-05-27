# test_indutive.py
# This is test code for reading inductive sensor inputs
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_inductive.py


# importing libraries
from digital_io import Digital_Io  # NEVER DELETE
from stepper import Stepper
import config
import time


if __name__ == "__main__":

    # initializing  classes and pins
    print("\nInitializing Classes & Pins")
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    slide = Stepper(config.slide_pins, 72, 1)

    # confirming power
    input("Press any key after motors are connected to power.")

    for x in range(30):
        print("\nHome switch: ", home_switch.read())
        print("End switch: ", end_switch.read())
        time.sleep(1)

    # cleaning up pins
    print("\nCleaning up pins.")
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    slide.cleanup()
