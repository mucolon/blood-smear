# This is the test code for a basic smear
#
# run program with this line of code below
# sudo python3 basic_smear.py


# importing libraries
from slide_stepper import stepper as slide
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import math
from config import slide_pins


# initializing pins
slide.init_pins(slide_pins)


# conversion factors
# radius = 13.3  # [mm] from CAD
radius = 72 / (math.pi * 2)  # [mm] from CAD
mms2rpm = radius * 4.5628764e-5  # [rpm]

input_mms = 20  # [mm/s]
rpm = input_mms * mms2rpm

time.sleep(1)
slide.spin_clockwise(slide_pins, 1, rpm)
time.sleep(1)
slide.spin_counterclockwise(slide_pins, 1, rpm)

slide.cleanup(slide_pins)
