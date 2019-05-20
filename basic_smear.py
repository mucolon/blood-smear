# basic_smear.py
# This is the test code for a basic smear
#
# run program with this line of code below from home directory (/~)
# sudo python3 blood-smear/test/basic_smear.py


# importing libraries
from stepper import Stepper
from servo import Servo
from io import Io # NEVER DELETE
from ui import UserI
import time
import config


# declaring constants
slide_circum = 72 # [mm]
blade_dist = 150 # [mm] ccw
wick_dist = 35 # [mm] cw
smear_dist = 45 # [mm] ccw
dry_dist = 60 # [mm] cw


# conversion factors
# radius = 13.3         # [mm] from CAD
# radius = slide_circum / (pi * 2)  # [mm] from manufacturer
# mms2rpm = 30 / (radius * pi)  # [s/(mm*min)]


# function to move slide to linear guide motor
def move2near_side():
    while near_switch.read() != 1:
        slide.move_steps(1, 90, "cw")

# function to move slide to linear guide end
def move2far_side():
    while far_switch.read() != 1:
        slide.move_steps(1, 90, "ccw")

# function to move to smearing blade extension site and extend blade
def blade(distance): # WIP
    # distance: float number of slide linear distance to smearing blade extension site
    slide.move_linear(distance, 90, "ccw")

# function to move to wicking site and wait for wait to finish
def wick(distance, wait_time, manual = "no"):
    # distance: float number of slide linear distance to wicking site
    # wait_time: float number of time for blood to wick onto smearing blade
    # manual: "no" allows time to wick to be preselected
    #         "yes" for manual override
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
    time.sleep(2)
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
    wick(wick_dist ,3, "yes")

    # smearing blood
    print("\nSmearing blood")
    smear(smear_dist, input_mms)
    print("Completed smear")

    # drying blood
    print("\nMoving to drying station")
    print("Drying blood")
    dry(dry_dist, 3, "yes")

    # moving slide to unloading site
    print("\nMoving slide to unloading site")
    slide.enable_pulse()
    move2near_side()

    # unloading slide
    print("\nUnloading slide")
    eject()


if __name__ == "__main__":

    # initializing  classes
    slide = Stepper(config.slide_pins, slide_circum, 1)
    near_switch = Io(config.limit_near_pin, "in") # NEVER DELETE
    far_switch = Io(config.limit_far_pin, "in") # NEVER DELETE
    slide_ui = UserI()
    unload = Servo(config.unload_pin)

    # initializing pins
    slide.init_pins()
    near_switch.init_pin() # NEVER DELETE
    far_switch.init_pin() # NEVER DELETE
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