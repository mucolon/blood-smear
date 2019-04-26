# This is the test code for a basic smear
#
# run program with this line of code below
# sudo python basic_smear.py

# importing libraries
from slide_stepper import stepper as slide
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import math

# configuring pins
slide.init_pins(config.slide_pins)

# conversion factors
# radius = NUMBER # [mm]
# mms2rpm = radius*4.5628764e-5 # [rpm]
