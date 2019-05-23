# test_interrupts.py
# This is test code for testing sensor interrupts
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_interrupts.py


# importing libraries
from digital_io import Digital_Io  # NEVER DELETE
import config
import time


def test(self):
    # function: print test
    print("\nTest Function!")


if __name__ == "__main__":

    # initializing  classes and pins
    print("\nInitializing Classes & Pins")
    near_switch = Digital_Io(config.limit_near_pin, "in")  # NEVER DELETE
    far_switch = Digital_Io(config.limit_far_pin, "in")  # NEVER DELETE
    near_switch.add_event("fall")
    far_switch.add_event("fall")

    # confirming power
    input("Press any key after motors are connected to power")

    for i in range(10, 0, -1):
        print(i, "secs left")
        time.sleep(1)

    # cleaning up pins
    print("\nCleaning up pins")
    near_switch.cleanup()  # NEVER DELETE
    far_switch.cleanup()  # NEVER DELETE