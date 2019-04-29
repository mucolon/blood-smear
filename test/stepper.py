# This file declares a class to use any stepper motor


# importing libraries
import Adafruit_BBIO.GPIO as GPIO
import time
import math


# declaring Stepper class with functions
class Stepper:

    # intitial class function
    def __init__(self, pins):
        self.ena = pins["ena"]
        self.dir = pins["dir"]
        self.pul = pins["pul"]

    # function to initialize pins
    def init_pins(self):
        GPIO.setup(self.pul, GPIO.OUT)
        GPIO.setup(self.dir, GPIO.OUT)
        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.output(self.pul, GPIO.LOW)
        GPIO.output(self.ena, GPIO.LOW)

    # function to step motor
    def step(self):
        GPIO.output(self.pul, GPIO.HIGH)

    # fucntion to move motor
    def spin(self, rotations, rpm, dir):
        # rotations: can be any float number to rotate the motor
        # rpm: can be any float number to describe the rpm of the motor
        # dir: 1 is for clockwise and 0 is for counterclockwise
        sleep_time = float(0.3 / rpm)
        steps = int(rotations * 200)  # 1 micro step = 200 pulses
        # steps = int(rotations * 6400) # 32 micro steps = 6400 pulses
        if dir == 1:
            GPIO.output(self.dir, GPIO.HIGH)
            for x in range(0, steps):
                self.step()
                time.sleep(sleep_time)
                GPIO.output(self.pul, GPIO.LOW)
        elif dir == 0:
            GPIO.output(self.dir, GPIO.LOW)
            for x in range(0, steps):
                self.step()
                time.sleep(sleep_time)
                GPIO.output(self.pul, GPIO.LOW)
        else:
            print("Error: Invalid dir value. 1 for cw or 0 for ccw")

    # function to disable motor from sending pulses
    def disable(self):
        GPIO.output(self.ena, GPIO.HIGH)

    # function to cleanup up pins from use
    def cleanup(self):
        GPIO.cleanup(self.ena)
        GPIO.cleanup(self.dir)
        GPIO.cleanup(self.pul)
        self.disable()


# enter stepper.'rotation'(pinarray, degrees, rpm)
# 1.8 per step
