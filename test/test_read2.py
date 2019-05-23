# test_read2.py
# This is test code for testing read2 function
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_read2.py


# importing libraries
from digital_io import Digital_Io  # NEVER DELETE
import config


if __name__ == "__main__":

    # initializing  classes and pins
    print("\nInitializing Classes & Pins")
    near_switch = Digital_Io(config.limit_near_pin, "in")  # NEVER DELETE
    far_switch = Digital_Io(config.limit_far_pin, "in")  # NEVER DELETE

    # confirming power
    input("Press any key after motors are connected to power.")

    while near_switch.read2(10, 9, 100) is not False:
        print("False")
    print("\nTrue")

    # cleaning up pins
    print("\nCleaning up pins.")
    near_switch.cleanup()  # NEVER DELETE
    far_switch.cleanup()  # NEVER DELETE
