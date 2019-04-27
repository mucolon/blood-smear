# This file declares a class to use the linear guide's stepper motor


# enter stepper.'rotation'(pinarray, degrees, rpm)
# 1.8 per step


# importing libraries
import Adafruit_BBIO.GPIO as GPIO
import time
import math
from config import slide_pins


# function to step motor forward
def step_forward(slide_pins, pin_index):
    GPIO.output(slide_pins["pul"], GPIO.LOW)


# function to step motor backward
def step_backward(slide_pins, pin_index):
    GPIO.output(slide_pins["pul"], GPIO.LOW)


# declaring stepper class with functions
class stepper(object):

# function to initialize pins
    def init_pins(self, slide_pins):
        GPIO.setup(slide_pins["pul"], GPIO.OUT)
        GPIO.setup(slide_pins["dir"], GPIO.OUT)
        GPIO.setup(slide_pins["ena"], GPIO.OUT)
        GPIO.output(slide_pins["pul"], GPIO.HIGH)
        GPIO.output(slide_pins["ena"], GPIO.LOW)

# fucntion to move motor clockwise
    def spin_clockwise(self, slide_pins, rotations, rpm):
        sleep_time = 0.3 / float(rpm)
        steps_forward = rotations * 200  # 1 micro step = 200 pulses
        # steps_forward = rotations * 6400 # 32 micro steps = 6400 pulses
        GPIO.output(slide_pins["dir"], GPIO.HIGH)
        for x in range(0, steps_forward):
            step_forward(self, slide_pins)
            time.sleep(sleep_time)
            GPIO.output(slide_pins["pul"], GPIO.HIGH)

# fucntion to move motor counterclockwise
    def spin_counterclockwise(self, slide_pins, rotations, rpm):
        sleep_time = 0.3 / float(rpm)
        steps_backward = rotations * 200  # 1 micro step = 200 pulses
        # steps_background = rotations * 6400 # 32 micro steps = 6400 pulses
        GPIO.output(slide_pins["dir"], GPIO.LOW)
        for x in range(0, steps_backward):
            step_backward(self, slide_pins)
            time.sleep(sleep_time)
            GPIO.output(slide_pins["pul"], GPIO.HIGH)

# function to cleanup up pins from use
    def cleanup(self, slide_pins):
        GPIO.cleanup()

# function to disable motor from sending pulses
    def disable(self, slide_pins):
        GPIO.output(slide_pins["ena"], GPIO.HIGH)
        GPIO.output(slide_pins["pul"], GPIO.LOW)
