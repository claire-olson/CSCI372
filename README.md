# CSCI372
Final Project
# Hangman Game Project

## Overview
This project is a Python-based implementation of the classic Hangman game, a fun and educational word-guessing game. Players attempt to guess a randomly selected word by suggesting letters, with a limited number of incorrect guesses allowed. This project showcases the use of Python's libraries for creating an interactive game and leverages Pygame for handling the graphical interface and real-time input.

Hangman is designed to improve vocabulary, spelling, and logical thinking, making it enjoyable and educational for players of all ages.

## Features
### 1. **Word Selection**
   - Randomly selects a word from predefined categories, with an option for different difficulty levels.
   - Categories include animals, fruits, countries, and sports.

### 2. **Gameplay Mechanics**
   - **Masked Word Display:** Shows blank spaces representing each letter in the word. Correct guesses reveal the corresponding letters.
   - **Input Validation:** Checks user inputs to handle invalid entries, repeated guesses, and real-time interactions.
   - **Lives Display:** Reduces available lives with each incorrect guess and shows the hangman figure progressing.

### 3. **Win/Loss Conditions**
   - The player wins by guessing all the letters in the word before running out of lives.
   - The game ends in a loss if all guesses are used up before solving the word, and the word is revealed.

### 4. **Scoring System**
   - Points are awarded for correct guesses and deducted for incorrect guesses.
   - Displays a real-time score that tracks performance across games.

## Libraries and Technologies
- **Python**: The core programming language used for logic, control flow, and structure.
- **Pygame**: Provides graphical interface capabilities, real-time input handling, and smooth gameplay mechanics.
- **Random**: Selects a random word from predefined categories.
- **Sys**: Handles program termination and system exit.

## Getting Started
### Prerequisites
1. Python 3.x installed on your computer.
2. Pygame library (`pip install pygame`).

### Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hangman-game.git
   cd hangman-game
2. Install
   pip install pygame
3. Run
   python hangman.py



## Structure
hangman-game/
│
├── hangman.py            # Main game script
├── README.md             # Project documentation
├── images/               # Folder containing hangman images for each wrong attempt


