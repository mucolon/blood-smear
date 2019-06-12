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
stepper_step = 2  # micro step configuration
default_speed = 50  # [mm/s]


def move2home(speed):
    # function: moves slide to home position
    # speed: float number for linear travel speed [mm/s]
    # function return: int 1 to identify slide at home position
    if home_switch.read() == 1:
        slide.move_linear(5, default_speed, "cw")
    else:
        while home_switch.read() == 1:
            slide.move_steps(1, speed, "ccw")
    return 1


def move2end(speed):
    # function: moves slide to end position
    # speed: float number for linear travel speed [mm/s]
    # function return: int 0 to identify slide at end position
    if end_switch.read() == 1:
        slide.move_linear(5, default_speed, "ccw")
    else:
        while end_switch.read() == 1:
            slide.move_steps(1, speed, "cw")
    return 0


def side2side():
    # function: moves slide side to side with input linear velocity
    home = 1
    while True:
        try:
            input_speed = str(input(
                "\nEnter linear slide speed [0-10000 mm/s] \
                \nOR [n] to back out: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if input_speed == "n":
            break
        elif home == 1:
            speed = float(input_speed)
            home = move2end(speed)
            continue
        elif home == 0:
            speed = float(input_speed)
            home = move2home(speed)
            continue
        elif float(input_speed) < 0:
            print("Error: Input speed cannot be negative")
            continue
        elif float(input_speed) > 10000:
            print("Error: Input speed cannot be greater than 10000 mm/s")
            continue
        else:
            print("Error: Try again")
            continue


def rotate():
    # function: moves slide one complete rotation with input linear velocity
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
            slide.rotate2(1, delay, "ccw")
            continue
        elif response == "b":
            delay = float(input("Enter step delay [ms]: "))
            slide.rotate2(1, delay, "cw")
            continue
        elif response == "h":
            move2home(default_speed)
        else:
            print("Error: Try again")
            continue


def velocity():
    # function: moves slide one revolution with input linear velocity
    data = open(r"slide_speed_data.txt", "a")
    data.write("\n% microstep = {}\n".format(stepper_step))
    while True:
        try:
            response = str(input("\nEnter linear slide speed [0-200 mm/s] \
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
        elif float(response) > 200:
            print("Error: Input speed cannot be greater than 200 mm/s")
            continue
        else:
            input_speed = float(response)
            now = time.time()
            slide.rotate(1, input_speed, "ccw")
            future = time.time()
            time_diff = future - now
            speed = stepper_circum / time_diff
            print(time_diff, "seconds")
            print(speed, "mm/s")
            data.write("{} {}\n".format(input_speed, speed))
            input("Press [ENTER] to redo test")
            move2home(default_speed)
            continue


def linear():
    # function: moves slide with input linear distance
    while True:
        try:
            response = str(input(
                "\nEnter linear slide travel distance [0-200 mm] \
                \nOR [h] to move back to home \
                \nOR [n] to back out: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if response == "n":
            break
        elif response == "h":
            move2home(default_speed)
            continue
        elif float(response) < 0:
            print("Error: Distance cannot be negative")
            continue
        elif float(response) > 200:
            print("Error: Distance cannot be greater than 200 mm")
            continue
        else:
            while True:
                try:
                    direction = str(input("Enter direction [cw or ccw]: "))
                except ValueError:
                    print("Error: Invalid Input")
                    continue
                if direction == "cw":
                    break
                elif direction == "ccw":
                    break
                else:
                    print("Error: Try again")
                    continue
            distance = float(response)
            slide.move_linear(distance, default_speed, direction)
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

    move2home(default_speed)

    while True:
        try:
            response = str(
                input("\nEnter test name [s=side2side, r=rotation, v=velocity, l=linear] \
                    \nOR [n] to exit program \
                    \nOR [h] for help: "))
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
        elif response == "l":
            linear()
        elif response == "n":
            break
        elif response == "h":
            print("side2side: Moves slide side to slide with input speed")
            print("rotation: Moves slide with input rotations")
            print("velocity: Moves slide 1 rotation with input speed and records data")
            print("linear: Moves slide with input linear distance")
        else:
            print("Error: Try again")
            continue

    print("\nClosing Program")
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    slide.cleanup()
