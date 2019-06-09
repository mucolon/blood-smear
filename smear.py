# smear.py
# This is code for a basic smear
#
# run program with this line of code below from home directory (/~)
# sudo python3 blood-smear/smear.py


# importing libraries
import tkinter as tk
import time
import sys
sys.path.insert(0, "~/blood-smear/lib")
from stepper import Stepper
from servo import Servo
from digital_io import Digital_Io  # NEVER DELETE
from analog_in import Analog_In  # NEVER DELETE
import config


# declaring constants
# default parameters
slide_circum = 72  # [mm]
slide_step = 4  # micro step configuration
default_speed = 150  # [mm/s]

# blade dispensing parameters
dist2blade = 145  # [mm] ccw (towards end)
blade_neutral_duty = 2.6  # TEST AGAIN!!

# wick parameters
dist2wick = 12  # [mm] cw (towards home)
wick_speed = 90  # [mm/s]
wick_time = 3  # [sec]

# smear parameters
smear_dist = 45  # [mm] ccw (towards end)

# blade ejection parameters
eject_duty = 5

# fan parameters
dist2fan = 50 + smear_dist / 2  # [mm] cw (towards home)
dry_time = 20  # [sec] (optimal value: 150)


class Smear(Stepper, Digital_Io, Servo, Analog_In):

    def __init__(self, master, boot=0):
        # function: sets up pins for motors and sensors and initializes gui
        # master: variable name for gui window
        # boot: int 0 to declare start of program
        self.master = master
        pad = 3
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.title("Blood Smearing Device")
        self.boot = boot

        # initializing  classes and pins
        self.slide = Stepper(config.slide_pins, slide_circum, slide_step)
        self.home_switch = Digital_Io(
            config.limit_home_pin, "in")  # NEVER DELETE
        self.end_switch = Digital_Io(
            config.limit_end_pin, "in")  # NEVER DELETE
        self.linear = Servo(config.linear_pin)
        self.pulley = Servo(config.pulley_pin)
        self.rotate = Servo(config.rotation_pin, 180)
        self.fan = Digital_Io(config.fan_pin, "out", 0)
        self.force_pwr = Digital_Io(
            config.force_pins, "out", 0)  # NEVER DELETE
        self.force_sig = Analog_In(config.force_pins)  # NEVER DELETE

        # initializing pins
        self.rotate.start(1.98, 12.86, 50)
        self.rotate.update_duty(blade_neutral_duty)
        self.linear.start(10, 5, 50)
        self.linear.update_duty(10)
        self.pulley.start(0, 7.1, 50)
        self.pulley.update_duty(0)

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
        self.label_power_on.grid(row=0, columnspan=4, pady=70, padx=300)
        self.button_power_on = tk.Button(
            self.master, text="Okay", font=("Verdana Bold", 24))
        self.button_power_on.grid(row=1, columnspan=4, pady=30,
                                  padx=300, ipadx=20, ipady=15)

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

        self.label_slide = tk.Label(
            self.master, text="Please load slide with blood droplet", font=("Verdana Bold", 24))
        self.label_slide.grid(row=0, columnspan=4, pady=70, padx=300)
        self.button_slide = tk.Button(
            self.master, text="Okay", font=("Verdana Bold", 24), command=self.during_smear)
        self.button_slide.grid(row=1, columnspan=4, pady=30,
                               padx=300, ipadx=20, ipady=15)

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

    def smear_done(self):
        # function: outputs a window stating the smear is complete
        widget_list = self.active_widgets()
        for item in widget_list:
            item.grid_forget()

        self.label_done = tk.Label(
            self.master, text="Blood smear is complete", font=("Verdana Bold", 24))
        self.label_done.grid(row=0, columnspan=4, pady=70, padx=300)
        self.label_remove = tk.Label(
            self.master, text="Please remove slide", font=("Verdana Bold", 20))
        self.label_remove.grid(row=1, columnspan=4, pady=40, padx=300)
        self.label_continue = tk.Label(
            self.master, text="Do you want to make another blood smear", font=("Verdana Bold", 22))
        self.label_continue.grid(row=2, columnspan=4, pady=70, padx=300)
        self.button_another = tk.Button(
            self.master, text="Yes", font=("Verdana Bold", 24), command=self.start)
        self.button_another.grid(
            row=3, column=0, columnspan=2, ipady=15, ipadx=20, pady=30, padx=150)
        self.button_no = tk.Button(
            self.master, text="No", font=("Verdana Bold", 24), command=self.quit)
        self.button_no.grid(row=3, column=2, columnspan=2,
                            ipady=15, ipadx=20, pady=30, padx=150)

    def button_press(self, button):
        # function: checks which button is pressed and passes on linear speed
        # button: int number for button
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
        if self.boot == 0:
            self.power_on()
            self.boot += 1

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
        self.slide.enable_pulse()
        while self.home_switch.read() == 1:
            self.slide.move_steps(1, default_speed, "cw")
        self.slide.disable_pulse()

    def move2end(self):
        # function: move slide to linear guide end
        self.slide.enable_pulse()
        while self.end_switch.read() == 1:
            self.slide.move_steps(1, default_speed, "ccw")
        self.slide.disable_pulse()

    def blade(self, distance):
        # function: move to smearing blade extension site and extend blade
        # distance: float number of slide linear distance to smearing blade
        #           extension site [mm]
        self.slide.enable_pulse()
        self.slide.move_linear(distance, default_speed, "ccw")
        time.sleep(2)
        self.linear.update_duty(5)  # extended
        self.pulley.update_duty(7)  # slow speed
        while True:
            try:
                stop = str(input("\nPress enter to stop"))
            except ValueError:
                print("Error: Invalid Value")
                continue
            if stop == "":
                self.pulley.update_duty(0)  # off
                self.linear.update_duty(10)  # retracted
                break
            else:
                continue
        self.slide.disable_pulse()

    def wick(self, distance, wait_time, manual="no"):
        # function: move to wicking site and wait for wick to finish
        # distance: float number of slide linear distance to wicking site [mm]
        # wait_time: float number of time for blood to wick onto smearing
        #            blade [sec]
        # manual: by default "no" allows time to wick to be preselected
        #         ie. wait_time or
        #         "yes" for manual override
        self.slide.enable_pulse()
        self.slide.move_linear(distance, wick_speed, "cw")
        if manual == "no":
            time.sleep(wait_time)
        elif manual == "yes":
            input("\nPress any key after blood has wicked")
        else:
            print("\nError: Invalid string for manual")
            print("\"no\" to use preselected wicking wait time")
            print("\"yes\" to manually proceed after blood has visually wicked")
            print("Please use quotation marks")
        self.slide.disable_pulse()

    def smear(self, distance):
        # function: move slide for smear
        # distance: float number of slide linear distance for smear [mm]
        # mms_speed: float number of motor load's linear velocity [mm/s]
        self.slide.enable_pulse()
        rpm = self.slide.convert_mms2rpm(self.speed)
        self.slide.move_linear(distance, rpm, "ccw")
        self.time.sleep(2)
        self.slide.disable_pulse()

    def dry(self, distance, wait_time, manual="no"):
        # function: move slide to drying site and wait for blood to dry
        # distance: float number of slide linear distance after smear to
        #           heater [mm]
        # wait_time: float number for time to dry blood slide [sec]
        # manual: by default "no" allows time to dry to be preselected
        #         ie. wait_time or
        #         "yes" for manual override
        self.slide.enable_pulse()
        self.slide.move_linear(distance, default_speed, "cw")
        self.fan.output(1)  # on
        self.rotate.update_duty(eject_duty)  # turns ccw
        self.pulley.update_duty(5)  # on
        time.sleep(5)
        self.pulley.update_duty(0)  # off
        self.rotate.update_duty(blade_neutral_duty)
        if manual == "no":
            time.sleep(wait_time)
            self.fan.output(0)  # off
            print("Blood has dried")
        elif manual == "yes":
            input("\nPress any key after blood has dried")
            self.fan.output(0)  # off
            print("Blood has dried")
        else:
            print("\nError: Invalid string for manual")
            print("\"no\" to use preselected drying wait time")
            print("\"yes\" to manually proceed after blood has visually dried")
            print("Please use quotation marks")
        self.slide.disable_pulse()

    def main(self):
        # function: complete smearing process

        # moving slide to start position
        self.move2home()

        # moving slide to smearing station
        self.blade(dist2blade)

        # blood wicking interface
        self.wick(dist2wick, wick_time)

        # smearing blood
        self.smear(smear_dist)

        # drying blood
        self.dry(dist2fan, dry_time)

        # moving slide to unloading site
        self.move2home()

    def cleanup(self):
        # function: cleans up all used pins for motors and sensors
        self.slide.cleanup()
        self.home_switch.cleanup()  # NEVER DELETE
        self.end_switch.cleanup()  # NEVER DELETE
        self.linear.cleanup()
        self.pulley.cleanup()
        self.rotate.cleanup()
        self.fan.cleanup()


if __name__ == "__main__":

    # setting up gui window
    window = tk.Tk()
    smear = Smear(window)

    # complete smearing process
    smear.start()
    window.mainloop()
