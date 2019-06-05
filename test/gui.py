# gui.py
# This file declares a class to handle a graphical user interface


# importing libraries
import tkinter as tk
# import tkFont


# class GUI:

#     def __init__(self, window_name):
#         # window_name: sting input for window title name
#         self.window = tk.Tk()
#         window = self.window
#         window.title(window_name)

#     def start():

max_width = 732
max_height = 50
width1 = 120

# setting up window object
window = tk.Tk()
# setting window frame size
# frame = tk.Frame(window, width=732, height=50).grid()
frame1 = tk.Frame(window, width=width1,
                  height=max_height).grid(row=0, column=0)
frame2 = tk.Frame(window, width=max_width - width1,
                  height=max_height).grid(row=0, column=1)
# writing a title to the output window
window.title("Self Smearing Device")
# writing introduction text
label_intro = tk.Label(
    frame1, text="Please choose the Hematocrit level of your blood sample").grid(row=0, column=0, columnspan=2)
# writing text to introduce linear speed descriptions for different hematocrit levels
label_speed = tk.Label(
    frame1, text="Linear speeds for different Hematocrit levels").grid(row=1, column=1, sticky="W")
# making buttons for different hematocrit levels
button1 = tk.Button(frame1, text="Hematocrit 1").grid(
    row=2, column=0, ipady=5, ipadx=5, padx=10, pady=10, sticky="W")
button2 = tk.Button(frame1, text="Hematocrit 2").grid(
    row=3, column=0, ipady=5, ipadx=5, padx=10, pady=10, sticky="W")
button3 = tk.Button(frame1, text="Hematocrit 3").grid(
    row=4, column=0, ipady=5, ipadx=5, padx=10, pady=10, sticky="W")
button4 = tk.Button(frame1, text="Hematocrit 4").grid(
    row=5, column=0, ipady=5, ipadx=5, padx=10, pady=10, sticky="W")
button5 = tk.Button(frame1, text="Hematocrit 5").grid(
    row=6, column=0, ipady=5, ipadx=5, padx=10, pady=10, sticky="W")
button6 = tk.Button(frame1, text="Hematocrit 6").grid(
    row=7, column=0, ipady=5, ipadx=5, padx=10, pady=10, sticky="W")
button7 = tk.Button(frame1, text="Hematocrit 7").grid(
    row=8, column=0, ipady=5, ipadx=5, padx=10, pady=10, sticky="W")
button8 = tk.Button(frame1, text="Hematocrit 8").grid(
    row=9, column=0, ipady=5, ipadx=5, padx=10, pady=10, sticky="W")
# writing linear speed descriptions for each hematocrit level
text1 = tk.Label(
    frame1, text="180 mm/s").grid(row=2, column=1, sticky="W")
text2 = tk.Label(
    frame1, text="175 mm/s").grid(row=3, column=1, sticky="W")
text3 = tk.Label(
    frame1, text="165 mm/s").grid(row=4, column=1, sticky="W")
text4 = tk.Label(
    frame1, text="160 mm/s").grid(row=5, column=1, sticky="W")
text5 = tk.Label(
    frame1, text="155 mm/s").grid(row=6, column=1, sticky="W")
text6 = tk.Label(
    frame1, text="150 mm/s").grid(row=7, column=1, sticky="W")
text7 = tk.Label(
    frame1, text="120 mm/s").grid(row=8, column=1, sticky="W")
text8 = tk.Label(
    frame1, text="100 mm/s").grid(row=9, column=1, sticky="W")
# running gui
window.mainloop()
