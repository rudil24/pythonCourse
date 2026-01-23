# rudil24
# Day 27: Miles to Kilometers Converter
from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# Label 1
miles = Label(text="Miles")
miles.grid(column=2, row=0)

# Label 2
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

# Label 3
result = Label(text="0")
result.grid(column=1, row=1)

# Label 4
kilometers = Label(text="Km")
kilometers.grid(column=2, row=1)


# Button
def button_clicked():
    miles = float(input.get())
    kms = round(miles * 1.60934, 2)
    result.config(text=kms)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
