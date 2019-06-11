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

    def change_duty(self, start, end, changes=200):
        # function: move servo from a start duty cycle to an end duty cycle
        # start: float number for starting duty cycle [duty]
        # end: float number for ending duty cycle [duty]
        # changes: int number for total duty cycle changes
        #           default amount is set to 200, translates to 2 secs total time
        diff = abs(end - start)
        time_sleep = 10 * 1E-3
        duty_change = diff / changes
        i = 0
        if end > start:
            duty = start
            while duty <= end:
                self.update_duty(duty)
                time.sleep(time_sleep)
                duty += duty_change
                if duty > end:
                    if i == 0:
                        duty = end
                        i += 1
        else:
            duty = end
            while duty >= start:
                self.update_duty(duty)
                time.sleep(time_sleep)
                duty -= duty_change
                if duty < start:
                    if i == 0:
                        duty = start
                        i += 1

    def update_angle(self, angle):
        # function: set servo angle
        # angle: float servo angle from (0, max) [degrees]
        duty = angle * self.span / self.range + self.min
        self.update_duty(duty)

    def change_angle(self, start, end, changes=200):
        # function: move servo from a start angle to an end angle
        # start: float number for starting angle position [degrees]
        # changes: int number for total angle changes
        #           default amount is set to 200, translates to 2 secs total time
        diff = abs(end - start)
        time_sleep = 10 * 1E-3
        angle_change = diff / changes
        i = 0
        if end > start:
            angle = start
            while angle <= end:
                self.update_angle(angle)
                time.sleep(time_sleep)
                angle += angle_change
                if angle > end:
                    if i == 0:
                        angle = end
                        i += 1
        else:
            angle = end
            while angle >= start:
                self.update_angle(angle)
                time.sleep(time_sleep)
                angle -= angle_change
                if angle < start:
                    if i == 0:
                        angle = start
                        i += 1

    def disable(self):
        # function: disable servo motor
        PWM.stop(self.pul)

    def cleanup(self):
        # function: cleanup servo PWM pin
        PWM.stop(self.pul)
        PWM.cleanup()
