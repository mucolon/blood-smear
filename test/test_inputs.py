# test_inputs.py
# This is test code for reading inputs from test code
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_inputs.py


# importing libraries
from input_io import Input_io
import Adafruit_BBIO.GPIO as GPIO
import config
import time


# def test():
#     print("\nTest function")


# reading inputs
# for x in range(30):
#     print("Near switch: ", near_switch.read())
#     # print("Near switch: ", near_switch.read(), "\n")
#     # print("Far switch: ", far_switch.read())
#     print("Far switch: ", far_switch.read(), "\n")
#     # print("Near switch: ", GPIO.input(config.limit_near_pin["sig"]))
#     # print("Far switch: ", GPIO.input(config.limit_far_pin["sig"]), "\n")
#     time.sleep(1)


if __name__ == "__main__":
    # initializing  classes
    print("\nInitializing Classes")
    near_switch = Input_io(config.limit_near_pin, "fall")
    far_switch = Input_io(config.limit_far_pin, "fall")

    # initializing pins
    print("Initializing Pins")
    near_info = near_switch.init_pin()
    far_info = far_switch.init_pin()
    near_pin = near_info[0]
    far_pin = far_info[0]
    near_edge = near_info[1]
    far_edge = far_info[1]

    # GPIO.add_event_detect(near_pin, near_edge)

    # confirming power
    input("Press any key after motors are connected to power.")

    # while GPIO.event_detected(near_pin) == True:
    #     print("False")
    # print("Event Detected!")

    # time.sleep(10)

    # testing interrupts
    # read_value = 1
    # while read_value != 0:
    #     read_value = near_switch.read()
    # print("\nTest 1")

    for x in range(30):
        print("\nNear switch: ", near_switch.read())
        print("Far switch: ", far_switch.read())
        time.sleep(1)

    # cleaning up pins
    print("\nCleaning up pins.")
    # near_switch.remove_event()
    # far_switch.remove_event()
    near_switch.cleanup()
    far_switch.cleanup()