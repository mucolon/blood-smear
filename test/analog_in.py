# analog_in.py
# This file declares a class to use analog GPIO pins as inputs


# importing libraries
import Adafruit_BBIO.ADC as ADC


# declaring Analog_In class to handle analog inputs
class Analog_In:

    # initial class function and pin start initialization
    def __init__(self, pin):
        # pin: dictionary containing used input pin
        self.sig = pin["sig"]
        ADC.setup_adc()

    # function to read normalized analog value
    def read(self):
        # function returns: float number from 0.0 to 1.0
        return ADC.setup_read(self.sig)

    # function to read raw analog value
    def read_raw(self):
        # function returns: float number from 0.0 to 4095.0
        return ADC.setup_read_raw(self.sig)