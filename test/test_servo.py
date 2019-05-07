# test_servo.py
# This is test code for testing a servo motor
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_servo.py


# importing libraries
from servo import Servo
from stepper import Stepper
from input_io import Input_io
import config


# main test function
def main():
    while True:
        try:
            # angle = str(input("\nEnter servo motor angle (n to exit): "))
            duty = str(input("\nEnter servo duty cycle [0-100] (n to exit): "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        # if angle == "n":
        if duty == "n":
            break
        # angle_f = float(angle)
        # servo.change_angle(angle_f)
        duty = int(duty)
        servo.change_duty(duty)
        # print("Current servo angle: ", angle_f)
        print("Cureent servo duty cycle: ", duty)


if __name__ == "__main__":

    # initializing  classes
    servo = Servo(config.unload_pin)
    near_switch = Input_io(config.limit_near_pin, "fall")
    far_switch = Input_io(config.limit_far_pin, "fall")
    slide = Stepper(config.slide_pins)

    # initializing pins
    servo.start(5, 10, 50, 0)
    near_switch.init_pin()
    far_switch.init_pin()
    slide.init_pins()

    # confirming power
    input("Press any key after motors are connected to power")

    main()

    print("\nClosing Program")
    servo.cleanup()
    near_switch.cleanup()
    far_switch.cleanup()
    slide.cleanup()