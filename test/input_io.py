# input_io.py
# This file declares a class to use GPIO pins as inputs


# importing libraries
import Adafruit_BBIO.GPIO as GPIO
import numpy as np
import time


# declaring Input_io class to handle GPIO inputs
class Input_io():

    # initial class function
    def __init__(self, pin, read_state, resist = "off"):
        # pin: dictionary containing used input pin
        # read_state: edge detection for pin either ("rise", "fall", "both")
        # resist: onboard pin resistor configuration you wish to add
        #   ("pull_up", "pull_down", "off")
        #   "off" is selected by default
        self.sig = pin["sig"]
        if read_state == "rise":
            self.edge = GPIO.RISING
        elif read_state == "fall":
            self.edge = GPIO.FALLING
        elif read_state == "both":
            self.edge = GPIO.BOTH
        else:
            print("\nError: Invalid read_state input (\"rise\", \"fall\", \"both\")")
            print("Please include quotation marks")
        if resist == "pull_up":
            self.resistor = GPIO.PUD_UP
        elif resist == "pull_down":
            self.resistor = GPIO.PUD_DOWN
        elif resist == "off":
            self.resistor = GPIO.PUD_OFF
        else:
            print("\nError: Invalid resist input (\"pull_up\", \"pull_down\", \"off\")")
            print("Please include quotation marks")

    # function to initialize pin
    def init_pin(self, func, freq = 1):
        # function retruns: sig - beaglebone input pin
        #                   edge - pin edge detection
        bouncetime = float(1E3/freq)
        GPIO.setup(self.sig, GPIO.IN, pull_up_down = self.resistor)
        GPIO.add_event_detect(self.pin, self.edge, func, bouncetime)
        return (self.sig, self.edge)

    # function to read input
    def read(self):
        # function returns: int 0 when nothing is detected and int 1 when sensor is triggered
    	return GPIO.input(self.sig)

    # function to detect event
    def event(self):
        # function returns: bool True if edge is detected or bool False otherwise
        return GPIO.event_detected(self.sig)

    # function to wait for event
    def wait(self):
        GPIO.wait_for_edge(self.sig, self.edge)

    # function to remove event detection
    def remove_event(self):
        GPIO.remove_event_detect(self.sig)

    # function to read input accurately
    def read2(self, num_samples, correct_samples, freq):
        # num_samples: int number of samples
        # correct_samples: int number of correct samples
        # freq: float sampling rate in [Hz]
        # function returns: bool True if read input is correct
        #                   bool False if read input is incorrect
        num_samples = int(num_samples)
        correct_samples = int(correct_samples)
        if correct_samples > num_samples:
            print("Error: correct_samples cannot be higher than num_samples")
        samples = np.array([0]*num_samples)
        sleepTime = float(1/freq)
        for i in range(num_samples):
            samples[i] = self.read()
            time.sleep(sleepTime)
        if np.sum(samples) >= correct_samples:
            return True
        else:
            return False

    # function to clean up pin
    def cleanup(self):
        GPIO.remove_event_detect(self.sig)
        GPIO.cleanup()