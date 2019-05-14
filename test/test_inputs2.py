# test_inputs2.py
# This is test code for testing sensor interrupts
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_inputs2.py


# importing libraries
from input_io import Input_io
import config
import time


# test function
def test():
    print("\nTest Function!")


if __name__ == "__main__":
    # initializing  classes
    print("\nInitializing Classes")
    near_switch = Input_io(config.limit_near_pin, "fall")
    far_switch = Input_io(config.limit_far_pin, "fall")

    # initializing pins
    print("Initializing Pins")
    near_switch.init_pin(test())
    far_switch.init_pin(test())

    # confirming power
    input("Press any key after motors are connected to power.")

    time.sleep(30)

    # near_switch.event()
    # far_switch.event()

    # cleaning up pins
    print("\nCleaning up pins.")
    near_switch.cleanup()
    far_switch.cleanup()