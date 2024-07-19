# Battleship Game

Welcome to the Battleship game! This README provides an overview of the code for a simple two-player Battleship game where one player competes against the computer.

## Table of Contents

1. [Overview](#overview)
2. [How to Play](#how-to-play)
3. [Features](#features)
4. [Bug Fixes](#bug-fixes)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)

## Overview

This Python script implements a basic console-based Battleship game. The game is played by trying to guess the locations of their opponent's ships. The game includes functionalities for:

- Initializing the game and giving the player the option to choose the size of the grid and number of ships.
- Randomly populating the board with ships.
- Making random guesses for the computer.
- Handling game turns for both player and computer.
- Keeping track of scores and allowing multiple games.
- Resetting the scores as well as requesting a new player name.

## How to Play

1. **Start the Game**: Run the script. You will be prompted to enter your name.
2. **Configure Game Settings**: Specify the size of the board and the number of ships.
3. **Play the Game**:
   - **Player's Turn**: Enter coordinates to guess the location of the computer's ships.
   - **Computer's Turn**: The computer will make random guesses.
4. **Win/Loss**: The game continues until all ships on one board are sunk.
5. **Play Again**: After a game ends, you can choose to play another game or exit. Optionally, reset scores and the name of the player.

## Features

### 1. **Dynamic Board Setup**

- **Customizable Board Size**: Players can specify the size of the game board, allowing for different levels of difficulty and gameplay experience.
- **Adjustable Number of Ships**: Players choose the number of ships to be placed on the board, adding variability to each game.

### 2. **Interactive Gameplay**

- **Player vs. Computer**: Compete against a computer opponent with randomly generated guesses, providing a challenging experience.
- **Real-Time Feedback**: The game provides immediate feedback on each guess, indicating whether it was a "HIT!!" or a "Miss!".
- **Turn-Based System**: Alternates turns between the player and the computer, simulating a realistic game flow.

### 3. **Game Status and End Conditions**

- **Winning and Losing Conditions**: The game detects when either the player or the computer has sunk all the opponent's ships, declaring a win or loss accordingly.
- **Score Tracking**: Maintains a score for both the player and the computer, with the ability to update scores based on game outcomes.
- **Play Again Option**: After a game ends, players can choose to start a new game without restarting the script.
- **Score Reset**: Players can opt to reset scores, allowing for a fresh start and the option to enter a new name.

### 4. **Randomized Ship Placement and Computer Guessing**

- **Random Ship Placement**: Ships are placed randomly on the board, ensuring that each game is unique.
- **Random Computer Guesses**: The computer makes random guesses, adding an element of unpredictability to the game.

### 5. **Input Validation and Error Checking**

**Board Size Validation**:
- **Validation**: The board size must be an integer greater than or equal to 2.
- **Error Handling**: If the input is not a valid integer or is less than 2, the user is prompted to enter a valid board size.

**Duplicate Guesses**:
- **Validation**: Ensure that the player does not guess the same coordinates more than once.
- **Error Handling**: If the coordinates have already been guessed, the player is informed and prompted to enter a new guess.

**Guesses Outside the Grid of the Board**:
- **Validation**: Coordinates for guesses must be within the boundaries of the board. This means that both the row and column values must be between `0` and `size-1` (where `size` is the dimension of the square board).

### 6. **Future Features**

#### **Graphical User Interface (GUI)**

- **Visual Representation**: Develop a GUI with a visual board, ship placement, and interactive buttons for a more engaging user experience.
- **Animations and Effects**: Add animations for hits, misses, and sinking ships to make the game more visually appealing.

#### **Ship Placement Options**

- **Manual Placement**: Allow players to place their ships manually rather than randomly, adding a strategic element to the game setup.
- **Ship Rotation**: Enable ships to be placed horizontally or vertically.

#### **Game Saving and Loading**

- **Save Progress**: Allow players to save their game progress and resume later.
- **Load Previous Games**: Implement functionality to load previously saved games.

## Bug Fixes

### 1. **Input Validation for Guesses**

- **Issue**: Players could enter invalid coordinate formats or non-integer values.
- **Fix**: Implemented input validation to ensure guesses are in the format "row column" with both values being integers. If the input format is incorrect or cannot be converted to integers, an error message prompts the player to try again.

### 2. **Coordinates Out of Bounds**

- **Issue**: Players could make guesses outside the board's boundaries, causing errors or unexpected behavior.
- **Fix**: Implemented coordinate validation to ensure guesses fall within the valid range of the board. If coordinates are out of bounds, an error message is displayed, and the player is prompted to enter valid coordinates.

### 3. **Player Name Handling**

- **Issue**: The player’s name was not consistently managed across different parts of the game, leading to errors in score tracking and display.
- **Fix**: Ensured that the player’s name is correctly handled and updated in the global scope, allowing for proper score tracking and personalized messages.

### 4. **Computer Move After Invalid Player Move**

- **Issue**: The computer could make its move even if the player made an invalid guess, leading to incorrect game flow and unfair advantage.
- **Fix**: Modified the game loop to ensure the computer only makes its move after the player has provided a valid guess. This maintains a fair and accurate turn-taking system.

**Remaining Bugs**: No bugs remaining

## Testing

- **Validator Testing**: PEP8 Python Validator
- **Status**: No errors were returned

## Deployment

The code was deployed using Heroku. Steps for deployment:

1. Fork or clone this repository.
2. Create a new Heroku app.
3. Set the buildpacks to Python and NodeJS in that order.
4. Link the Heroku app to the repository.
5. Click deploy.

## Credits

- Code Institute for the deployment terminal.
- Wikipedia for the details of the Battleship game.
- Tutors at Code Institute for solving minor faults in deployment.
- Code Institute for providing an example of a Battleship README document.
