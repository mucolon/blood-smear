# test_stepper_raw.py
# This is test code for testing a stepper motor using Adafruit_BBIO library
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_stepper_raw.py


# importing libraries
import sys
import Adafruit_BBIO.GPIO as GPIO
import time
sys.path.insert(0, "/home/debian/blood-smear/lib")
import config
from digital_io import Digital_Io  # NEVER DELETE
from analog_in import Analog_In  # NEVER DELETE


# declaring constants
stepper_circum = 72.087  # [mm]
stepper_step = 4  # micro step configuration
defualt_speed_mms = 200  # [mms]
defualt_speed_rpm = 190  # [rpm]


def
