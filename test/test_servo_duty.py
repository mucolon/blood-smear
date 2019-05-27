# test_servo_duty.py
# This is test code for testing a servo motor's duty cycle range
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_servo_duty.py


# importing libraries
from servo import Servo
from digital_io import Digital_Io  # NEVER DELETE
from stepper import Stepper
import config


# declaring constants
start = 3
end = 14


def main():
    # function: main test function
    duty = start
    while True:
        try:
            input_duty = str(input(
                "\nEnter servo duty cycle [0-100] (n to exit or enter to increase by 0.5): "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if input_duty == "n":
            break
        elif input_duty == "":
            duty += 0.5
            servo.update_duty(duty)
            print("Current servo duty cycle: ", duty)
            continue
        else:
            duty = float(input_duty)
            servo.update_duty(duty)
            print("Current servo duty cycle: ", duty)
            continue


if __name__ == "__main__":

    # initializing  classes
    servo = Servo(config.unload_pin, 180)
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    slide = Stepper(config.slide_pins, 72)

    # initializing pins
    servo.start(start, end, 50)
    # unload servo duty: 2.8 - 14 @ 50Hz
    # smear assembly servo: 2 - 12.8 @ 50Hz (2.5 straight)
    # pulley servo: 0 stops, 7.1 good slow speed @ 50Hz
    # linear servo: 5 extended, 10 retracted @ 50Hz

    # confirming power
    input("Press any key after motors are connected to power")

    main()

    print("\nClosing Program")
    servo.cleanup()
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    slide.cleanup()
