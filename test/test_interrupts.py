# test_interrupts.py
# This is test code for testing sensor interrupts
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_interrupts.py

'''
    ######## CODE MAY NOT BE FUNCTIONAL ########
'''


# importing libraries
import time
import sys
sys.path.insert(0, "/home/debian/blood-smear/lib")
from digital_io import Digital_Io  # NEVER DELETE
from analog_in import Analog_In  # NEVER DELETE
import config


def test(self):
    # function: print test
    print("\nTest Function!")


if __name__ == "__main__":

    # initializing  classes and pins
    print("\nInitializing Classes & Pins")
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    home_switch.add_event("fall")
    end_switch.add_event("fall")
    force_pwr = Digital_Io(config.force_pins, "out", 0)
    force_sig = Analog_In(config.force_pins)

    # confirming power
    input("Press any key after motors are connected to power")

    for i in range(10, 0, -1):
        print(i, "secs left")
        time.sleep(1)

    # cleaning up pins
    print("\nCleaning up pins")
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
