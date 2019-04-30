# This file declares a class to use GPIO pins as inputs


# importing libraries
import Adafruit_BBIO.GPIO as GPIO


# declaring Input_io class to handle GPIO inputs
class Input_io():

    # intitial class function
    def __init__(self, pin):
        self.sig = pin["sig"]

    # function to initialize pin
    def init_pin(self):
        GPIO.setup(self.sig, GPIO.IN)

    # function to
