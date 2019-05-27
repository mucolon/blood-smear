# test_servo_angle.py
# This is test code for testing a servo motor rotation by angle inputs
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_servo_angle.py


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
    while True:
        try:
            angle = str(
                input("\nEnter servo motor angle from [0-180] degrees (n to exit): "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if angle == "n":
            break
        elif float(angle) >= 0:
            angle_f = float(angle)
            servo.update_angle(angle_f)
            print("Current servo angle: ", angle_f)
            continue
        else:
            continue


if __name__ == "__main__":

    # initializing  classes
    servo = Servo(config.unload_pin, 180)
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    slide = Stepper(config.slide_pins, 72)

    # initializing pins
    servo.start(start, end, 50)

    # confirming power
    input("Press any key after motors are connected to power")

    main()

    print("\nClosing Program")
    servo.cleanup()
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    slide.cleanup()
