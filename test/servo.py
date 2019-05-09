# servo.py
# This file declares a class to use any servo motor


# importing libraries
import Adafruit_BBIO.PWM as PWM
import time


# declaring Servo class to handle actuating a servo motor
class Servo:

    # initial class function
    def __init__(self, pin):
        # pin: dictionary containing used servo PWM pin
        self.pul = pin["pul"]

    # function to start servo
    def start(self, duty_min, duty_max, freq = 50, polarity = 0):
        # duty_min: int PWM duty cycle for -90 degrees
        # duty_max: int PWM duty cycle for +90 degrees
        # freq: int PWM frequency in [Hz], must be > 0
        #   50 Hz by default
        # polarity: int defines whether the duty affects the PWM waveform
        #   0 by default (rising edge), 1 (falling edge)
        self.min = int(duty_min)
        self.max = int(duty_max)
        self.span = duty_max - duty_min
        duty = self.span / 2 + self.min
        PWM.start(self.pul, duty, freq, polarity)

    # function to change servo duty cycle
    def change_duty(self, duty):
        # duty: int PWM duty cycle from 0-100
        PWM.set_duty_cycle(self.pul, duty)

    # function to set servo angle
    def change_angle(self, angle):
        # angle: float servo angle from (-90,90) degrees
        duty = (angle + 90) * self.span / 180 + self.min
        self.change_duty(duty)

    # function to disable servo motor
    def disable(self):
        PWM.stop(self.pul)

    # function to cleanup servo PWM pin
    def cleanup(self):
        PWM.stop(self.pul)
        PWM.cleanup()