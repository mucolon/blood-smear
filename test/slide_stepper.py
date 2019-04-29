# This file declares a class to use the linear guide's stepper motor


# enter stepper.'rotation'(pinarray, degrees, rpm)
# 1.8 per step


# importing libraries
import Adafruit_BBIO.GPIO as GPIO
import time
# import math
# import config


# function to step motor forward
def step_forward(pins):
    GPIO.output(pins["pul"], GPIO.HIGH)


# function to step motor backward
def step_backward(pins):
    GPIO.output(pins["pul"], GPIO.HIGH)


# declaring stepper class with functions
class Slide(object):

    # function to initialize pins
    def init_pins(self, pins):
        GPIO.setup(pins["pul"], GPIO.OUT)
        GPIO.setup(pins["dir"], GPIO.OUT)
        GPIO.setup(pins["ena"], GPIO.OUT)
        GPIO.output(pins["pul"], GPIO.LOW)
        GPIO.output(pins["ena"], GPIO.LOW)

    # fucntion to move motor clockwise
    def spin_clockwise(self, pins, rotations, rpm):
        sleep_time = 0.3 / float(rpm)
        steps = rotations * 200  # 1 micro step = 200 pulses
        # steps = rotations * 6400 # 32 micro steps = 6400 pulses
        GPIO.output(pins["dir"], GPIO.HIGH)
        for x in range(0, steps):
            step_forward(self, pins)
            time.sleep(sleep_time)
            GPIO.output(pins["pul"], GPIO.LOW)

    # fucntion to move motor counterclockwise
    def spin_counterclockwise(self, pins, rotations, rpm):
        sleep_time = 0.3 / float(rpm)
        steps = rotations * 200  # 1 micro step = 200 pulses
        # steps = rotations * 6400 # 32 micro steps = 6400 pulses
        GPIO.output(pins["dir"], GPIO.LOW)
        for x in range(0, steps):
            step_backward(self, pins)
            time.sleep(sleep_time)
            GPIO.output(pins["pul"], GPIO.LOW)

    # function to cleanup up pins from use
    def cleanup(self, pins):
        GPIO.cleanup()

    # function to disable motor from sending pulses
    def disable(self, pins):
        GPIO.output(pins["ena"], GPIO.HIGH)
        GPIO.output(pins["pul"], GPIO.LOW)
