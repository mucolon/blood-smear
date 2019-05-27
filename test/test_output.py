# test_output.py
# This is the test code for testing GPIO outputs
#
# run program with this line of code below from home directory (/~)
# sudo python3 blood-smear/test/test_output.py

# importing libraries
from digital_io import Digital_Io  # NEVER DELETE
# from analog_in import Analog_In  # NEVER DELETE
from stepper import Stepper
from servo import Servo
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
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    fan = Digital_Io(config.fan_pin, "out", 0)
    slide = Stepper(config.slide_pins, 72, 1)
    unload = Servo(config.unload_pin, 180)
    unload.start(3, 14, 50)

    # confirming power
    input("Press any key after motors are connected to power.")

    main()

    # cleaning up pins
    print("\nCleaning up pins.")
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    fan.cleanup()
    slide.cleanup()
    unload.cleanup()
