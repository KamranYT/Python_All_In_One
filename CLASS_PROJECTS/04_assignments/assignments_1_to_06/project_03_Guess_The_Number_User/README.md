# Guess The Number User

A Python-based number guessing game that offers two modes of play: user guessing and computer guessing. This interactive game provides an engaging way to practice number guessing with helpful feedback.

## Features

### 1. User Guessing Mode
- The computer generates a random number within a specified range
- User attempts to guess the number
- Provides feedback whether the guess is too high or too low
- Congratulates the user upon correct guess

### 2. Computer Guessing Mode
- User thinks of a number within a specified range
- Computer makes intelligent guesses based on user feedback
- User provides feedback (H for too high, L for too low, C for correct)
- Computer narrows down the range until it finds the correct number

## How to Play

### User Guessing Mode
1. Run the program
2. Enter your guess when prompted
3. Receive feedback if your guess is too high or too low
4. Continue guessing until you find the correct number

### Computer Guessing Mode
1. Think of a number between 1 and the specified range (currently set to 10)
2. Run the program
3. For each computer guess, provide feedback:
   - 'H' if the guess is too high
   - 'L' if the guess is too low
   - 'C' if the guess is correct
4. Watch as the computer narrows down your number

## Technical Details

- Written in Python
- Uses the `random` module for number generation
- Implements binary search-like algorithm in computer guessing mode
- Simple and intuitive user interface through console

## Requirements

- Python 3.x
- No additional dependencies required

## Usage

To run the game:
```bash
python main.py
```

## Future Improvements

- Add difficulty levels with different number ranges
- Implement a scoring system
- Add a graphical user interface
- Include statistics tracking
- Add option to switch between modes during gameplay
