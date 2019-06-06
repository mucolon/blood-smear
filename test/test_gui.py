# test_gui.py
# This file declares a class to handle a graphical user interface
#
# run program with this line of code below form home directory (/~)
# sudo python3 blood-smear/test/test_gui.py

# importing libraries
import tkinter as tk
import tkinter.messagebox as tkm


class GUI():
    # class initialization for gui
    def __init__(self, master):
        # master: variable name for gui window
        # title: string title name for gui window
        self.master = master
        pad = 3
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.title("Blood Smearing Device")
        self.boot = 0

    def quit_fun(self):
        print("Quit Function")

    def main_fun(self, var):
        print("var = ", str(var))

    def power_on(self):
        # function: outputs alert window to turn on motor switch
        tkm.showinfo("Alert Message", "Please flip switch on")

    def power_off(self):
        # function: outputs alert window to turn off motor switch
        tkm.showinfo("Alert Message", "Please flip switch off")

    def quit(self):
        # function: quit and exit program
        self.quit_fun()
        self.power_off()
        self.master.destroy()

    def load_slide(self):
        # function: outputs alert window to load slide
        tkm.showinfo("Alert Message", "Please load slide with blood droplet")

    def during_smear(self):
        # function: outputs a window during smearing process
        self.label_intro.grid_forget()
        self.label_speed.grid_forget()
        self.button1.grid_forget()
        self.button2.grid_forget()
        self.button3.grid_forget()
        self.button4.grid_forget()
        self.button5.grid_forget()
        self.button6.grid_forget()
        self.button7.grid_forget()
        self.button8.grid_forget()
        self.text1.grid_forget()
        self.text2.grid_forget()
        self.text3.grid_forget()
        self.text4.grid_forget()
        self.text5.grid_forget()
        self.text6.grid_forget()
        self.text7.grid_forget()
        self.text8.grid_forget()
        self.quit_button.grid_forget()
        self.label_smear = tk.Label(
            self.master, text="Blood smear in progress", font=("Verdana Bold", 24))
        self.label_smear.grid(row=0, columnspan=4, pady=30, padx=70)
        self.emergency_button = tk.Button(
            self.master, text="Emergency Shutoff", font=("Verdana Bold", 24), command=self.quit)
        self.emergency_button.grid(row=1, columnspan=4, pady=30,
                                   padx=70, ipadx=20, ipady=15)

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
        self.load_slide()
        self.during_smear()

    def start(self):
        # function: displays start screen for device
        if self.boot >= 1:
            self.label_smear.grid_forget()
            self.emergency_button.grid_forget()
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
            "Verdana Bold", 18), command=lambda: self.button_press(1))
        self.button1.grid(row=2, column=0, ipady=15,
                          ipadx=25, padx=15, pady=20)
        self.button2 = tk.Button(self.master, text="20-25%",
                                 font=("Verdana Bold", 18), command=lambda: self.button_press(2))
        self.button2.grid(row=2, column=1, ipady=15,
                          ipadx=20, padx=15, pady=20)
        self.button3 = tk.Button(self.master, text="25-30%",
                                 font=("Verdana Bold", 18), command=lambda: self.button_press(3))
        self.button3.grid(row=2, column=2, ipady=15,
                          ipadx=20, padx=15, pady=20)
        self.button4 = tk.Button(self.master, text="30-35%",
                                 font=("Verdana Bold", 18), command=lambda: self.button_press(4))
        self.button4.grid(row=2, column=3, ipady=15,
                          ipadx=20, padx=15, pady=20)
        self.button5 = tk.Button(self.master, text="35-40%",
                                 font=("Verdana Bold", 18), command=lambda: self.button_press(5))
        self.button5.grid(row=4, column=0, ipady=15,
                          ipadx=20, padx=15, pady=20)
        self.button6 = tk.Button(self.master, text="40-45%",
                                 font=("Verdana Bold", 18), command=lambda: self.button_press(6))
        self.button6.grid(row=4, column=1, ipady=15,
                          ipadx=20, padx=15, pady=20)
        self.button7 = tk.Button(self.master, text="45-50%",
                                 font=("Verdana Bold", 18), command=lambda: self.button_press(7))
        self.button7.grid(row=4, column=2, ipady=15,
                          ipadx=20, padx=15, pady=20)
        self.button8 = tk.Button(self.master, text="> 50%", font=(
            "Verdana Bold", 18), command=lambda: self.button_press(8))
        self.button8.grid(row=4, column=3, ipady=15,
                          ipadx=25, padx=15, pady=20)

        # writing linear speed descriptions for each hematocrit percentage range
        self.text1 = tk.Label(self.master, text="180 mm/s",
                              font=("Verdana Bold", 18))
        self.text1.grid(row=3, column=0)
        self.text2 = tk.Label(self.master, text="175 mm/s",
                              font=("Verdana Bold", 18))
        self.text2.grid(row=3, column=1)
        self.text3 = tk.Label(self.master, text="165 mm/s",
                              font=("Verdana Bold", 18))
        self.text3.grid(row=3, column=2)
        self.text4 = tk.Label(self.master, text="160 mm/s",
                              font=("Verdana Bold", 18))
        self.text4.grid(row=3, column=3)
        self.text5 = tk.Label(self.master, text="155 mm/s",
                              font=("Verdana Bold", 18))
        self.text5.grid(row=5, column=0)
        self.text6 = tk.Label(self.master, text="150 mm/s",
                              font=("Verdana Bold", 18))
        self.text6.grid(row=5, column=1)
        self.text7 = tk.Label(self.master, text="120 mm/s",
                              font=("Verdana Bold", 18))
        self.text7.grid(row=5, column=2)
        self.text8 = tk.Label(self.master, text="100 mm/s",
                              font=("Verdana Bold", 18))
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
