# analog_in.py
# This file declares a class to use analog GPIO pins as inputs


# importing libraries
import Adafruit_BBIO.ADC as ADC


class Analog_In:

    def __init__(self, pin):
        # pin: dictionary containing used input pin
        self.sig = pin["sig"]
        ADC.setup_adc()

    def read(self):
        # function: read normalized analog value
        # function returns: float number from 0.0 to 1.0
        return ADC.setup_read(self.sig)

    def read_raw(self):
        # function: read raw analog value
        # function returns: float number from 0.0 to 4095.0
        return ADC.setup_read_raw(self.sig)
