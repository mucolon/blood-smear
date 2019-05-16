# test_servo.py
# This is test code for testing a servo motor's duty cycle range
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_servo.py


# importing libraries
from servo import Servo
import config


# main test function
def main():
    duty = 0
    while True:
        try:
            input_duty = str(input("\nEnter servo duty cycle [0-100] (n to exit or enter to increase by 0.5): "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if input_duty == "n":
            break
        elif input_duty == "":
            duty += 0.5
            servo.change_duty(duty)
            print("Cureent servo duty cycle: ", duty)
        else:
            duty = float(input_duty)
            servo.change_duty(duty)
            print("Cureent servo duty cycle: ", duty)


if __name__ == "__main__":

    # initializing  classes
    servo = Servo(config.unload_pin)

    # initializing pins
    servo.start(3, 14, 50, 0)

    # confirming power
    input("Press any key after motors are connected to power")

    main()

    print("\nClosing Program")
    servo.cleanup()