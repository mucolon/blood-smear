# This file declares a class to use any stepper motor


# importing libraries
import Adafruit_BBIO.GPIO as GPIO
import time
import math


# declaring Stepper class to handle a stepper motor
class Stepper:

    # intitial class function
    def __init__(self, pins):
        self.ena = pins["ena"]
        self.dir = pins["dir"]
        self.pul = pins["pul"]

    # function to initialize pins
    def init_pins(self):
        GPIO.setup(self.pul, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.dir, GPIO.OUT)
        GPIO.setup(self.ena, GPIO.OUT, initial = GPIO.LOW)
        # GPIO.output(self.pul, GPIO.LOW)
        # GPIO.output(self.ena, GPIO.LOW)

    # function to step motor
    def step(self):
        GPIO.output(self.pul, GPIO.HIGH)

    # function to set stepper motor micro steps
    def micro_steps(self, microStep = 1):
        # microStep: the amount of microsteps the stepper motor is set to
        #   by default the micro step amount is 1
        if microStep == 1:
            self.pulses = 200    # 1 micro step = 200 pulses
        elif microStep == 32:
            self.pulses = 6400   # 32 micro steps = 6400 pulses
        elif microStep == 2:
            self.pulses == 400   # 2 micro steps = 400 pulses
        elif microStep == 4:
            self.pulses = 800    # 4 micro steps = 800 pulses
        elif microStep == 8:
            self.pulses = 1600   # 8 micro steps = 1600 pulses
        elif microStep == 16:
            self.pulses = 3200   # 16 micro steps = 3200 pulses
        else:
            print("Error: Invalid micro step value")

    # fucntion to move motor by rotations
    def rotate(self, rotations, rpm, dir):
        # rotations: float number to rotate motor
        # rpm: float number to describe motor's rpm
        # dir: 1 is for clockwise and 0 is for counterclockwise
        sleep_time = float(0.3 / rpm)
        steps = int(rotations * self.pulses)
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
            print("Error: Invalid dir value [1 for cw or 0 for ccw]")

    def move_steps(self, numberOfSteps, rpm, dir):
        # numberOfSteps: int number of amount of steps motor will turn
        # rpm: float number to describe motor's rpm
        # dir: 1 is for clockwise and 0 is for counterclockwise
        sleep_time = float(0.3 / rpm)
        if dir == 1:
            GPIO.output(self.dir, GPIO.HIGH)
            for x in range(0, numberOfSteps):
                self.step()
                time.sleep(sleep_time)
                GPIO.output(self.pul, GPIO.LOW)
        elif dir == 0:
            GPIO.output(self.dir, GPIO.LOW)
            for x in range(0, numberOfSteps):
                self.step()
                time.sleep(sleep_time)
                GPIO.output(self.pul, GPIO.LOW)
        else:
            print("Error: Invalid dir value [1 for cw or 0 for ccw]")

    # function to disable motor from sending pulses
    def disable(self):
        GPIO.output(self.ena, GPIO.HIGH)

    # function to cleanup up pins from use
    def cleanup(self):
        GPIO.cleanup(self.ena)
        GPIO.cleanup(self.dir)
        GPIO.cleanup(self.pul)
        self.disable()