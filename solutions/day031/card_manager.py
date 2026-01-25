"""
Card Manager Module
Handles data loading, random card selection, and updating the known words list.
"""

import pandas as pd
import random

# Constants for file paths
DATA_FILE = "data/bra_pt_words.csv"
LEARN_FILE = "data/words_to_learn.csv"


class CardManager:
    """
    Manages the deck of flash cards using Pandas.
    """

    def __init__(self):
        """
        Initialize the CardManager.
        Tries to load words_to_learn.csv, otherwise falls back to bra_pt_words.csv.
        """
        self.to_learn = {}
        self.current_card = {}

        try:
            # Try to read the progress file
            data = pd.read_csv(LEARN_FILE)
        except FileNotFoundError:
            # If not found, read the original data
            try:
                original_data = pd.read_csv(DATA_FILE)
                self.to_learn = original_data.to_dict(orient="records")
            except FileNotFoundError:
                print(f"Error: {DATA_FILE} not found. Please ensure data exists.")
                self.to_learn = []
        else:
            # If progress file exists, use it
            self.to_learn = data.to_dict(orient="records")

    def get_next_card(self):
        """
        Selects a random card from the list of words to learn.
        :return: A dictionary representing the card (Portuguese, English) or None if empty.
        """
        if not self.to_learn:
            return None
        self.current_card = random.choice(self.to_learn)
        return self.current_card

    def is_known(self):
        """
        Removes the current card from the list of words to learn and saves the updated list to CSV.
        """
        if self.current_card in self.to_learn:
            self.to_learn.remove(self.current_card)

            # Save updated list to CSV
            data = pd.DataFrame(self.to_learn)
            data.to_csv(LEARN_FILE, index=False)
