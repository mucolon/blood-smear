# test_smear.py
# This is test code for making a blood smear using a terminal interface
#
# run program with this line of code below from home directory (/~)
# sudo python3 blood-smear/test/test_smear.py


# importing libraries
import time
import sys
import numpy as np
sys.path.insert(0, "/home/debian/blood-smear/lib")
from ui import UserI
from stepper import Stepper
from servo import Servo
from digital_io import Digital_Io  # NEVER DELETE
from analog_in import Analog_In  # NEVER DELETE
import config


# declaring constants
# default parameters
slide_circum = 72.087  # [mm]
slide_step = 2  # micro step configuration
default_speed = 50  # [mm/s]
default_wait_time = 0.5  # [s]
inductive_sensor_buffer = 6  # [mm]

# blade dispensing parameters
blade_dist = 149.35  # [mm] ccw (towards end)
rotate_neutral_duty = 7.415
linear_blade_extend_duty = 5
linear_blade_retract_duty = 10
pulley_dispense_duty = 2.17
pulley_dispense_time = 20  # [s]
pulley_off_duty = 0
force_threshold = 300
sample_amount = 10
filtered_amount = 3

# wick parameters
wick_dist = 21  # [mm] cw (towards home)
wick_speed = 80  # [mm/s]
wick_time = 4  # [s]

# smear parameters
smear_dist = 47.89  # [mm] ccw (towards end)

# blade ejection parameters
pulley_retract_duty = 7.54
pulley_retract_time = 35  # [s]
pulley_eject_duty = 2.17
pulley_eject_time = 5  # [s]
rotate_eject_duty = 5

# fan parameters
dry_dist = 56 + smear_dist / 2  # [mm] cw (towards home)
dry_time = 5  # [sec] (optimal value: 150)

# force_diameter = 25.4E-3  # [m]
# force_area = pi * ((force_diameter / 2) ** 2)  # [m^2]


def move2home():
    # function: move slide to linear guide motor
    if home_switch.read() == 1:
        slide.move_linear(inductive_sensor_buffer, default_speed, "cw")
    else:
        while home_switch.read() == 1:
            slide.move_steps(1, default_speed, "ccw")
    slide.disable_pulse()


def move2end():
    # function: move slide to linear guide end
    while end_switch.read() == 1:
        slide.move_steps(1, default_speed, "cw")


def blade(distance):
    # function: move to smearing blade extension site and extend blade
    # distance: float number of slide linear distance to smearing blade
    #           extension site [mm]
    slide.move_linear(distance, default_speed, "ccw")
    time.sleep(default_wait_time)

    linear.change_duty(linear_blade_retract_duty,
                       linear_blade_extend_duty, 100)
    time.sleep(default_wait_time)

    pulley.update_duty(pulley_dispense_duty)
    time.sleep(pulley_dispense_time)

    pulley.update_duty(pulley_off_duty)


def wick(distance, wait_time, manual="no"):
    # function: move to wicking site and wait for wick to finish
    # distance: float number of slide linear distance to wicking site [mm]
    # wait_time: float number of time for blood to wick onto smearing
    #            blade [sec]
    # manual: by default "no" allows time to wick to be preselected
    #         ie. wait_time or
    #         "yes" for manual override
    slide.move_linear(distance, wick_speed, "cw")
    if manual == "no":
        time.sleep(wait_time)
    elif manual == "yes":
        input("\nPress [ENTER] after blood has wicked")
    else:
        print("\nError: Invalid string for manual")
        print("\"no\" to use preselected wicking wait time")
        print("\"yes\" to manually proceed after blood has visually wicked")
        print("Please use quotation marks")


def smear(distance, speed):
    # function: move slide for smear
    # distance: float number of slide linear distance for smear [mm]
    # speed: float number of motor load's linear velocity [mm/s]
    slide.move_linear(distance, speed, "ccw")
    time.sleep(default_wait_time)

    pulley.update_duty(pulley_retract_duty)
    time.sleep(pulley_retract_time)

    pulley.update_duty(pulley_off_duty)


def dry(distance, wait_time, manual="no"):
    # function: move slide to drying site and wait for blood to dry
    # distance: float number of slide linear distance after smear to
    #           heater [mm]
    # wait_time: float number for time to dry blood slide [sec]
    # manual: by default "no" allows time to dry to be preselected
    #         ie. wait_time or
    #         "yes" for manual override
    slide.move_linear(distance, default_speed, "cw")
    fan.output(1)  # on
    # rotate.update_duty(rotate_eject_duty)
    rotate.change_duty(rotate_neutral_duty, rotate_eject_duty)
    time.sleep(default_wait_time)

    pulley.update_duty(pulley_eject_duty)
    time.sleep(pulley_eject_time)

    pulley.update_duty(pulley_off_duty)
    time.sleep(default_wait_time)

    # rotate.update_duty(rotate_neutral_duty)
    rotate.change_duty(rotate_eject_duty, rotate_neutral_duty)
    time.sleep(default_wait_time)

    linear.update_duty(linear_blade_retract_duty)
    if manual == "no":
        time.sleep(wait_time - (1.5 + pulley_eject_time))
        fan.output(0)  # off
        print("Blood has dried")
    elif manual == "yes":
        input("\nPress [ENTER] after blood has dried")
        fan.output(0)  # off
        print("Blood has dried")
    else:
        print("\nError: Invalid string for manual")
        print("\"no\" to use preselected drying wait time")
        print("\"yes\" to manually proceed after blood has visually dried")
        print("Please use quotation marks")


def main():
    # function: complete smearing process

    # moving slide to start position
    slide.enable_pulse()
    move2home()

    # asking for linear speed
    print("\nPlease enter linear speed of smear below")
    input_speed = slide_ui.linear_speed()

    # slide loading interface
    print("\nPlease load slide with blood droplet")
    input("Press [ENTER] after slide is loaded")

    # moving slide to smearing station
    print("\nMoving blood slide to smearing blade")
    blade(blade_dist)

    # blood wicking interface
    print("\nWaiting for blood to wick")
    wick(wick_dist, wick_time)

    # smearing blood
    print("\nSmearing blood")
    smear(smear_dist, input_speed)
    print("Completed smear")

    # drying blood
    print("\nMoving to drying station")
    print("Drying blood")
    dry(dry_dist, dry_time)

    # moving slide to unloading site
    print("\nMoving slide to unloading site")
    move2home()
    slide.disable_pulse()

    # unloading slide
    print("\nUnload slide")
    input("Press [ENTER] after slide has been unloaded")


def cleanup():
    # function: cleans up all used pins for motors and sensors
    slide.cleanup()
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    linear.cleanup()
    pulley.cleanup()
    rotate.cleanup()
    fan.cleanup()


if __name__ == "__main__":

    # initializing  classes and pins
    slide = Stepper(config.slide_pins, slide_circum, slide_step)
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    slide_ui = UserI()
    linear = Servo(config.linear_pin)
    pulley = Servo(config.pulley_pin)
    rotate = Servo(config.rotation_pin, 180)
    fan = Digital_Io(config.fan_pin, "out", 0)

    # initializing pins
    rotate.start(1.98, 12.86)
    rotate.update_duty(rotate_neutral_duty)
    linear.start(10, 5)
    linear.update_duty(linear_blade_retract_duty)
    pulley.start(0, 7.1)
    pulley.update_duty(pulley_off_duty)

    # confirming power
    input("Press [ENTER] after switch has been turned on")

    # complete smearing process
    main()

    # asking to repeat process
    while True:
        try:
            cont = str(
                input("Press [ENTER] if you're loading another slide\
                    \nOR press [n] to stop: "))
        except ValueError:
            print("Error: Invalid Value")
            continue
        if cont == "":
            main()
            continue
        elif cont == "n":
            break
        else:
            continue

    # cleaning up pins
    print("\nClosing Program")
    cleanup()
