# This is the test code for a basic smear
#
# run program with this line of code below
# sudo python3 basic_smear.py


# importing libraries
from slide_stepper import Slide
# import Adafruit_BBIO.GPIO as GPIO
# import Adafruit_BBIO.PWM as PWM
import time
import math
import config


# initializing stepper classes
print("Initializing Classes")
slide = Slide()


# initializing pins
print("Initializing Pins")
slide.init_pins(config.slide_pins)


# conversion factors
# radius = 13.3  # [mm] from CAD
radius = 72 / (math.pi * 2)  # [mm] from CAD
mms2rpm = radius * 4.5628764e-5  # [rpm]

input_mms = 50  # [mm/s]
rpm = input_mms * mms2rpm

time.sleep(1)
print("Spining Clockwise")
slide.spin_clockwise(config.slide_pins, 2, rpm)
time.sleep(1)
print("Spining CounterClockwise")
slide.spin_counterclockwise(config.slide_pins, 2, rpm)

print("Cleaning up pins")
slide.cleanup(config.slide_pins)
