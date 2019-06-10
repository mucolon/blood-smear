# test_stepper.py
# This is test code for testing a stepper motor
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_stepper.py


# importing libraries
import sys
import time
sys.path.insert(0, "/home/debian/blood-smear/lib")
from stepper import Stepper
from digital_io import Digital_Io  # NEVER DELETE
from analog_in import Analog_In  # NEVER DELETE
import config


# declaring constants
stepper_circum = 72.087  # [mm]
stepper_step = 4  # micro step configuration
defualt_speed_mms = 200  # [mms]
defualt_speed_rpm = 190  # [rpm]


def move2home(mms):
    # function: moves slide to home position
    # mms: float number for linear travel speed
    # function return: int 1 to identify slide at home position
    rpm = slide.convert_mms2rpm(mms)
    while home_switch.read() == 1:
        slide.move_steps(1, rpm, "cw")
    return 1


def move2end(mms):
    # function: moves slide to end position
    # mms: float number for linear travel speed
    # function return: int 0 to identify slide at end position
    rpm = slide.convert_mms2rpm(mms)
    while end_switch.read() == 1:
        slide.move_steps(1, rpm, "ccw")
    return 0


def side2side():
    # function: moves slide side to side
    home = 1
    while True:
        try:
            input_mms = str(input(
                "\nEnter linear slide speed [0-10000 mm/s] \
                \nOR [n] to back out: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if input_mms == "n":
            break
        elif home == 1:
            mms = float(input_mms)
            home = move2end(mms)
            continue
        elif home == 0:
            mms = float(input_mms)
            home = move2home(mms)
            continue
        elif float(input_mms) < 0:
            print("Error: Input speed cannot be negative")
            continue
        elif float(input_mms) > 10000:
            print("Error: Input speed cannot be greater than 10000 mm/s")
            continue
        else:
            print("Error: Try again")
            continue


def rotate():
    # function: moves slide one complete rotation at a time
    while True:
        try:
            response = str(input(
                "\nPress [ENTER] to move 1 revolution towards the end \
                \nOR [b] to move 1 revolution towards home \
                \nOR [h] to move back to home \
                \nOR [n] to back out: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if response == "n":
            break
        elif response == "":
            delay = float(input("Enter step delay [ms]: "))
            # slide.rotate(1, defualt_speed_rpm, "ccw")
            slide.rotate2(1, delay, "ccw")
            continue
        elif response == "b":
            delay = float(input("Enter step delay [ms]: "))
            # slide.rotate(1, defualt_speed_rpm, "cw")
            slide.rotate2(1, delay, "ccw")
            continue
        elif response == "h":
            move2home(defualt_speed_mms)
        else:
            print("Error: Try again")
            continue


def velocity():
    # function: moves slide one revolution at input linear velocity
    data = open(r"slide_speed_data.txt", "a")
    data.write("\n")
    while True:
        try:
            response = str(input("\nEnter linear slide speed [0-10000 mm/s] \
                \nOR [n] to back out: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if response == "n":
            data.close()
            break
        elif float(response) < 0:
            print("Error: Input speed cannot be negative")
            continue
        elif float(response) > 10000:
            print("Error: Input speed cannot be greater than 10000 mm/s")
            continue
        else:
            mms = float(response)
            rpm = slide.convert_mms2rpm(mms)
            now = time.time()
            slide.rotate(1, rpm, "ccw")
            future = time.time()
            time_diff = future - now
            speed = stepper_circum / time_diff
            print(time_diff, "seconds")
            print(speed, "mm/s")
            data.write("{} {}\n".format(mms, speed))
            input("Press [ENTER] to redo test")
            move2home(defualt_speed_mms)
            continue


if __name__ == "__main__":

    # initializing  classes
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    slide = Stepper(config.slide_pins, stepper_circum, stepper_step)
    force_pwr = Digital_Io(config.force_pins, "out", 0)  # NEVER DELETE
    force_sig = Analog_In(config.force_pins)  # NEVER DELETE

    # confirming power
    input("Press [ENTER] after motors are connected to power")

    move2home(defualt_speed_mms)

    while True:
        try:
            response = str(
                input("\nEnter test name [s=side2side, r=rotation, v=velocity] \
                    \nOR [n] to exit program: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if response == "s":
            side2side()
            continue
        elif response == "r":
            rotate()
            continue
        elif response == "v":
            velocity()
        elif response == "n":
            break
        else:
            print("Error: Try again")
            continue

    print("\nClosing Program")
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    slide.cleanup()
