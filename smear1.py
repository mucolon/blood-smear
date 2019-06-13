# smear1.py
# This is code for making a smear
#
# run program with this line of code below from home directory (/~)
# sudo python3 blood-smear/test/smear1.py


# importing libraries
import time
import sys
import tkinter as tk
sys.path.insert(0, "/home/debian/blood-smear/lib")
from stepper import Stepper
from servo import Servo
from digital_io import Digital_Io  # NEVER DELETE
import config


# declaring constants
# default parameters
slide_circum = 72.087  # [mm]
slide_step = 2  # micro step configuration
default_speed = 50  # [mm/s]
default_wait_time = 0.5  # [s]

# blade dispensing parameters
blade_dist = 135  # [mm] ccw (towards end)
rotate_neutral_duty = 7.415
linear_blade_extend_duty = 5
linear_blade_retract_duty = 10
pulley_fast_dispense_duty = 2.2
pulley_slow_dispense_duty = 7.1
pulley_fast_dispense_time = 12  # [s]
pulley_slow_dispense_time = 8  # [s]
pulley_off_duty = 0

# wick parameters
wick_dist = 25  # [mm] cw (towards home)
wick_time = 4  # [s]

# smear parameters
smear_dist = 45  # [mm] ccw (towards end)

# blade ejection parameters
pulley_retract_duty = 7.8
pulley_retract_time = 8  # [s]
pulley_eject_duty = pulley_fast_dispense_duty
pulley_eject_time = 5  # [s]
rotate_eject_duty = 5

# fan parameters
dry_dist = 75 + smear_dist / 2  # [mm] cw (towards home)
dry_time = 30  # [sec] (optimal value: 150)


class Smear(Stepper, Digital_Io, Servo):

    def __init__(self, master):
        # function: sets up pins for motors and sensors and initializes gui
        # master: variable name for gui window
        self.master = master
        pad = 3
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.title("Blood Smearing Device")

    def active_widgets(self):
        # function: lists all active widgets in window
        # function return: list of all active widgets
        _list = self.master.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        return _list

    def power_on(self):
        # function: outputs a window to turn on motor switch
        widget_list = self.active_widgets()
        for item in widget_list:
            item.grid_forget()

        self.label_power_on = tk.Label(
            self.master, text="Please turn switch on", font=("Verdana Bold", 24))
        self.label_power_on.grid(row=0, columnspan=4, pady=70, padx=310)
        self.button_power_on = tk.Button(
            self.master, text="Okay", font=("Verdana Bold", 24), command=self.load_slide)
        self.button_power_on.grid(row=1, columnspan=4, pady=30,
                                  padx=310, ipadx=20, ipady=15)

    def power_off(self):
        # function: outputs a window to turn off motor switch
        widget_list = self.active_widgets()
        for item in widget_list:
            item.grid_forget()

        self.label_power_off = tk.Label(
            self.master, text="Please turn switch off", font=("Verdana Bold", 24))
        self.label_power_off.grid(row=0, columnspan=4, pady=70, padx=300)
        self.button_power_off = tk.Button(
            self.master, text="Okay", font=("Verdana Bold", 24))
        self.button_power_off.grid(row=1, columnspan=4, pady=30,
                                   padx=300, ipadx=20, ipady=15)

    def quit(self):
        # function: quit and exit program
        self.cleanup()
        self.power_off()
        self.master.destroy()

    def load_slide(self):
        # function: outputs a window to load slide
        widget_list = self.active_widgets()
        for item in widget_list:
            item.grid_forget()

        # moving to loading site
        self.move2home()

        self.label_slide = tk.Label(
            self.master, text="Please load slide with blood droplet", font=("Verdana Bold", 24))
        self.label_slide.grid(row=0, columnspan=4, pady=70, padx=230)
        self.button_slide = tk.Button(
            self.master, text="Okay", font=("Verdana Bold", 24), command=self.start)
        self.button_slide.grid(row=1, columnspan=4, pady=30,
                               padx=200, ipadx=20, ipady=15)

    def during_smear(self):
        # function: outputs a window during smearing process
        widget_list = self.active_widgets()
        for item in widget_list:
            item.grid_forget()

        self.label_smear = tk.Label(
            self.master, text="Blood smear in progress", font=("Verdana Bold", 24))
        self.label_smear.grid(row=0, columnspan=4, pady=70, padx=300)
        self.emergency_button = tk.Button(
            self.master, text="Emergency Shutoff", font=("Verdana Bold", 24), command=self.quit)
        self.emergency_button.grid(row=1, columnspan=4, pady=30,
                                   padx=300, ipadx=20, ipady=15)
        self.main()

    def smear_done(self):
        # function: outputs a window stating the smear is complete
        widget_list = self.active_widgets()
        for item in widget_list:
            item.grid_forget()

        self.label_done = tk.Label(
            self.master, text="Blood smear is complete", font=("Verdana Bold", 24))
        self.label_done.grid(row=0, columnspan=4, pady=40, padx=200)
        self.label_remove = tk.Label(
            self.master, text="Please remove slide", font=("Verdana Bold", 20))
        self.label_remove.grid(row=1, columnspan=4, pady=20, padx=200)
        self.label_continue = tk.Label(
            self.master, text="Do you want to make another blood smear", font=("Verdana Bold", 22))
        self.label_continue.grid(row=2, columnspan=4, pady=70, padx=200)
        self.button_another = tk.Button(
            self.master, text="Yes", font=("Verdana Bold", 24), command=self.start)
        self.button_another.grid(
            row=3, column=0, columnspan=2, ipady=15, ipadx=20, pady=30, padx=100)
        self.button_no = tk.Button(
            self.master, text="No", font=("Verdana Bold", 24), command=self.quit)
        self.button_no.grid(row=3, column=2, columnspan=2,
                            ipady=15, ipadx=20, pady=30, padx=100)

    def button_press(self, button):
        # function: checks which button is pressed and passes on linear speed
        # button: int number for button
        widget_list = self.active_widgets()
        for item in widget_list:
            item.grid_forget()

        if button == 1:
            self.speed = 180
        elif button == 2:
            self.speed = 175
        elif button == 3:
            self.speed = 165
        elif button == 4:
            self.speed = 160
        elif button == 5:
            self.speed = 155
        elif button == 6:
            self.speed = 150
        elif button == 7:
            self.speed = 120
        elif button == 8:
            self.speed = 100
        self.during_smear()
        # self.main()

    def start(self):
        # function: displays start screen for device
        widget_list = self.active_widgets()
        for item in widget_list:
            item.grid_forget()

        # writing introduction text
        self.label_intro = tk.Label(
            self.master, text="Please choose the Hematocrit percentage of your blood sample", font=("Verdana Bold", 18))
        self.label_intro.grid(row=0, columnspan=4, pady=5)

        # writing text to introduce linear speed descriptions for different hematocrit percentages
        self.label_speed = tk.Label(
            self.master, text="Linear speeds for different Hematocrit percentages are listed below their respective buttons", font=("Verdana Bold", 16))
        self.label_speed.grid(row=1, columnspan=4, pady=20, padx=10)

        # making buttons for different hematocrit percentages
        self.button1 = tk.Button(self.master, text="< 20%", font=(
            "Verdana Bold", 20), command=lambda: self.button_press(1))
        self.button1.grid(row=2, column=0, ipady=15,
                          ipadx=25, padx=15, pady=20)
        self.button2 = tk.Button(self.master, text="20-25%",
                                 font=("Verdana Bold", 20), command=lambda: self.button_press(2))
        self.button2.grid(row=2, column=1, ipady=15,
                          ipadx=20, padx=15, pady=20)
        self.button3 = tk.Button(self.master, text="25-30%",
                                 font=("Verdana Bold", 20), command=lambda: self.button_press(3))
        self.button3.grid(row=2, column=2, ipady=15,
                          ipadx=20, padx=15, pady=20)
        self.button4 = tk.Button(self.master, text="30-35%",
                                 font=("Verdana Bold", 20), command=lambda: self.button_press(4))
        self.button4.grid(row=2, column=3, ipady=15,
                          ipadx=20, padx=15, pady=20)
        self.button5 = tk.Button(self.master, text="35-40%",
                                 font=("Verdana Bold", 20), command=lambda: self.button_press(5))
        self.button5.grid(row=4, column=0, ipady=15,
                          ipadx=20, padx=15, pady=20)
        self.button6 = tk.Button(self.master, text="40-45%",
                                 font=("Verdana Bold", 20), command=lambda: self.button_press(6))
        self.button6.grid(row=4, column=1, ipady=15,
                          ipadx=20, padx=15, pady=20)
        self.button7 = tk.Button(self.master, text="45-50%",
                                 font=("Verdana Bold", 20), command=lambda: self.button_press(7))
        self.button7.grid(row=4, column=2, ipady=15,
                          ipadx=20, padx=15, pady=20)
        self.button8 = tk.Button(self.master, text="> 50%", font=(
            "Verdana Bold", 20), command=lambda: self.button_press(8))
        self.button8.grid(row=4, column=3, ipady=15,
                          ipadx=25, padx=15, pady=20)

        # writing linear speed descriptions for each hematocrit percentage range
        self.text1 = tk.Label(self.master, text="180 mm/s",
                              font=("Verdana Bold", 14))
        self.text1.grid(row=3, column=0)
        self.text2 = tk.Label(self.master, text="175 mm/s",
                              font=("Verdana Bold", 14))
        self.text2.grid(row=3, column=1)
        self.text3 = tk.Label(self.master, text="165 mm/s",
                              font=("Verdana Bold", 14))
        self.text3.grid(row=3, column=2)
        self.text4 = tk.Label(self.master, text="160 mm/s",
                              font=("Verdana Bold", 14))
        self.text4.grid(row=3, column=3)
        self.text5 = tk.Label(self.master, text="155 mm/s",
                              font=("Verdana Bold", 14))
        self.text5.grid(row=5, column=0)
        self.text6 = tk.Label(self.master, text="150 mm/s",
                              font=("Verdana Bold", 14))
        self.text6.grid(row=5, column=1)
        self.text7 = tk.Label(self.master, text="120 mm/s",
                              font=("Verdana Bold", 14))
        self.text7.grid(row=5, column=2)
        self.text8 = tk.Label(self.master, text="100 mm/s",
                              font=("Verdana Bold", 14))
        self.text8.grid(row=5, column=3)

        # making a quit button
        self.quit_button = tk.Button(self.master, text="Quit", font=(
            "Verdana Bold", 18), command=self.quit)
        self.quit_button.grid(row=6, columnspan=4, ipady=15,
                              ipadx=25, padx=20, pady=20)

    def move2home(self):
        # function: move slide to linear guide motor
        while home_switch.read() == 1:
            slide.move_steps(1, default_speed, "ccw")

    def move2end(self):
        # function: move slide to linear guide end
        while end_switch.read() == 1:
            slide.move_steps(1, default_speed, "cw")

    def blade(self, distance):
        # function: move to smearing blade extension site and extend blade
        # distance: float number of slide linear distance to smearing blade
        #           extension site [mm]
        slide.move_linear(distance, default_speed, "cw")
        time.sleep(default_wait_time)

        linear.update_duty(linear_blade_extend_duty)
        time.sleep(default_wait_time)

        rotate.update_duty(rotate_neutral_duty)
        pulley.update_duty(pulley_slow_dispense_duty)
        time.sleep(pulley_slow_dispense_time)

        rotate.update_duty(rotate_neutral_duty)
        pulley.update_duty(pulley_fast_dispense_duty)
        time.sleep(pulley_fast_dispense_time)

        pulley.update_duty(pulley_off_duty)

    def wick(self, distance, wait_time, manual="no"):
        # function: move to wicking site and wait for wick to finish
        # distance: float number of slide linear distance to wicking site [mm]
        # wait_time: float number of time for blood to wick onto smearing
        #            blade [sec]
        # manual: by default "no" allows time to wick to be preselected
        #         ie. wait_time or
        #         "yes" for manual override
        slide.move_linear(distance, default_speed, "ccw")
        if manual == "no":
            time.sleep(wait_time)
        elif manual == "yes":
            input("\nPress [ENTER] after blood has wicked")
        else:
            print("\nError: Invalid string for manual")
            print("\"no\" to use preselected wicking wait time")
            print("\"yes\" to manually proceed after blood has visually wicked")
            print("Please use quotation marks")

    def smear(self, distance, speed):
        # function: move slide for smear
        # distance: float number of slide linear distance for smear [mm]
        # speed: float number of motor load's linear velocity [mm/s]
        slide.move_linear(distance, speed, "cw")
        time.sleep(default_wait_time)

        pulley.update_duty(pulley_retract_duty)
        time.sleep(pulley_retract_time)

        pulley.update_duty(pulley_off_duty)

    def dry(self, distance, wait_time, manual="no"):
        # function: move slide to drying site and wait for blood to dry
        # distance: float number of slide linear distance after smear to
        #           heater [mm]
        # wait_time: float number for time to dry blood slide [sec]
        # manual: by default "no" allows time to dry to be preselected
        #         ie. wait_time or
        #         "yes" for manual override
        slide.move_linear(distance, default_speed, "ccw")
        fan.output(1)  # on
        rotate.update_duty(rotate_eject_duty)
        time.sleep(default_wait_time)

        pulley.update_duty(pulley_eject_duty)
        time.sleep(pulley_eject_time)

        pulley.update_duty(pulley_off_duty)
        time.sleep(default_wait_time)

        rotate.update_duty(rotate_neutral_duty)
        time.sleep(default_wait_time)

        linear.update_duty(linear_blade_retract_duty)
        if manual == "no":
            time.sleep(wait_time)
            fan.output(0)  # off
            print("Blood has dried")
        elif manual == "yes":
            input("\nPress [ENTER] after blood has dried")
            fan.output(0)  # off
            print("Blood has dried")
        else:
            print("\nError: Invalid string for manual")
            print("\"no\" to use preselected drying wait time")
            print("\"yes\" to manually proceed after blood has visually dried")
            print("Please use quotation marks")

    def main(self):
        # function: complete smearing process

        # moving slide to smearing station
        self.blade(blade_dist)

        # blood wicking interface
        self.wick(wick_dist, wick_time)

        # smearing blood
        self.smear(smear_dist, self.speed)

        # drying blood
        self.dry(dry_dist, dry_time)

        # moving slide to unloading site
        self.move2home()

        self.smear_done()

    def cleanup(self):
        # function: cleans up all used pins for motors and sensors
        slide.cleanup()
        home_switch.cleanup()  # NEVER DELETE
        end_switch.cleanup()  # NEVER DELETE
        linear.cleanup()
        pulley.cleanup()
        rotate.cleanup()
        fan.cleanup()


if __name__ == "__main__":

    # initializing  classes and pins
    slide = Stepper(config.slide_pins, slide_circum, slide_step)
    home_switch = Digital_Io(config.limit_home_pin, "in")  # NEVER DELETE
    end_switch = Digital_Io(config.limit_end_pin, "in")  # NEVER DELETE
    linear = Servo(config.linear_pin)
    pulley = Servo(config.pulley_pin)
    rotate = Servo(config.rotation_pin, 180)
    fan = Digital_Io(config.fan_pin, "out", 0)

    # initializing pins
    rotate.start(1.98, 12.85)
    rotate.update_duty(rotate_neutral_duty)
    linear.start(10, 5)
    linear.update_duty(linear_blade_retract_duty)
    pulley.start(0, 12.59)
    pulley.update_duty(pulley_off_duty)

    # setting up gui window
    window = tk.Tk()
    smear = Smear(window)

    # complete smearing process
    smear.power_on()
    window.mainloop()
