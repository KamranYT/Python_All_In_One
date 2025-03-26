# Hangman Game

A classic word-guessing game implemented in Python where players try to guess a hidden word by suggesting letters. The game features a visual representation of the hangman and provides feedback on correct and incorrect guesses.

## Features

- Random word selection from a comprehensive word list
- Visual representation of the hangman using ASCII art
- Lives system (7 attempts to guess the word)
- Input validation for letters
- Tracking of used letters
- Clear feedback on correct and incorrect guesses
- Case-insensitive letter input

## How to Play

1. Run the game using Python:
   ```bash
   python main.py
   ```

2. The game will select a random word and display it as dashes (e.g., "W - R D")

3. You have 7 lives to guess the word. Each incorrect guess will:
   - Reduce your lives by 1
   - Add a part to the hangman visual
   - Show which letters you've already used

4. For each turn:
   - Enter a single letter (case doesn't matter)
   - If the letter is in the word, it will be revealed in all its positions
   - If the letter is not in the word, you lose a life
   - You cannot use the same letter twice

5. The game ends when either:
   - You successfully guess the word (win)
   - You run out of lives (lose)

## Project Structure

- `main.py`: Contains the main game logic
- `words.py`: Contains the list of words used in the game
- `hangman_visual.py`: Contains the ASCII art for the hangman visualization
- `count_words.py`: Utility script to count total words in the word list

## Word List

The game uses a comprehensive list of 2,643 words, including:
- Nouns
- Adjectives
- Verbs
- Common English words

## Example Game Flow

```
You have 7 lives left and you have used these letters: 

Current word: W - R D
Guess a letter: A

Your letter, A, is not in the word.

You have 6 lives left and you have used these letters: A
...
```

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the game using Python

## Contributing

Feel free to submit issues and enhancement requests!
