# gui.py
# This file declares a class to handle a graphical user interface


# importing libraries
import tkinter as tk
# import tkFont


# setting up window object
window = tk.Tk()
# setting window frame size
frame = tk.Frame(window, width=1024, height=600).grid()
# window.maxsize()
# writing a title to the output window
window.title("Self Smearing Device")
# writing introduction text
label_intro = tk.Label(
    window, text="Please choose the Hematocrit level of your blood sample").grid(row=0, column=0, columnspan=2)
# making buttons for different hematocrit levels
button1 = tk.Button(window, text="Hematocrit 1").grid(
    row=2, column=0, ipady=5, ipadx=5, padx=10, pady=10)
button2 = tk.Button(window, text="Hematocrit 2").grid(
    row=3, column=0, ipady=5, ipadx=5, pady=10)
button3 = tk.Button(window, text="Hematocrit 3").grid(
    row=4, column=0, ipady=5, ipadx=5, pady=10)
button4 = tk.Button(window, text="Hematocrit 4").grid(
    row=5, column=0, ipady=5, ipadx=5, pady=10)
button5 = tk.Button(window, text="Hematocrit 5").grid(
    row=6, column=0, ipady=5, ipadx=5, pady=10)
button6 = tk.Button(window, text="Hematocrit 6").grid(
    row=7, column=0, ipady=5, ipadx=5, pady=10)
button7 = tk.Button(window, text="Hematocrit 7").grid(
    row=8, column=0, ipady=5, ipadx=5, pady=10)
button8 = tk.Button(window, text="Hematocrit 8").grid(
    row=9, column=0, ipady=5, ipadx=5, pady=10)
# writing text to introduce linear speed descriptions
label_speed = tk.Label(
    window, text="Linear speeds for different Hematocrit levels").grid(row=1, column=1)
# writing linear speed descriptions for each hematocrit level
text1 = tk.Label(
    window, text="180 mm/s").grid(row=2, column=1, sticky="W")
text2 = tk.Label(
    window, text="175 mm/s").grid(row=3, column=1, sticky="W")
text3 = tk.Label(
    window, text="165 mm/s").grid(row=4, column=1, sticky="W")
text4 = tk.Label(
    window, text="160 mm/s").grid(row=5, column=1, sticky="W")
text5 = tk.Label(
    window, text="155 mm/s").grid(row=6, column=1, sticky="W")
text6 = tk.Label(
    window, text="150 mm/s").grid(row=7, column=1, sticky="W")
text7 = tk.Label(
    window, text="120 mm/s").grid(row=8, column=1, sticky="W")
text8 = tk.Label(
    window, text="100 mm/s").grid(row=9, column=1, sticky="W")


window.mainloop()
