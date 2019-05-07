# test_servo.py
# This is test code for testing a servo motor
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_servo.py


# importing libraries
from servo import Servo
import config


# main test function
def main():
    while True:
        try:
            angle = str(input("\nEnter servo motor angle (n to exit): "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if angle == "n":
            break
        angle_f = float(angle)
        servo.change_angle(angle_f)
        print("Current servo angle: ", angle_f)


if __name__ == "__main__":

    # initializing  classes
    servo = Servo(config.unload_pin)

    # initializing pins
    servo.start(5, 10, 50)

    # confirming power
    input("Press any key after motors are connected to power")

    main()

    print("\nClosing Program")
    servo.cleanup()