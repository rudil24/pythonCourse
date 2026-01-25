"""
Flash Card UI Module
Handles the Tkinter User Interface for the Flash Card application.
"""

from tkinter import *
from card_manager import CardManager

# Constants
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"


class FlashCardUI:
    """
    The main UI class for the Flash Card application.
    """

    def __init__(self, card_manager: CardManager):
        """
        Initialize the UI.
        :param card_manager: An instance of CardManager to handle data logic.
        """
        self.manager = card_manager
        self.window = Tk()
        self.window.title("Flashy - Brazilian Portuguese")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.flip_timer = None
        self.current_card = {}

        # --- Canvas Setup ---
        self.canvas = Canvas(width=800, height=526)

        # Load Images
        # Note: Keeping references to PhotoImages is crucial to prevent garbage collection
        try:
            self.card_front_img = PhotoImage(file="assets/card_front.png")
            self.card_back_img = PhotoImage(file="assets/card_back.png")
            self.cross_image = PhotoImage(file="assets/wrong.png")
            self.check_image = PhotoImage(file="assets/right.png")
        except TclError:
            print(
                "Error: Assets not found. Please ensure ./assets/ contains the required images."
            )
            return

        self.card_background = self.canvas.create_image(
            400, 263, image=self.card_front_img
        )
        self.card_title = self.canvas.create_text(
            400, 150, text="", font=(FONT_NAME, 40, "italic")
        )
        self.card_word = self.canvas.create_text(
            400, 263, text="", font=(FONT_NAME, 60, "bold")
        )

        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # --- Buttons ---
        self.unknown_button = Button(
            image=self.cross_image, highlightthickness=0, command=self.next_card
        )
        self.unknown_button.grid(row=1, column=0)

        self.known_button = Button(
            image=self.check_image, highlightthickness=0, command=self.is_known
        )
        self.known_button.grid(row=1, column=1)

        # Initial call to start the game
        self.next_card()

        # Start the main loop
        self.window.mainloop()

    def next_card(self):
        """
        Displays the next random card (Front side).
        Resets the timer for flipping the card.
        """
        # Cancel existing timer if user clicks quickly
        if self.flip_timer:
            self.window.after_cancel(self.flip_timer)

        self.current_card = self.manager.get_next_card()

        if self.current_card:
            # Update UI for Front of Card
            self.canvas.itemconfig(self.card_title, text="Portuguese", fill="black")
            self.canvas.itemconfig(
                self.card_word, text=self.current_card["Portuguese"], fill="black"
            )
            self.canvas.itemconfig(self.card_background, image=self.card_front_img)

            # Set timer to flip card after 3 seconds (3000ms)
            self.flip_timer = self.window.after(3000, func=self.flip_card)
        else:
            # No more cards
            self.canvas.itemconfig(self.card_title, text="Done!", fill="black")
            self.canvas.itemconfig(
                self.card_word, text="You've learned all words!", fill="black"
            )
            self.known_button.config(state="disabled")
            self.unknown_button.config(state="disabled")

    def flip_card(self):
        """
        Flips the card to show the English translation (Back side).
        """
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(
            self.card_word, text=self.current_card["English"], fill="white"
        )
        self.canvas.itemconfig(self.card_background, image=self.card_back_img)

    def is_known(self):
        """
        Handler for the 'Right' (Check) button.
        Marks card as known in manager and proceeds to next card.
        """
        self.manager.is_known()
        self.next_card()
