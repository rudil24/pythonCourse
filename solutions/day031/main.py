"""
Main Entry Point for Flashy
Language Flash Cards Application
"""

from flash_card_ui import FlashCardUI
from card_manager import CardManager


def main():
    """
    Orchestrates the application startup.
    """
    # Initialize the Data Manager
    card_manager = CardManager()

    # Initialize and run the UI
    FlashCardUI(card_manager)


if __name__ == "__main__":
    main()
