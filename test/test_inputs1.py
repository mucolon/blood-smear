# test_inputs1.py
# This is test code for reading inductive sensor inputs
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_inputs1.py


# importing libraries
from input_io import Input_io # NEVER DELETE
import config
import time


if __name__ == "__main__":
    # initializing  classes
    print("\nInitializing Classes")
    near_switch = Input_io(config.limit_near_pin, "fall") # NEVER DELETE
    far_switch = Input_io(config.limit_far_pin, "fall") # NEVER DELETE

    # initializing pins
    print("Initializing Pins")
    near_switch.init_pin() # NEVER DELETE
    far_switch.init_pin() # NEVER DELETE

    # confirming power
    input("Press any key after motors are connected to power.")

    for x in range(30):
        print("\nNear switch: ", near_switch.read())
        print("Far switch: ", far_switch.read())
        time.sleep(1)

    # cleaning up pins
    print("\nCleaning up pins.")
    near_switch.cleanup() # NEVER DELETE
    far_switch.cleanup() # NEVER DELETE