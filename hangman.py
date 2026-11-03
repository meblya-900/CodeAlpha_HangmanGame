"""
Hangman Game
============
A text-based Hangman game that runs entirely in the terminal.

Created for the CodeAlpha Python Programming Internship.
Uses only Python's standard library (no external dependencies).
"""

import random
import string

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
MAX_INCORRECT_ATTEMPTS = 6
HIDDEN_LETTER_SYMBOL = "_"
SEPARATOR_LINE = "=" * 50

# Predefined words grouped by category (12 words in total).
WORD_BANK = {
    "Animals": ["elephant", "giraffe", "dolphin"],
    "Fruits": ["banana", "mango", "pineapple"],
    "Countries": ["zambia", "brazil", "canada"],
    "Programming": ["python", "variable", "function"],
}

# ASCII art for every stage of the game (Stage 0 to Stage 6).
HANGMAN_STAGES = [
    # Stage 0: no mistakes yet
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    # Stage 1: head
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    # Stage 2: body
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    # Stage 3: left arm
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    # Stage 4: right arm
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    # Stage 5: left leg
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    # Stage 6: right leg (game over)
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]


# ---------------------------------------------------------------------------
# Game setup
# ---------------------------------------------------------------------------
def choose_word(word_bank):
    """
    Randomly choose a category and a word from the word bank.

    Args:
        word_bank (dict): Maps category names to lists of words.

    Returns:
        tuple: (category, word) where the word is in uppercase.
    """
    category = random.choice(list(word_bank.keys()))
    word = random.choice(word_bank[category])
    return category, word.upper()


def create_game_state(category, secret_word):
    """
    Create a dictionary that stores everything about the current game.

    Keeping the data in one dictionary avoids global variables.

    Args:
        category (str): The category of the secret word.
        secret_word (str): The word the player must guess (uppercase).

    Returns:
        dict: The initial game state.
    """
    return {
        "category": category,
        "secret_word": secret_word,
        "correct_letters": set(),
        "wrong_letters": set(),
    }


# ---------------------------------------------------------------------------
# Game state helpers
# ---------------------------------------------------------------------------
def get_guessed_letters(game_state):
    """
    Return every letter guessed so far (correct and wrong combined).

    Args:
        game_state (dict): The current game state.

    Returns:
        set: All guessed letters.
    """
    return game_state["correct_letters"] | game_state["wrong_letters"]


def get_remaining_attempts(game_state):
    """
    Calculate how many incorrect guesses the player has left.

    Args:
        game_state (dict): The current game state.

    Returns:
        int: Remaining incorrect attempts.
    """
    return MAX_INCORRECT_ATTEMPTS - len(game_state["wrong_letters"])


def get_hidden_word(game_state):
    """
    Build the word display, revealing only correctly guessed letters.

    Example: "PYTHON" with P, T and O guessed becomes "P _ T _ O _".

    Args:
        game_state (dict): The current game state.

    Returns:
        str: The partially hidden word with spaces between characters.
    """
    display_letters = []
    for letter in game_state["secret_word"]:
        if letter in game_state["correct_letters"]:
            display_letters.append(letter)
        else:
            display_letters.append(HIDDEN_LETTER_SYMBOL)
    return " ".join(display_letters)


def is_word_guessed(game_state):
    """
    Check whether the player has revealed every letter of the word.

    Args:
        game_state (dict): The current game state.

    Returns:
        bool: True if all letters have been guessed, otherwise False.
    """
    secret_letters = set(game_state["secret_word"])
    return secret_letters.issubset(game_state["correct_letters"])


def is_game_lost(game_state):
    """
    Check whether the player has run out of attempts.

    Args:
        game_state (dict): The current game state.

    Returns:
        bool: True if no attempts remain, otherwise False.
    """
    return get_remaining_attempts(game_state) <= 0


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------
def draw_hangman(wrong_guess_count):
    """
    Print the ASCII hangman picture for the given number of mistakes.

    Args:
        wrong_guess_count (int): Number of incorrect guesses (0 to 6).
    """
    stage_index = min(wrong_guess_count, len(HANGMAN_STAGES) - 1)
    print(HANGMAN_STAGES[stage_index])


def format_letters(letters):
    """
    Convert a set of letters into a sorted, readable string.

    Args:
        letters (set): A set of letters.

    Returns:
        str: Letters separated by spaces, or "None" if the set is empty.
    """
    if not letters:
        return "None"
    return " ".join(sorted(letters))


def display_game(game_state):
    """
    Show the full game screen to the player.

    Displays the hangman drawing, the hidden word, remaining attempts,
    wrong letters, correct letters and all letters already guessed.

    Args:
        game_state (dict): The current game state.
    """
    print(f"\n{SEPARATOR_LINE}")
    draw_hangman(len(game_state["wrong_letters"]))
    print(f"Category           : {game_state['category']}")
    print(f"Word               : {get_hidden_word(game_state)}")
    print(f"Remaining attempts : {get_remaining_attempts(game_state)}")
    print(f"Wrong letters      : {format_letters(game_state['wrong_letters'])}")
    print(f"Correct letters    : {format_letters(game_state['correct_letters'])}")
    print(f"Letters guessed    : {format_letters(get_guessed_letters(game_state))}")
    print(SEPARATOR_LINE)


# ---------------------------------------------------------------------------
# Input handling
# ---------------------------------------------------------------------------
def validate_guess(raw_input_text, guessed_letters):
    """
    Check whether the player's input is a valid guess.

    Args:
        raw_input_text (str): Text typed by the player.
        guessed_letters (set): Letters that were already guessed.

    Returns:
        str or None: An error message if invalid, or None if valid.
    """
    guess = raw_input_text.strip()

    if not guess:
        return "Input cannot be empty. Please enter a letter."
    if len(guess) > 1:
        return "Please enter only ONE letter at a time."
    if guess.isdigit():
        return "Numbers are not allowed. Please enter a letter (A-Z)."
    if guess.upper() not in string.ascii_uppercase:
        return "Symbols are not allowed. Please enter a letter (A-Z)."
    if guess.upper() in guessed_letters:
        return f"You already guessed '{guess.upper()}'. Try a different letter."

    return None


def get_guess(guessed_letters):
    """
    Keep asking the player for a guess until a valid one is entered.

    Args:
        guessed_letters (set): Letters that were already guessed.

    Returns:
        str: A valid guess as an uppercase letter.
    """
    while True:
        raw_input_text = input("Guess a letter: ")
        error_message = validate_guess(raw_input_text, guessed_letters)

        if error_message is None:
            return raw_input_text.strip().upper()

        print(f"  [!] {error_message}")


def ask_play_again():
    """
    Ask the player whether they want to play another round.

    Returns:
        bool: True if the player answers Y, False if the answer is N.
    """
    while True:
        answer = input("\nPlay again? (Y/N): ").strip().upper()

        if answer == "Y":
            return True
        if answer == "N":
            return False

        print("  [!] Please enter Y for Yes or N for No.")


# ---------------------------------------------------------------------------
# Game logic
# ---------------------------------------------------------------------------
def update_game(game_state, guess):
    """
    Apply a guess to the game state and report the result.

    Args:
        game_state (dict): The current game state (modified in place).
        guess (str): A validated uppercase letter.

    Returns:
        bool: True if the guess is in the secret word, otherwise False.
    """
    if guess in game_state["secret_word"]:
        game_state["correct_letters"].add(guess)
        return True

    game_state["wrong_letters"].add(guess)
    return False


def show_result(game_state):
    """
    Display the final win or lose message.

    Args:
        game_state (dict): The finished game state.
    """
    display_game(game_state)

    if is_word_guessed(game_state):
        print("\n*** CONGRATULATIONS! YOU WON! ***")
        print(f"You correctly guessed the word: {game_state['secret_word']}")
    else:
        print("\n*** GAME OVER - YOU LOST ***")
        print(f"The word was: {game_state['secret_word']}")
        print("Better luck next time!")


def play_game():
    """
    Play one complete round of Hangman.

    Chooses a word, then loops through guesses until the player
    wins or runs out of attempts.
    """
    category, secret_word = choose_word(WORD_BANK)
    game_state = create_game_state(category, secret_word)

    while not is_word_guessed(game_state) and not is_game_lost(game_state):
        display_game(game_state)
        guess = get_guess(get_guessed_letters(game_state))

        if update_game(game_state, guess):
            print(f"\nGood job! '{guess}' is in the word.")
        else:
            print(f"\nSorry, '{guess}' is not in the word.")

    show_result(game_state)


def main():
    """
    Run the Hangman program: welcome the player and handle replays.
    """
    print(SEPARATOR_LINE)
    print("        WELCOME TO HANGMAN")
    print(SEPARATOR_LINE)
    print(f"Guess the secret word one letter at a time.")
    print(f"You are allowed {MAX_INCORRECT_ATTEMPTS} incorrect attempts.")

    try:
        keep_playing = True
        while keep_playing:
            play_game()
            keep_playing = ask_play_again()
    except (KeyboardInterrupt, EOFError):
        # Handles Ctrl+C or Ctrl+Z gracefully instead of showing a traceback.
        print("\n\nGame interrupted.")

    print("\nThanks for playing Hangman. Goodbye!")


if __name__ == "__main__":
    main()