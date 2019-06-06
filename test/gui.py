# gui.py
# This file declares a class to handle a graphical user interface


# importing libraries
import tkinter as tk


class GUI():
    def __init__(self, master):
        self.master = master
        pad = 3
        self._geom = '600x300+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

    def start(self):
        # writing introduction text
        label_intro = tk.Label(
            self.master, text="Please choose the Hematocrit level of your blood sample").grid(row=0, columnspan=4, pady=5)
        # writing text to introduce linear speed descriptions for different hematocrit levels
        label_speed = tk.Label(
            # frame2, text="Linear speeds for different Hematocrit levels are listed below their respective buttons").pack(fill="x")
            self.master, text="Linear speeds for different Hematocrit levels are listed below their respective buttons").grid(row=1, columnspan=4, pady=20)
        # making buttons for different hematocrit levels
        button1 = tk.Button(
            self.master, text="Hematocrit 1").grid(row=2, column=0, ipady=5, ipadx=5, padx=10, pady=10)
        button2 = tk.Button(
            self.master, text="Hematocrit 2").grid(row=2, column=1, ipady=5, ipadx=5, padx=10, pady=10)
        button3 = tk.Button(
            self.master, text="Hematocrit 3").grid(row=2, column=2, ipady=5, ipadx=5, padx=10, pady=10)
        button4 = tk.Button(
            self.master, text="Hematocrit 4").grid(row=2, column=3, ipady=5, ipadx=5, padx=10, pady=10)
        button5 = tk.Button(
            self.master, text="Hematocrit 5").grid(row=4, column=0, ipady=5, ipadx=5, padx=10, pady=10)
        button6 = tk.Button(
            self.master, text="Hematocrit 6").grid(row=4, column=1, ipady=5, ipadx=5, padx=10, pady=10)
        button7 = tk.Button(
            self.master, text="Hematocrit 7").grid(row=4, column=2, ipady=5, ipadx=5, padx=10, pady=10)
        button8 = tk.Button(
            self.master, text="Hematocrit 8").grid(row=4, column=3, ipady=5, ipadx=5, padx=10, pady=10)
        # writing linear speed descriptions for each hematocrit level
        text1 = tk.Label(
            self.master, text="180 mm/s").grid(row=3, column=0)
        text2 = tk.Label(
            self.master, text="175 mm/s").grid(row=3, column=1)
        text3 = tk.Label(
            self.master, text="165 mm/s").grid(row=3, column=2)
        text4 = tk.Label(
            self.master, text="160 mm/s").grid(row=3, column=3)
        text5 = tk.Label(
            self.master, text="155 mm/s").grid(row=5, column=0)
        text6 = tk.Label(
            self.master, text="150 mm/s").grid(row=5, column=1)
        text7 = tk.Label(
            self.master, text="120 mm/s").grid(row=5, column=2)
        text8 = tk.Label(
            self.master, text="100 mm/s").grid(row=5, column=3)


root = tk.Tk()
app = GUI(root)
app.start()
root.mainloop()
