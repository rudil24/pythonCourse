import tkinter as tk  # i think this is a happy medium of how to import it, so you can use shorthand tk without blindly just naming classes like from tkinter import * does


# you can render tkinter items using pack, place, and grid
# pack: puts the item in the center of the window by default, no padding, and packs the next item below it
# place: puts the item at a specific location
# grid: puts the item in a grid

window = tk.Tk()
window.title("My Second GUI Program")
window.minsize(width=500, height=300)
window.config(
    padx=20, pady=20
)  # this is to add invisible padding inside the outside edges of the window

# Label
my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack() # easiest way to pop the label in center of the window
# my_label.place(x=100, y=65)   # 100 pixels from the left, 65 pixels from the top
my_label.grid(column=0, row=0)  # 0,0 is top left. CAREFUL, you can't mix pack and grid
my_label.config(padx=50, pady=50)  # adds 50px of padding to the outer edge of the label


# Button
def action():
    print("Do something")


# calls action() when pressed
button = tk.Button(text="Click Me", command=action)
button.grid(column=1, row=1)

# Entries
entry = tk.Entry(width=30)
# Add some text to begin with
entry.insert(tk.END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.grid(column=3, row=2)

# Button 2
button2 = tk.Button(text="Click Me2", command=action)
button2.grid(column=2, row=0)

window.mainloop()  # this is what keeps the window open on the screen
