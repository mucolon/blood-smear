# test_servo_duty.py
# This is test code for testing a servo motor's duty cycle range
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_servo_duty.py


# importing libraries
import sys
sys.path.insert(0, "/home/debian/blood-smear/lib")
from servo import Servo
from digital_io import Digital_Io  # NEVER DELETE
from analog_in import Analog_In  # NEVER DELETE
from stepper import Stepper
import config


def main(duty):
    # function: main test function
    # duty: float number for a servo's duty cycle to start from
    while True:
        start = duty
        try:
            input_duty = str(input(
                "\nEnter servo duty cycle [0-100] \
                \nOR [n] to exit \
                \nOR [ENTER] to increase by 0.5: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        if input_duty == "n":
            servo.update_duty(start)
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
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    slide = Stepper(config.slide_pins, 72, 1)
    force_pwr = Digital_Io(config.force_pins, "out", 0)  # NEVER DELETE
    force_sig = Analog_In(config.force_pins)  # NEVER DELETE

    while True:
        try:
            input_servo = str(input(
                "\nEnter servo name [r=rotation, l=linear, p=pulley]: "))
        except ValueError:
            print("Error: Invalid Input")
            continue
        # rotation servo: 1.98 - 12.85 @ 50Hz (7.415 straight) (5 trash bin)
        if input_servo == "r":
            servo = Servo(config.rotation_pin, 180)
            servo.start(1.98, 12.85)
            servo.update_duty(7.415)
            duty = 2.6
            break
        # linear servo: 5 extended, 10 retracted @ 50Hz
        elif input_servo == "l":
            servo = Servo(config.linear_pin, 180)
            servo.start(10, 5)
            servo.update_duty(10)
            duty = 10
            break
        #   pulley servo:
        #    stop: 0, 100
        #    ccw: [2.17 - 7.23] (fast - slow) extend blade
        #    cw: [7.55 - 12.59] (slow - fast) retract blade
        elif input_servo == "p":
            servo = Servo(config.pulley_pin, 180)
            servo.start(0, 8)
            servo.update_duty(0)
            duty = 0
            break
        else:
            print("Error: Try again")
            continue

    # confirming power
    input("Press any key after motors are connected to power")

    main(duty)

    print("\nClosing Program")
    servo.cleanup()
    home_switch.cleanup()  # NEVER DELETE
    end_switch.cleanup()  # NEVER DELETE
    slide.cleanup()
