# stepper.py
# This file declares a class to use any stepper motor


# importing libraries
import Adafruit_BBIO.GPIO as GPIO
import time
from math import pi


class Stepper:

    abs_max_speed = 500  # [mm/s]
    pulse_per_microstep = 200
    # enable_time = 0.7  # [s]

    # class initialization also initializes motor
    def __init__(self, pins, circumference, microstep=2):
        # pins: dictionary containing used stepper motor pins
        # circumference: float number for distance traveled by one motor
        #                revolution [mm]
        # microstep: int number for current microstep configuration for
        #            stepper motor, by default microstep is 2
        '''
        CRITICAL: As microstep count increases max smooth rotational velocity
                    decreases. ie. 2 microsteps -> 250 mm/s max linear velocity
                    with 72 mm effective motor circumference. The pattern continues
                    4 microsteps -> 150 mm/s max linear velocity
        '''
        self.ena = pins["ena"]
        self.dir = pins["dir"]
        self.pul = pins["pul"]
        self.circum = circumference
        self.radius = self.circum / (pi * 2)
        self.micro = microstep
        self.pulses = microstep * Stepper.pulse_per_microstep
        self.travel_per_pulse = circumference / self.pulses
        self.max_speed = Stepper.abs_max_speed / microstep
        GPIO.setup(self.pul, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.dir, GPIO.OUT)
        GPIO.setup(self.ena, GPIO.OUT, initial=GPIO.HIGH)

    def disable_pulse(self):
        # function: disable motor from sending pulses
        GPIO.output(self.ena, GPIO.HIGH)

    def enable_pulse(self):
        # function: enable motor to send pulses
        GPIO.output(self.ena, GPIO.LOW)

    def step(self):
        # function: step motor
        GPIO.output(self.pul, GPIO.HIGH)

    def stop(self):
        # function: stop stepping motor
        GPIO.output(self.pul, GPIO.LOW)

    def set_direction(self, direction):
        # function: set motor rotation direction
        # direction: string "cw" for clockwise rotation or
        #            string "ccw" for counter-clockwise rotation
        if direction == "cw":
            GPIO.output(self.dir, GPIO.HIGH)
        elif direction == "ccw":
            GPIO.output(self.dir, GPIO.LOW)
        else:
            print(
                "Error: Invalid direction sting [\"cw\" for cw or \"ccw\" for ccw]")
            print("Please include quotation marks")

    def rotate(self, rotations, speed, direction):
        # function: move motor by rotations
        # rotations: float number for motor rotations [rev]
        # speed: float number for stepper load's linear velocity [mm/s]
        # direction: string "cw" for clockwise or
        #            string "ccw" for counter-clockwise
        # self.enable_pulse()
        if speed > self.max_speed:
            speed = self.max_speed
            print("Input speed was too high, it would have caused unstable pulses")
            print("Max safe speed was assigned ", self.max_speed, " mm/s")
        sleep_time = (self.travel_per_pulse / speed) * 0.3366
        steps = round(rotations * self.pulses)
        # time.sleep(Stepper.enable_time)
        if direction == "cw":
            GPIO.output(self.dir, GPIO.HIGH)
            for x in range(steps):
                GPIO.output(self.pul, GPIO.HIGH)
                time.sleep(sleep_time)
                GPIO.output(self.pul, GPIO.LOW)
        elif direction == "ccw":
            GPIO.output(self.dir, GPIO.LOW)
            for x in range(steps):
                GPIO.output(self.pul, GPIO.HIGH)
                time.sleep(sleep_time)
                GPIO.output(self.pul, GPIO.LOW)
        else:
            print(
                "Error: Invalid direction sting [\"cw\" for cw or \"ccw\" for ccw]")
            print("Please include quotation marks")
        # self.disable_pulse()

    def rotate2(self, rotations, delay, direction):
        # function: move motor by rotations and set time delay
        # rotations: float number for motor rotations [rev]
        # delay: float number for motor pulse time delay [ms]
        # direction: string "cw" for clockwise or
        #            string "ccw" for counter-clockwise
        # self.enable_pulse()
        steps = round(rotations * self.pulses)
        # time.sleep(Stepper.enable_time)
        if direction == "cw":
            GPIO.output(self.dir, GPIO.HIGH)
            for x in range(steps):
                GPIO.output(self.pul, GPIO.HIGH)
                time.sleep(delay * 1E-3)
                GPIO.output(self.pul, GPIO.LOW)
        elif direction == "ccw":
            GPIO.output(self.dir, GPIO.LOW)
            for x in range(steps):
                GPIO.output(self.pul, GPIO.HIGH)
                time.sleep(delay * 1E-3)
                GPIO.output(self.pul, GPIO.LOW)
        else:
            print(
                "Error: Invalid direction sting [\"cw\" for cw or \"ccw\" for ccw]")
            print("Please include quotation marks")
        # self.disable_pulse()

    def move_steps(self, numberOfSteps, speed, direction):
        # function: move motor by amount of steps
        # numberOfSteps: int number of steps motor will turn
        # speed: float number for stepper load's linear velocity [mm/s]
        # direction: string "cw" for clockwise or
        #            string "ccw" for counter-clockwise
        if speed > self.max_speed:
            speed = self.max_speed
            print("Input speed was too high, it would have caused unstable pulses")
            print("Max safe speed was assigned ", self.max_speed, " mm/s")
        rotations = numberOfSteps / self.pulses
        self.rotate(rotations, speed, direction)

    def move_linear(self, distance, speed, direction):
        # function: move motor with respect to linear load distance
        # distance: float number of motor's linear distance to travel [mm]
        # speed: float number for stepper load's linear velocity [mm/s]
        # direction: string "cw" for clockwise or
        #            string "ccw" for counter-clockwise
        if speed > self.max_speed:
            speed = self.max_speed
            print("Input speed was too high, it would have caused unstable pulses")
            print("Max safe speed was assigned ", self.max_speed, " mm/s")
        rotations = distance / self.circum
        self.rotate(rotations, speed, direction)

    def cleanup(self):
        # function: cleanup up pins from use
        self.disable_pulse()
        GPIO.cleanup()
