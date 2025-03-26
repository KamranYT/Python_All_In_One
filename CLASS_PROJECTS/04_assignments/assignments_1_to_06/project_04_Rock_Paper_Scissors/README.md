# Rock Paper Scissors Game

A simple and interactive command-line implementation of the classic Rock Paper Scissors game in Python.

## Overview

This project implements a text-based version of the popular Rock Paper Scissors game where the player competes against the computer. The game features a clean, user-friendly interface and follows the traditional rules of Rock Paper Scissors.

## Features

- Player vs Computer gameplay
- Simple command-line interface
- Random computer choice generation
- Clear win/lose/tie outcomes
- Input validation for player choices

## How to Play

1. Run the program using Python:
   ```bash
   python main.py
   ```

2. When prompted, enter your choice using the following letters:
   - 'r' for Rock
   - 'p' for Paper
   - 's' for Scissors

3. The computer will randomly select its choice, and the result will be displayed:
   - "You won!" if you beat the computer
   - "You lost!" if the computer beats you
   - "It's a tie" if both choices are the same

## Game Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

## Technical Details

The project is implemented in Python and uses the following features:
- Random choice generation using the `random` module
- Function-based architecture for clean code organization
- Simple conditional logic for determining the winner

## Requirements

- Python 3.x

## File Structure

- `main.py`: Contains the main game logic and user interaction
