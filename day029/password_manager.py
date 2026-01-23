from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import os
import traceback


# We use a class-based structure here to keep the state (window, entries) encapsulated.
# This makes it easier to manage the application lifecycle and access widgets across different methods.
class PasswordManager:
    def __init__(self):
        print("Starting application...")
        # Wrapping UI initialization in a try-except block is useful for debugging,
        # especially when dealing with external assets like images which might be missing or have incorrect paths.
        try:
            self.window = Tk()
            self.window.title("Password Manager")
            self.window.config(padx=50, pady=50)

            # Canvas allows us to layer images and text.
            self.canvas = Canvas(width=200, height=200)
            # Using os.path.join ensures the path works correctly across different operating systems (Windows vs Unix).
            # os.path.dirname(__file__) gets the directory where this script is located.
            image_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
            print(f"Loading image from: {image_path}")
            self.logo_img = PhotoImage(file=image_path)
            # The image is centered at (100, 100) because the canvas is 200x200.
            self.canvas.create_image(100, 100, image=self.logo_img)
            self.canvas.grid(row=0, column=1)

            # Labels
            self.website_label = Label(text="Website:")
            self.website_label.grid(row=1, column=0)
            self.email_label = Label(text="Email/Username:")
            self.email_label.grid(row=2, column=0)
            self.password_label = Label(text="Password:")
            self.password_label.grid(row=3, column=0)

            # Entries
            # 'width' sets the character width of the input field.
            self.website_entry = Entry(width=35)
            self.website_entry.grid(row=1, column=1, columnspan=2)
            # focus() puts the cursor in this field immediately when the app launches.
            self.website_entry.focus()

            self.email_entry = Entry(width=35)
            self.email_entry.grid(row=2, column=1, columnspan=2)
            # Pre-populating common fields improves user experience (UX). 0 indicates the insertion index (start).
            self.email_entry.insert(0, "rudil24@gmail.com")

            self.password_entry = Entry(width=21)
            self.password_entry.grid(row=3, column=1)

            # Buttons
            # The 'command' argument links the button click to a function (callback).
            # Note: We pass the function name 'self.generate_password' without parentheses '()'.
            self.generate_password_button = Button(
                text="Generate Password", command=self.generate_password
            )
            self.generate_password_button.grid(row=3, column=2)
            self.add_button = Button(text="Add", width=36, command=self.save)
            self.add_button.grid(row=4, column=1, columnspan=2)
        except Exception as e:
            # Catching generic Exception is usually discouraged in production logic,
            # but for top-level initialization debugging, it helps prevent silent failures.
            print(f"Error initializing app: {e}")
            traceback.print_exc()

    def generate_password(self):
        """Generates a strong random password and copies it to clipboard."""
        letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        # List comprehensions are a pythonic way to generate lists.
        password_letters = [random.choice(letters) for _ in range(nr_letters)]
        password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
        password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

        password_list = password_letters + password_symbols + password_numbers
        # Shuffle in place to ensure the pattern isn't predictable (e.g. always letters first).
        random.shuffle(password_list)

        password = "".join(password_list)

        # Clear the entry field before inserting the new password.
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)

        # UX improvement: Automatically copy to clipboard.
        pyperclip.copy(password)

    def save(self):
        """Validates inputs and saves the password to a file."""
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Validation: Ensure no fields are empty.
        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(
                title="Oops",
                message="Please make sure you haven't left any fields empty.",
            )
        else:
            # Confirmation dialog returns a boolean.
            is_ok = messagebox.askokcancel(
                title=website,
                message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?",
            )
            if is_ok:
                # Using 'with open(...)' is best practice for file handling.
                # It automatically closes the file even if an error occurs during writing.
                # mode "a" stands for append, so we don't overwrite existing data.
                with open("data.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")

                # Clear fields after saving for the next entry.
                self.website_entry.delete(0, END)
                self.password_entry.delete(0, END)

    def run(self):
        """Starts the Tkinter event loop."""
        # Check if window exists before running mainloop to avoid errors if init failed.
        if hasattr(self, "window"):
            self.window.mainloop()
