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


def read_nonstop():
    # function: read analog values continuously
    print("Press [CTRL + C] to exit\n")
    data = open(r"force_sensor_data.txt", "a")
    data.write("\n")
    force_pwr.output(1)
    while True:
        try:
            now = time.time()
            print("Raw value: ", force_sig.read_raw())
            data.write("{} {}\n".format(now, force_sig.read_raw()))
        except KeyboardInterrupt:
            print('Exiting')
            data.close()
            break


def read():
    # function: read analog values at every [ENTER] press
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


# def filter():
    # function: read filtered analog values


if __name__ == "__main__":

    # initializing  classes and pins
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    force_pwr = Digital_Io(config.force_pins, "out", 0)  # NEVER DELETE
    force_sig = Analog_In(config.force_pins)  # NEVER DELETE

    # confirming power
    input("Press any key after switch has been turned on")

    while True:
        try:
            response = str(
                input("\nEnter test name [r=read, f=filter read, rn=read nonstop] \
                    \nOR [n] to exit program: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if response == "r":
            read()
            continue
        # elif response == "f":
        #     filter()
        #     continue
        elif response == "rn":
            read_nonstop()
            continue
        elif response == "n":
            break
        else:
            print("Error: Try again")
            continue

    print("\nClosing Program")
    force_pwr.output(0)
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    force_pwr.cleanup()  # NEVER DELETE
