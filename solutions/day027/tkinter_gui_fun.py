# import tkinter  # should come pre-installed with every python install, but if not use: python3 -m pip install tkinter
from tkinter import *  # this is the same as above, but makes it easier to change parameters without typing out tkinter.<parameter>

# window = tkinter.Tk() # see the above import changes
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # this is to add padding to the window

# Label
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold")) #see the above import changes
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()  # easiest way to pop the label in center of the window
my_label.pack(side="left")  # left, right, top, bottom
# above uses Advanced Python Arguments to specify a wider range of inputs
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

# with tkinter, you can name parameters at creation as above seen in my_label = ...
# or you can name OR update after creation using the dictionary element method
my_label["text"] = "New Text"
# and/or using the config method
my_label.config(text="New Text2")


# # Button
# def button_clicked():  # event listener
#     print("I got clicked")
#     my_label.config(text="My Button Got Clicked")


# Button
def button_clicked():  # event listener
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(
    text="Click Me", command=button_clicked
)  # when it's clicked, run the button_clicked function
button.pack()  # to display the button


# Entry field
input = Entry(width=10)
input.pack()
# input.get()  # returns the value of the entry field

window.mainloop()  # this is what keeps the window open on the screen
