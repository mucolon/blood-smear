# stepper.py
# This file declares a class to use any stepper motor


# importing libraries
import Adafruit_BBIO.GPIO as GPIO
import time
from math import pi


class Stepper:

    def __init__(self, pins, circumference, microstep=1):
        # pins: dictionary containing used stepper motor pins
        # circumference: float number for distance traveled by one motor revolution
        # microstep: int number for current microstep configuration for stepper motor
        #            by default the micro step amount is 1
        self.ena = pins["ena"]
        self.dir = pins["dir"]
        self.pul = pins["pul"]
        self.circum = circumference
        self.radius = self.circum / (pi * 2)
        self.mms2rpm = 30 / (self.radius * pi)
        if microstep == 1:
            self.pulses = 200    # 1 micro step = 200 pulses
        elif microstep == 2:
            self.pulses == 400   # 2 micro steps = 400 pulses
        elif microstep == 4:
            self.pulses = 800    # 4 micro steps = 800 pulses
        elif microstep == 8:
            self.pulses = 1600   # 8 micro steps = 1600 pulses
        elif microstep == 16:
            self.pulses = 3200   # 16 micro steps = 3200 pulses
        elif microstep == 32:
            self.pulses = 6400   # 32 micro steps = 6400 pulses
        else:
            print("Error: Invalid micro step value")
        GPIO.setup(self.pul, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.dir, GPIO.OUT)
        GPIO.setup(self.ena, GPIO.OUT, initial=GPIO.LOW)

    def step(self):
        # function: step motor
        GPIO.output(self.pul, GPIO.HIGH)

    def stop(self):
        # function: stop stepping motor
        GPIO.output(self.pul, GPIO.LOW)

    def set_direction(self, direction):
        # function: set motor rotation direction
        # direction: string "cw" for clockwise rotation
        #            string "ccw" for counter-clockwise rotation
        if direction == "cw":
            GPIO.output(self.pul, GPIO.HIGH)
        elif direction == "ccw":
            GPIO.output(self.dir, GPIO.LOW)
        else:
            print(
                "Error: Invalid direction sting [\"cw\" for cw or \"ccw\" for ccw]")
            print("Please include quotation marks")

    def convert_mms2rpm(self, mms):
        # function: convert linear velocity [mm/s] to rotational velocity [rpm]
        # mms: float number of motor load's linear velocity [mm/s]
        # function return: float number to motor's rotational velocity [rpm]
        return (mms * self.mms2rpm)

    def rotate(self, rotations, rpm, direction):
        # function: move motor by rotations
        # rotations: float number of motor rotations
        # rpm: float number of motor's rpm
        # direction: string "cw" for clockwise or string "ccw" for counter-clockwise
        sleep_time = float(0.3 / rpm)
        steps = round(rotations * self.pulses)
        if direction == "cw":
            GPIO.output(self.dir, GPIO.HIGH)
            for x in range(steps):
                self.step()
                time.sleep(sleep_time)
                GPIO.output(self.pul, GPIO.LOW)
        elif direction == "ccw":
            GPIO.output(self.dir, GPIO.LOW)
            for x in range(steps):
                self.step()
                time.sleep(sleep_time)
                GPIO.output(self.pul, GPIO.LOW)
        else:
            print(
                "Error: Invalid direction sting [\"cw\" for cw or \"ccw\" for ccw]")
            print("Please include quotation marks")

    def move_steps(self, numberOfSteps, rpm, direction):
        # function: move motor by amount of steps
        # numberOfSteps: int number of steps motor will turn
        # rpm: float number of motor's rpm
        # direction: string "cw" for clockwise or string "ccw" for counter-clockwise
        rotations = numberOfSteps / self.pulses
        self.rotate(rotations, rpm, direction)

    def move_linear(self, distance, rpm, direction):
        # function: move motor with respect to linear load distance
        # distance: float number of motor's linear distance to travel [mm]
        # rpm: float number of motor's rpm [rpm]
        # direction: string "cw" for clockwise or string "ccw" for counter-clockwise
        rotations = distance / self.circum
        self.rotate(rotations, rpm, direction)

    def disable_pulse(self):
        # function: disable motor from sending pulses
        GPIO.output(self.ena, GPIO.HIGH)

    def enable_pulse(self):
        # function: enable motor to send pulses
        GPIO.output(self.ena, GPIO.LOW)

    def cleanup(self):
        # function: cleanup up pins from use
        self.disable_pulse()
        GPIO.cleanup()
