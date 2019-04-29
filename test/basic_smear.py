# This is the test code for a basic smear
#
# run program with this line of code below
# sudo python3 basic_smear.py


# importing libraries
from slide_stepper import Stepper
# import Adafruit_BBIO.GPIO as GPIO
# import Adafruit_BBIO.PWM as PWM
import time
import math
import config


# declaring constants
cw = 1  # clockwise
ccw = 0 # counterclockwise


# initializing stepper classes
print("Initializing Classes")
slide = Stepper(config.slide_pins)


# initializing pins
print("Initializing Pins")
slide.init_pins()


# conversion factors
# radius = 13.3  # [mm] from CAD
radius = 72 / (math.pi * 2)  # [mm] from CAD
mms2rpm = radius * 4.5628764e-5  # [rpm]

input_mms = 10  # [mm/s]
# rpm = input_mms * mms2rpm
rpm = 10

for x in range(1):
    # time.sleep(1)
    # print("Spining Clockwise")
    # slide.spin(2, rpm, cw)

    # time.sleep(1)
    print("Spining CounterClockwise")
    slide.spin(1, rpm, ccw)

    print("Completed", x+1, "Cycles")

print("Cleaning up pins")
slide.cleanup()
