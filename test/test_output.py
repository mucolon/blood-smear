# test_output.py
# This is the test code for testing GPIO outputs
#
# run program with this line of code below from home directory (/~)
# sudo python3 blood-smear/test/test_output.py

# importing libraries
from digital_io import Digital_Io  # NEVER DELETE
# from analog_in import Analog_In  # NEVER DELETE
import config


def main():
    # function: main test function
    while True:
        try:
            data = str(input("\nEnter 1 for HIGH or 0 for LOW (n to exit)"))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if data == "n":
            break
        elif int(data) == 0:
            fan.output(0)
            continue
        elif int(data) == 1:
            fan.output(1)
            continue
        else:
            continue


if __name__ == "__main__":

    # initializing  classes and pins
    print("\nInitializing Classes & Pins")
    near_switch = Digital_Io(config.limit_near_pin, "in")  # NEVER DELETE
    far_switch = Digital_Io(config.limit_far_pin, "in")  # NEVER DELETE
    fan = Digital_Io(config.fan_pin, "out", 1)

    # confirming power
    input("Press any key after motors are connected to power.")

    main()

    # cleaning up pins
    print("\nCleaning up pins.")
    near_switch.cleanup()  # NEVER DELETE
    far_switch.cleanup()  # NEVER DELETE
    fan.cleanup()
