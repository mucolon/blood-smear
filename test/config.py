# config.py
# This file list all used pins for blood smearing device
# Note: please leave pin labels alone, other files depend on those specific labels


# active output pins for linear guide
# "ena": digital LOW enables pulses to be sent
#        digital HIGH disables pulses
# "dir": digital LOW for ccw rotation
#        digital HIGH for cw rotation
# "pul": digital HIGH then LOW turns motor one step
slide_pins = {"ena": "P8_11", "dir": "P8_15", "pul": "P8_17"}

# active digital input pin for far limit switch
limit_far_pin = {"sig": "P8_12"}

# active digital input pin for near limit switch
limit_near_pin = {"sig": "P8_14"}

# active output pulse pin for unloading servo
unload_pin = {"pul": "P8_13"}