# test_indutive.py
# This is test code for reading inductive sensor inputs
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_inductive.py


# importing libraries
from digital_io import Digital_Io  # NEVER DELETE
import config
import time


if __name__ == "__main__":

    # initializing  classes and pins
    print("\nInitializing Classes & Pins")
    near_switch = Digital_Io(config.limit_near_pin, "in")  # NEVER DELETE
    far_switch = Digital_Io(config.limit_far_pin, "in")  # NEVER DELETE

    # confirming power
    input("Press any key after motors are connected to power.")

    for x in range(30):
        print("\nNear switch: ", near_switch.read())
        print("Far switch: ", far_switch.read())
        time.sleep(1)

    # cleaning up pins
    print("\nCleaning up pins.")
    near_switch.cleanup()  # NEVER DELETE
    far_switch.cleanup()  # NEVER DELETE
