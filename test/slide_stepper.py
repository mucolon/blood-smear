# This file declares a class to use the linear guide's stepper motor


# enter stepper.'rotation'(pinarray, degrees, rpm)
# 1.8 per step


# importing libraries
import Adafruit_BBIO.GPIO as GPIO
import time
import math
import config


# function to step motor forward
def step_forward(pins, pin_index):
    GPIO.output(config.slide_pins["pul"], GPIO.LOW)


# function to step motor backward
def step_backward(pins, pin_index):
    GPIO.output(config.slide_pins["pul"], GPIO.LOW)


# declaring stepper class with functions
class stepper(object):

    # function to initialize pins
    def init_pins(self, pins):
        GPIO.setup(config.slide_pins["pul"], GPIO.OUT)
        GPIO.setup(config.slide_pins["dir"], GPIO.OUT)
        GPIO.setup(config.slide_pins["ena"], GPIO.OUT)
        GPIO.output(config.slide_pins["pul"], GPIO.HIGH)
        GPIO.output(config.slide_pins["ena"], GPIO.LOW)

# fucntion to move motor clockwise
    def spin_clockwise(self, pins, rotations, rpm):
        sleep_time = 0.3 / float(rpm)
        steps_forward = rotations * 200  # 1 micro step = 200 pulses
        # steps_forward = rotations * 6400 # 32 micro steps = 6400 pulses
        GPIO.output(config.slide_pins["dir"], GPIO.HIGH)
        for x in range(0, steps_forward):
            step_forward(self, pins)
            time.sleep(sleep_time)
            GPIO.output(config.slide_pins["pul"], GPIO.HIGH)

# fucntion to move motor counterclockwise
    def spin_counterclockwise(self, pins, rotations, rpm):
        sleep_time = .3 / float(rpm)
        steps_backward = rotations * 200  # 1 micro step = 200 pulses
        # steps_background = rotations * 6400 # 32 micro steps = 6400 pulses
        GPIO.output(config.slide_pins["dir"], GPIO.LOW)
        for x in range(0, steps_backward):
            step_backward(self, pins)
            time.sleep(sleep_time)
            GPIO.output(config.slide_pins["pul"], GPIO.HIGH)

# function to cleanup up pins from use
    def cleanup(self, pins):
        GPIO.cleanup()
