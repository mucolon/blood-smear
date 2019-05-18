# test_servo.py
# This is test code for testing a servo motor rotation
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_servo.py


# importing libraries
from servo import Servo
from input_io import Input_io # NEVER DELETE
import config


# main test function
def main():
    while True:
        try:
            angle = str(input("\nEnter servo motor angle from [0-180] degrees (n to exit): "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if angle == "n":
            break
        else:
            angle_f = float(angle)
            servo.change_angle(angle_f)
            print("Current servo angle: ", angle_f)


if __name__ == "__main__":

    # initializing  classes
    servo = Servo(config.unload_pin)
    near_switch = Input_io(config.limit_near_pin, "fall") # NEVER DELETE
    far_switch = Input_io(config.limit_far_pin, "fall") # NEVER DELETE

    # initializing pins
    servo.start(3, 14, 50, 0)
    near_switch.init_pin() # NEVER DELETE
    far_switch.init_pin() # NEVER DELETE

    # confirming power
    input("Press any key after motors are connected to power")

    main()

    print("\nClosing Program")
    servo.cleanup()
    near_switch.cleanup() # NEVER DELETE
    far_switch.cleanup() # NEVER DELETE