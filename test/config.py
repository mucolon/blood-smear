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

# active digital input pin for home (opposite side of stepper motor) limit switch
limit_home_pin = {"sig": "P9_11"}

# active digital input pin for end (same side as stepper motor) limit switch
limit_end_pin = {"sig": "P9_12"}

# active output pulse pin for unloading servo
unload_pin = {"pul": "P8_13"}  # 5V or 6V

# active digital output pin for activating drying fan
fan_pin = {"sig": "P8_16"}

# active output pulse pin for blade ejection linear servo
linear_pin = {"pul": "P8_19"}  # 6V

# active output pulse pin for blade ejection pulley servo
pulley_pin = {"pul": "P9_16"}  # 6V

# active output pulse pin for blade ejection rotation servo
rotation_pin = {"pul": "P9_14"}  # 6V
