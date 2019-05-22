# basic_smear.py
# This is the test code for a basic smear
#
# run program with this line of code below from home directory (/~)
# sudo python3 blood-smear/test/basic_smear.py


# importing libraries
from stepper import Stepper
from servo import Servo
from digital_io import Digital_Io # NEVER DELETE
from ui import UserI
import time
import config
from math import pi


# declaring constants
slide_circum = 72 # [mm]
slide_step = 1 # micro step configuration
blade_dist = 150 # [mm] ccw
wick_dist = 35 # [mm] cw
wick_time = 3 # [sec]
smear_dist = 45 # [mm] ccw
dry_dist = 60 # [mm] cw
dry_time = 120 # [sec]
force_diameter = 25.4E-3 # [m]
force_area = pi * ((force_diameter / 2) ** 2) # [m^2]


# conversion factors
# radius = 13.3         # [mm] from CAD
# radius = slide_circum / (pi * 2)  # [mm] from manufacturer
# mms2rpm = 30 / (radius * pi)  # [s/(mm*min)]


# function to move slide to linear guide motor
def move2near_side(frequency = 600):
    # frequency: float number to represent the occurence of sensor readings [Hz]
    #            by default 600Hz is selected
    slide.set_direction("cw")
    time_sleep = 1/frequency
    while near_switch.read() != 1:
        # slide.move_steps(1, 90, "cw")
        slide.step()
        time.sleep(time_sleep)
        slide.stop()

# function to move slide to linear guide end
def move2far_side(delay):
    # frequency: float number to represent the occurence of sensor readings [Hz]
    #            by default 600Hz is selected
    slide.set_direction("ccw")
    time_sleep = 1/frequency
    while far_switch.read() != 1:
        # slide.move_steps(1, 90, "ccw")
        slide.step()
        time.sleep(time_sleep)
        slide.stop()

# function to move to smearing blade extension site and extend blade
def blade(distance): # WIP
    # distance: float number of slide linear distance to smearing blade extension site
    slide.move_linear(distance, 90, "ccw")

# function to move to wicking site and wait for wait to finish
def wick(distance, wait_time, manual = "no"):
    # distance: float number of slide linear distance to wicking site [mm]
    # wait_time: float number of time for blood to wick onto smearing blade [sec]
    # manual: "no" allows time to wick to be preselected
    #         "yes" for manual override
    slide.move_linear(distance, 45, "cw")
    if manual == "no":
        time.sleep(wait_time)
    elif manual == "yes":
        input("\nPress any key after blood has wicked")
    else:
        print("\nError: Invalid string for manual")
        print("\"no\" to use preselected wicking wait time")
        print("\"yes\" to manaully proceed after blood has visually wicked")
        print("Please use quotation marks")

# function to move slide for smear
def smear(distance, mms_speed):
    # distance: float number of slide linear distance for smear [mm]
    # mms_speed: float number of motor load's linear velocity [mm/s]
    rpm = slide.convert_mms2rpm(mms_speed)
    slide.move_linear(distance, rpm, "ccw")
    time.sleep(2)

# function to move slide to heater
def dry(distance, wait_time, manual = "no"):
    # distance: float number of slide linear distance after smear to heater [mm]
    # wait_time: float number for time to dry blood slide [sec]
    # manual: "no" allows time to dry to be preselected ie. wait_time, "yes" allows user to
    #         press any key to finish drying process
    slide.move_linear(distance, 90, "cw")
    if manual == "no":
        time.sleep(wait_time)
    elif manual == "yes":
        input("\nPress any key after blood has dried")
    else:
        print("\nError: Invalid string for manual")
        print("\"no\" to use preselected drying wait time")
        print("\"yes\" to manaully proceed after blood has visually dried")
        print("Please use quotation marks")

# function to unload slide
def eject():
    unload.change_angle(95)
    time.sleep(1.5)
    unload.change_angle(0)

# main function for complete smearing process
def main():
    # moving slide to start position
    slide.enable_pulse()
    move2near_side()

    # asking for linear speed
    print("\nPlease enter linear speed of smear")
    input_mms = slide_ui.linear_speed()

    # slide loading interface
    print("\nPlease load slide")
    input("Press any key after slide is loaded")

    # blood dispensing interface
    print("\nPlease dispense blood at target location")
    input("Press any key after blood is dispensed")

    # moving slide to smearing station
    print("\nMoving blood slide to smearing blade")
    slide.enable_pulse()
    # move2far_side()
    blade(blade_dist)

    # blood wicking interface
    print("\nWaiting for blood to wick")
    wick(wick_dist, wick_time, "yes")

    # smearing blood
    print("\nSmearing blood")
    smear(smear_dist, input_mms)
    print("Completed smear")

    # drying blood
    print("\nMoving to drying station")
    print("Drying blood")
    dry(dry_dist, dry_time, "yes")

    # moving slide to unloading site
    print("\nMoving slide to unloading site")
    slide.enable_pulse()
    move2near_side()

    # unloading slide
    print("\nUnloading slide")
    eject()


if __name__ == "__main__":

    # initializing  classes and pins
    slide = Stepper(config.slide_pins, slide_circum, slide_step)
    near_switch = Digital_Io(config.limit_near_pin, "in") # NEVER DELETE
    far_switch = Digital_Io(config.limit_far_pin, "in") # NEVER DELETE
    slide_ui = UserI()
    unload = Servo(config.unload_pin)

    # initializing pins
    unload.start(3, 14)

    # confirming power
    input("Press any key after motors are connected to power")

    # complete smearing process
    main()

    # asking to repeat process
    while True:
        try:
            cont = str(input("Press enter if you're loading another slide\nOR\nPress n to stop: "))
        except ValueError:
            print("Error: Invalid Value")
            continue
        if cont == "":
            main()
            break
        elif cont == "n":
            break
        else:
            continue

    # cleaning up pins
    print("\nClosing Program")
    slide.cleanup()
    near_switch.cleanup() # NEVER DELETE
    far_switch.cleanup() # NEVER DELETE
    unload.cleanup()