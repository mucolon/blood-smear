# servo.py
# This file declares a class to use any servo motor


# importing libraries
import Adafruit_BBIO.PWM as PWM
import time


class Servo:

    def __init__(self, pin, angle_range=180):
        # pin: dictionary containing used servo PWM pin
        # angle_range: float number describing the max angle range of a servo
        #              motor [degrees], by default 180 degrees
        self.pul = pin["pul"]
        self.range = angle_range

    def start(self, duty_min, duty_max, frequency=50, polarity=0):
        # function: start/initialize servo
        # duty_min: float PWM duty cycle for 0 [degrees]
        # duty_max: float PWM duty cycle for angle range [degrees]
        # frequency: float PWM frequency [Hz], must be > 0, by default 50Hz
        # polarity: int defines whether the duty affects the PWM waveform
        #           by default 0 (rising edge), 1 (falling edge)
        self.min = float(duty_min)
        self.max = float(duty_max)
        self.span = duty_max - duty_min
        duty = self.min
        PWM.start(self.pul, duty, frequency, polarity)

    def update_duty(self, duty):
        # function: change servo duty cycle
        # duty: float PWM duty cycle from 0-100
        PWM.set_duty_cycle(self.pul, duty)

    def update_angle(self, angle):
        # function: set servo angle
        # angle: float servo angle from (0, max) [degrees]
        duty = angle * self.span / self.range + self.min
        self.update_duty(duty)

    def change_angle(self, start, end, frequency=100):
        # function: move servo from a start angle to an end angle
        # start: float number for starting angle position [degrees]
        # end: float number for ending angle position [degrees]
        # frequency: float number rate of angle change [Hz], by default 100Hz
        time_sleep = 1 / frequency
        angle = start
        if end > start:
            while angle <= end:
                self.update_angle(angle)
                time.sleep(time_sleep)
                angle += 1
        else:
            while angle <= end:
                self.update_angle(angle)
                time.sleep(time_sleep)
                angle -= 1

    def disable(self):
        # function: disable servo motor
        PWM.stop(self.pul)

    def cleanup(self):
        # function: cleanup servo PWM pin
        PWM.stop(self.pul)
        PWM.cleanup()
