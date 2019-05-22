# digital_io.py
# This file declares a class to use digital GPIO pins as inputs/outputs


# importing libraries
import Adafruit_BBIO.GPIO as GPIO
import numpy as np
import time


# declaring Digital_Io class to handle GPIO inputs/outputs
class Digital_Io:

    # initial class function and pin start initialization
    def __init__(self, pin, direction):
        # pin: dictionary containing used input/output pin
        # direction: string "in" to set up pin as an input or
        #            string "out" to set up pin as an output
        self.sig = pin["sig"]
        if direction == "in":
            self.dir = GPIO.IN
        elif direction == "out":
            self.dir = GPIO.OUT
        else:
            print("\nError: Invalid string direction input (\"in\" or \"out\")
            print("\"in\" for input pin or \"out\" for output pin")
            print("Please include quotation marks")
        GPIO.setup(self.sig, self.dir)

    # function to read input
    def read(self):
        # function returns: int 0 when nothing is detected and int 1 when sensor is triggered
    	return GPIO.input(self.sig)

    # function to add event detection
    def add_event(self, edge):
        # edge: string "rise" to detect rising edge
        #       string "fall" to detect falling edge
        #       string "both" to detect both edges
        if edge == "rise":
            self.edge = GPIO.RISING
            GPIO.add_event_detection(self.sig, self.edge)
        elif edge == "fall":
            self.edge = GPIO.FALLING
            GPIO.add_event_detection(self.sig, self.edge)
        elif edge == "both":
            self.edge = GPIO.BOTH
            GPIO.add_event_detection(self.sig, self.edge)
        else:
            print("Error: Invalid string edge input")
            print("\"rise\" for rising edge")
            print("\"fall\" for falling edge")
            print("\"both\" for both edges")
            print("Please add quotation marks)

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
    def read2(self, num_samples, correct_samples, frequency):
        # num_samples: int number of samples
        # correct_samples: int number of correct samples
        # frequency: float sampling rate in [Hz]
        # function returns: bool True if read input is correct
        #                   bool False if read input is incorrect
        num_samples = int(num_samples)
        correct_samples = int(correct_samples)
        if correct_samples > num_samples:
            print("Error: correct_samples cannot be higher than num_samples")
        samples = np.array([0]*num_samples)
        sleepTime = float(1/frequency)
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