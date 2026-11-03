# CodeAlpha Hangman Game

A clean, beginner-friendly, text-based Hangman game written in Python 3 and played entirely in the terminal.

## Project Overview

This project was built for the **CodeAlpha Python Programming Internship**. The player guesses a secret word one letter at a time. Each wrong guess adds a part to the hangman drawing, and the player loses after **6 incorrect attempts**. The program uses only Python's standard library, so there is nothing extra to install.

## Screenshots

### Welcome Screen

![Welcome](screenshots/welcome.png)

### Gameplay

![Gameplay](screenshots/gameplay.png)

### CONGRATULATIONS! YOU WON!

![Youwon](screenshots/you-won.png)
## Features

- 12 predefined words in 4 categories (Animals, Fruits, Countries, Programming)
- Random word selection with the `random` module
- Exactly 6 incorrect attempts allowed
- Live display of:
  - The hidden word (for example, `P _ T H O N`)
  - Remaining attempts
  - Wrong letters
  - Correct letters
  - All letters already guessed
- Input validation with helpful error messages for:
  - Empty input
  - Numbers
  - Symbols
  - More than one character
  - Duplicate guesses
- ASCII hangman graphics for all 7 stages (Stage 0 to Stage 6)
- Win and lose detection with clear messages
- "Play again? (Y/N)" prompt and graceful exit
- Handles `Ctrl+C` without showing an error traceback

## Project Structure

```text
CodeAlpha_HangmanGame/
├── hangman.py          # Main game source code
├── README.md           # Project documentation
└── requirements.txt    # Dependency note (none required)
│
└── screenshots
      ├── welcome.png
      └── gameplay.png
```

## How to Install

1. Install **Python 3.8 or newer** from https://www.python.org/downloads/
2. Verify the installation in PowerShell:

```powershell
python --version
```

3. Download or clone this project, then open PowerShell in the project folder:

```powershell
cd CodeAlpha_HangmanGame
```

No `pip install` is needed because the game uses only the standard library.

## How to Run

```powershell
python hangman.py
```

## Example Gameplay

```text
==================================================
        WELCOME TO HANGMAN
==================================================
Guess the secret word one letter at a time.
You are allowed 6 incorrect attempts.

==================================================

  +---+
  |   |
      |
      |
      |
      |
=========

Category           : Programming
Word               : _ _ _ _ _ _
Remaining attempts : 6
Wrong letters      : None
Correct letters    : None
Letters guessed    : None
==================================================
Guess a letter: p

Good job! 'P' is in the word.

==================================================

  +---+
  |   |
      |
      |
      |
      |
=========

Category           : Programming
Word               : P _ _ _ _ _
Remaining attempts : 6
Wrong letters      : None
Correct letters    : P
Letters guessed    : P
==================================================
Guess a letter: 7
  [!] Numbers are not allowed. Please enter a letter (A-Z).
Guess a letter: z

Sorry, 'Z' is not in the word.
```

## Python Concepts Used

- Functions and docstrings
- Constants and naming conventions (PEP 8)
- Lists, dictionaries, sets and tuples
- String methods (`strip`, `upper`, `isdigit`, `join`)
- The `random` and `string` modules
- `while` loops and conditional logic
- Input validation and error handling
- `try` / `except` for graceful exit
- Passing a state dictionary to functions instead of using global variables
- The `if __name__ == "__main__"` entry point

## Future Improvements

- Let the player choose a category and difficulty level
- Load words from an external text file
- Add a hint feature
- Track scores and win/loss statistics across rounds
- Add a two-player mode
- Support colored terminal output
- Add unit tests with `unittest`

## Author

**MEWARD BWALYA**
CodeAlpha Python Programming Intern
Email: mewardb@gmail.com