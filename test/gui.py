# gui.py
# This file declares a class to handle a graphical user interface


# importing libraries
import tkinter as tk


class GUI():
    def __init__(self, master, title):
        self.master = master
        pad = 3
        self._geom = '600x300+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)
        master.title(title)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

    def start(self):
        # writing introduction text
        label_intro = tk.Label(
            self.master, text="Please choose the Hematocrit level of your blood sample", font=("Verdana Bold", 18)).grid(row=0, columnspan=4, pady=5)
        # writing text to introduce linear speed descriptions for different hematocrit levels
        label_speed = tk.Label(
            # frame2, text="Linear speeds for different Hematocrit levels are listed below their respective buttons").pack(fill="x")
            self.master, text="Linear speeds for different Hematocrit levels are listed below their respective buttons", font=("Verdana Bold", 18)).grid(row=1, columnspan=4, pady=20)
        # making buttons for different hematocrit levels
        button1 = tk.Button(
            self.master, text="Hematocrit 1", font=("Verdana Bold", 18)).grid(row=2, column=0, ipady=15, ipadx=25, padx=15, pady=20)
        button2 = tk.Button(
            self.master, text="Hematocrit 2", font=("Verdana Bold", 18)).grid(row=2, column=1, ipady=15, ipadx=25, padx=15, pady=20)
        button3 = tk.Button(
            self.master, text="Hematocrit 3", font=("Verdana Bold", 18)).grid(row=2, column=2, ipady=15, ipadx=25, padx=15, pady=20)
        button4 = tk.Button(
            self.master, text="Hematocrit 4", font=("Verdana Bold", 18)).grid(row=2, column=3, ipady=15, ipadx=25, padx=15, pady=20)
        button5 = tk.Button(
            self.master, text="Hematocrit 5", font=("Verdana Bold", 18)).grid(row=4, column=0, ipady=15, ipadx=25, padx=15, pady=20)
        button6 = tk.Button(
            self.master, text="Hematocrit 6", font=("Verdana Bold", 18)).grid(row=4, column=1, ipady=15, ipadx=25, padx=15, pady=20)
        button7 = tk.Button(
            self.master, text="Hematocrit 7", font=("Verdana Bold", 18)).grid(row=4, column=2, ipady=15, ipadx=25, padx=15, pady=20)
        button8 = tk.Button(
            self.master, text="Hematocrit 8", font=("Verdana Bold", 18)).grid(row=4, column=3, ipady=15, ipadx=25, padx=15, pady=20)
        # writing linear speed descriptions for each hematocrit level
        text1 = tk.Label(
            self.master, text="180 mm/s", font=("Verdana Bold", 18)).grid(row=3, column=0)
        text2 = tk.Label(
            self.master, text="175 mm/s", font=("Verdana Bold", 18)).grid(row=3, column=1)
        text3 = tk.Label(
            self.master, text="165 mm/s", font=("Verdana Bold", 18)).grid(row=3, column=2)
        text4 = tk.Label(
            self.master, text="160 mm/s", font=("Verdana Bold", 18)).grid(row=3, column=3)
        text5 = tk.Label(
            self.master, text="155 mm/s", font=("Verdana Bold", 18)).grid(row=5, column=0)
        text6 = tk.Label(
            self.master, text="150 mm/s", font=("Verdana Bold", 18)).grid(row=5, column=1)
        text7 = tk.Label(
            self.master, text="120 mm/s", font=("Verdana Bold", 18)).grid(row=5, column=2)
        text8 = tk.Label(
            self.master, text="100 mm/s", font=("Verdana Bold", 18)).grid(row=5, column=3)
        # making a quit button
        quit_button = tk.Button(self.master, text="Quit", font=("Verdana Bold", 18)).grid(
            row=6, columnspan=4, ipady=15, ipadx=25, padx=20, pady=20)


root = tk.Tk()
app = GUI(root, "Blood Smear Device")
app.start()
root.mainloop()
