# This is test code for reading inputs from test code
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_inputs.py


# importing libraries
from input_io import Input_io
import Adafruit_BBIO.GPIO as GPIO
import config
import time

def test():
    print("\nTest function")

# initializing  classes
print("Initializing Classes")
near_switch = Input_io(config.limit_near_pin, "fall")
far_switch = Input_io(config.limit_far_pin, "fall")

# initializing pins
print("Initializing Pins")
near_switch.init_pin(test())
far_switch.init_pin(test())

# confirming power
input("Press any key after motors are connected to power.")

# reading inputs
# for x in range(30):
#     print("Near switch: ", near_switch.read())
#     # print("Near switch: ", near_switch.read(), "\n")
#     # print("Far switch: ", far_switch.read())
#     print("Far switch: ", far_switch.read(), "\n")
#     # print("Near switch: ", GPIO.input(config.limit_near_pin["sig"]))
#     # print("Far switch: ", GPIO.input(config.limit_far_pin["sig"]), "\n")
#     time.sleep(1)

# testing interrupts
read_value = 0
    while read_value != 1:
        read_value = near_switch.read()
    print("Test 1")



# cleaning up pins
print("Cleaning up pins.")
near_switch.remove_event()
far_switch.remove_event()
near_switch.cleanup()
far_switch.cleanup()