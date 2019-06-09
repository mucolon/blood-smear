# test_gui.py
# This file declares a class to handle a graphical user interface
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_gui.py

# importing libraries
import tkinter as tk


class GUI():
    # class initialization for gui
    def __init__(self, master, boot=0):
        # master: variable name for gui window
        # boot: int 0 to declare start of program
        self.master = master
        pad = 3
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.title("Blood Smearing Device")
        self.boot = boot

    def active_widgets(self):
        # function: lists all active widgets in window
        # function return: list of all active widgets
        _list = self.master.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        return _list

    def quit_fun(self):
        print("Quit Function")

    def main_fun(self, var):
        print("var = ", str(var))

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
        self.quit_fun()
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
        self.main_fun(self.speed)
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


root = tk.Tk()
app = GUI(root)
app.start()
root.mainloop()
