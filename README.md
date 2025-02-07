# Hangman Game 🎮

Welcome to the Hangman Game! This is a simple yet fun word-guessing game where you have to guess the hidden word letter by letter. You have a limited number of lives, so choose wisely! 🎯

## How to Play 🕹️

1. **Start the Game**: Run the script, and a random word will be selected for you to guess.
2. **Guess a Letter**: Enter a single letter to see if it exists in the hidden word.
3. **Win or Lose**: 
   - If you guess all the letters correctly before running out of lives, you win! 🎉
   - If you run out of lives before guessing the word, you lose. 😢
4. **Play Again**: After each game, you can choose to play again or exit.

## Features 🌟

- **Random Word Generation**: The game uses the `Faker` library to generate random words.
- **Life Count**: You start with 7 lives. The life count is displayed in blue if you have 4 or more lives, and in red if you have fewer than 4 lives.
- **Colorful Output**: The game uses `colorama` to add colors to the output, making it more visually appealing.
- **Interactive**: The game is interactive and prompts you to play again after each round.

## Requirements 📋

- Python 3.x
- `colorama` library
- `faker` library

You can install the required libraries using pip:

```bash
pip install colorama faker
