from tkinter import *


def miles_to_kilo():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("meter to KiloMeter")
window.minsize(width=800, height=500)

miles_input = Entry(width=30)
miles_input.grid(row=1, column=0)

miles_label = Label(text="Miles")
miles_label.grid(row=2, column=0)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(row=0, column=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(text="km")
kilometer_label.grid(row=2, column=1)

calculate_button = Button(text="calculate", command=miles_to_kilo)
calculate_button.grid(row=1, column=2)

window.mainloop()
