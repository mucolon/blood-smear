# test_analog.py
# This is test code for testing analog input voltages
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_analog.py


# importing libraries
import sys
import time
sys.path.insert(0, "/home/debian/blood-smear/lib")
from digital_io import Digital_Io  # NEVER DELETE
from analog_in import Analog_In  # NEVER DELETE
import config


def main():
    # function: read analog values
    force_pwr.output(1)
    while True:
        try:
            response = str(input("\nHold [ENTER] to output values \
                \nOR press [n] to exit: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if response == "n":
            break
        elif response == "":
            print("Raw value: ", force_sig.read_raw())
            continue


if __name__ == "__main__":

    # initializing  classes and pins
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    force_pwr = Digital_Io(config.force_pins, "out", 0)  # NEVER DELETE
    force_sig = Analog_In(config.force_pins)  # NEVER DELETE

    # confirming power
    input("Press any key after switch has been turned on")

    main()

    print("\nClosing Program")
    force_pwr.output(0)
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    force_pwr.cleanup()  # NEVER DELETE
