import turtle
import pandas
from state_writer import StateWriter

# --- Screen Setup ---
screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# --- Initialization ---
writer = StateWriter()
data = pandas.read_csv("50_states.csv")  # Load state data
all_states = data.state.to_list()  # Create a list of all state names for validation
guessed_states = []  # Track user's correct guesses

# --- Game Loop ---
while len(guessed_states) < 50:
    # Prompt user for input
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    )

    # Handle Cancel/Close dialog
    if answer_state is None:
        break

    # Normalize input to Title Case (e.g., "new york" -> "New York")
    answer_state = answer_state.title()

    # --- Exit Condition ---
    # If user types "Exit", save missing states to a CSV and quit
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [
            state for state in all_states if state not in guessed_states
        ]  # revised missing_states logic using list comprehension learned Day 26!
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # --- Check Answer ---
    # If correct and not already guessed
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        # Retrieve row data for the state
        state_data = data[data.state == answer_state]
        # Write state name at coordinates found in CSV
        writer.write_state(
            answer_state, int(state_data.x.iloc[0]), int(state_data.y.iloc[0])
        )

screen.exitonclick()
