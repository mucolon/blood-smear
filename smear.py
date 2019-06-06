# smear.py
# This is code for a basic smear
#
# run program with this line of code below from home directory (/~)
# sudo python3 blood-smear/test/smear.py


# importing libraries
from stepper import Stepper
from servo import Servo
from digital_io import Digital_Io  # NEVER DELETE
from analog_in import Analog_In  # NEVER DELETE
import time
import config
# from math import pi


# declaring constants
# default parameters
slide_circum = 72  # [mm]
slide_step = 4  # micro step configuration
default_speed = 150  # [mm/s]

# blade dispensing parameters
dist2blade = 145  # [mm] ccw (towards end)
blade_neutral_duty = 2.6

# wick parameters
dist2wick = 12  # [mm] cw (towards home)
wick_speed = 90  # [mm/s]
wick_time = 3  # [sec]

# smear parameters
smear_dist = 45  # [mm] ccw (towards end)

# blade ejection parameters
eject_duty = 5

# fan parameters
dist2fan = 50 + smear_dist / 2  # [mm] cw (towards home)
dry_time = 20  # [sec] (optimal value: 150)

# force_diameter = 25.4E-3  # [m]
# force_area = pi * ((force_diameter / 2) ** 2)  # [m^2]


class Smear(Stepper, Digital_Io, Servo, Analog_In):

    def __init__(self):
        # function: sets up pins for motors and sensors

        # initializing  classes and pins
        self.slide = Stepper(config.slide_pins, slide_circum, slide_step)
        self.home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
        self.end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
        self.linear = Servo(config.linear_pin)
        self.pulley = Servo(config.pulley_pin)
        self.rotate = Servo(config.rotation_pin, 180)
        self.fan = Digital_Io(config.fan_pin, "out", 0)
        self.force_pwr = Digital_Io(config.force_pins, "out", 0)  # NEVER DELETE
        self.force_sig = Analog_In(config.force_pins)  # NEVER DELETE

        # initializing pins
        self.rotate.start(1.98, 12.86, 50)
        self.rotate.update_duty(blade_neutral_duty)
        self.linear.start(10, 5, 50)
        self.linear.update_duty(10)
        self.pulley.start(0, 7.1, 50)
        self.pulley.update_duty(0)

    def move2home(self):
        # function: move slide to linear guide motor
        self.slide.enable_pulse()
        while self.home_switch.read() == 1:
            self.slide.move_steps(1, default_speed, "cw")
        self.slide.disable_pulse()

    def move2end(self):
        # function: move slide to linear guide end
        self.slide.enable_pulse()
        while self.end_switch.read() == 1:
            self.slide.move_steps(1, default_speed, "ccw")
        self.slide.disable_pulse()

    def blade(self, distance):
        # function: move to smearing blade extension site and extend blade
        # distance: float number of slide linear distance to smearing blade
        #           extension site [mm]
        self.slide.enable_pulse()
        self.slide.move_linear(distance, default_speed, "ccw")
        time.sleep(2)
        self.linear.update_duty(5)  # extended
        self.pulley.update_duty(7)  # slow speed
        while True:
            try:
                stop = str(input("\nPress enter to stop"))
            except ValueError:
                print("Error: Invalid Value")
                continue
            if stop == "":
                self.pulley.update_duty(0)  # off
                self.linear.update_duty(10)  # retracted
                break
            else:
                continue
        self.slide.disable_pulse()

    def wick(self, distance, wait_time, manual="no"):
        # function: move to wicking site and wait for wick to finish
        # distance: float number of slide linear distance to wicking site [mm]
        # wait_time: float number of time for blood to wick onto smearing
        #            blade [sec]
        # manual: by default "no" allows time to wick to be preselected
        #         ie. wait_time or
        #         "yes" for manual override
        self.slide.enable_pulse()
        self.slide.move_linear(distance, wick_speed, "cw")
        if manual == "no":
            time.sleep(wait_time)
        elif manual == "yes":
            input("\nPress any key after blood has wicked")
        else:
            print("\nError: Invalid string for manual")
            print("\"no\" to use preselected wicking wait time")
            print("\"yes\" to manually proceed after blood has visually wicked")
            print("Please use quotation marks")
        self.slide.disable_pulse()

    def smear(self, distance, mms_speed):
        # function: move slide for smear
        # distance: float number of slide linear distance for smear [mm]
        # mms_speed: float number of motor load's linear velocity [mm/s]
        self.slide.enable_pulse()
        rpm = self.slide.convert_mms2rpm(mms_speed)
        self.slide.move_linear(distance, rpm, "ccw")
        self.time.sleep(2)
        self.slide.disable_pulse()

    def dry(self, distance, wait_time, manual="no"):
        # function: move slide to drying site and wait for blood to dry
        # distance: float number of slide linear distance after smear to
        #           heater [mm]
        # wait_time: float number for time to dry blood slide [sec]
        # manual: by default "no" allows time to dry to be preselected
        #         ie. wait_time or
        #         "yes" for manual override
        self.slide.enable_pulse()
        self.slide.move_linear(distance, default_speed, "cw")
        self.fan.output(1)  # on
        self.rotate.update_duty(eject_duty)  # turns ccw
        self.pulley.update_duty(5)  # on
        time.sleep(5)
        self.pulley.update_duty(0)  # off
        self.rotate.update_duty(blade_neutral_duty)
        if manual == "no":
            time.sleep(wait_time)
            self.fan.output(0)  # off
            print("Blood has dried")
        elif manual == "yes":
            input("\nPress any key after blood has dried")
            self.fan.output(0)  # off
            print("Blood has dried")
        else:
            print("\nError: Invalid string for manual")
            print("\"no\" to use preselected drying wait time")
            print("\"yes\" to manually proceed after blood has visually dried")
            print("Please use quotation marks")
        self.slide.disable_pulse()

    def main(self):
        # function: complete smearing process

        # moving slide to start position
        self.move2home()

        # slide loading interface
        print("\nPlease load slide with blood droplet")
        input("Press any key after slide is loaded")

        # moving slide to smearing station
        print("\nMoving blood slide to smearing blade")
        self.blade(dist2blade)

        # blood wicking interface
        print("\nWaiting for blood to wick")
        self.wick(dist2wick, wick_time)

        # smearing blood
        print("\nSmearing blood")
        self.smear(smear_dist)
        print("Completed smear")

        # drying blood
        print("\nMoving to drying station")
        print("Drying blood")
        self.dry(dist2fan, dry_time)

        # moving slide to unloading site
        print("\nMoving slide to unloading site")
        self.move2home()

        # unloading slide
        print("\nUnload slide")
        input("Press any key after slide has been unloaded")

    def cleanup(self):
        # function: cleans up all used pins for motors and sensors
        self.slide.cleanup()
        self.home_switch.cleanup()  # NEVER DELETE
        self.end_switch.cleanup()  # NEVER DELETE
        self.linear.cleanup()
        self.pulley.cleanup()
        self.rotate.cleanup()
        self.fan.cleanup()


if __name__ == "__main__":

    smear = Smear()

    # confirming power
    input("Press any key after switch has been turned on")

    # complete smearing process
    smear.main()

    # asking to repeat process
    while True:
        try:
            cont = str(
                input("Press enter if you're loading another slide\nOR\n Press n to stop: "))
        except ValueError:
            print("Error: Invalid Value")
            continue
        if cont == "":
            smear.main()
            break
        elif cont == "n":
            break
        else:
            continue

    # cleaning up pins
    print("\nClosing Program")
    smear.cleanup()
