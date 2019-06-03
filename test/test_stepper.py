# test_stepper.py
# This is test code for testing a stepper motor
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_stepper.py


# importing libraries
from stepper import Stepper
from digital_io import Digital_Io  # NEVER DELETE
from analog_in import Analog_In  # NEVER DELETE
import config


# declaring constants
stepper_circum = 72  # [mm]
stepper_step = 1  # micro step configuration


def main():
    # function: main test function
    while True:
        try:
            input_dir = str(input(
                "\nEnter 1 for clockwise rotation or 0 for counter-clockwise rotation \
                \n OR n to exit"))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if input_dir == "n":
            break
        elif input_dir == "1":
            slide.move_steps(5, 90, "cw")
            continue
        else:
            slide.move_steps(5, 90, "ccw")
            continue


if __name__ == "__main__":

    # initializing  classes
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    slide = Stepper(config.slide_pins, stepper_circum, stepper_step)
    force_pwr = Digital_Io(config.force_pins, "out", 0)  # NEVER DELETE
    force_sig = Analog_In(config.force_pins)  # NEVER DELETE

    # confirming power
    input("Press any key after motors are connected to power")

    main()

    print("\nClosing Program")
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    slide.cleanup()
