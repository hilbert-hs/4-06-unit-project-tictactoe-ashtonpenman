[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18421790)
# 4.06-Unit-Project-TicTacToe

Using Python, students will create a Tic-Tac-Toe game. This project has two parts:
1. Designing a game so that two users can play Tic-Tac-Toe against each other.
2. Writing functions which will check the board to see if Xs or Os have won the game or if it ends in a draw.

## Overview

Tic-Tac-Toe is a game in which one player draws X's and another player draws O's inside a set of nine squares and each player tries to be the first to fill a row, column, or diagonal of squares with either X's or O's. We will be writing an interactive Tic-Tac-Toe program. At the end of each turn the computer will check to see if X's have won the game or if the O's have won the game.

### Behavior

* Use variables to store the user names for personalized prompts.
* Create a game board represented as a list of lists, size 3 by 3. 
* The program will prompt the user to enter their name and their opponents name. 
* Whoever enters their name first will be playing as X's, and the other player will be O's. 
* The players will take turns inputting the row and column they would like to place their mark. 
* If that spot is already taken the program will ask for the spot again. 
* At the end of each player's turn the program will check if that player has won.
* At the end of each player's turn the program will print the updated game board.
* If there are no more spots open and nobody has won the game, the program will print Tie game!

### Implementation Details

* Check for a winner horizontally, vertically, and on both diagonals.
* Cannot allow a user to overwrite a spot on the board.

### Grading / Rubric

| **Functional Correctness (Behavior)**                     |               |       |
|-----------------------------------------------------------|---------------|-------|
| Program prompts user for name                             | 2 points      |       |
| Program marks board where user requested                  | 5 points      |       |
| Program prints a readable board after user’s turn         | 5 points      |       |
| Program won’t overwrite value on board                    | 5 points      |       |
| Program reports who won or if there is a tie              | 15 points     |       |
| Program ends after win, loss, or tie                      | 3 points      |       |
| **Sub Total**                                             | **35 points** |       |
| **Technical Correctness**                                 |               |       |
| Correctly use of game loop                                | 5 points      |       |
| Correctly indexes into lists of lists to store board      | 5 points      |       |
| Correctly checks board for mark                           | 5 points      |       |
| Checks for winners on all three horizontals and verticals | 20 points     |       |
| Checks for winners on both diagonals                      | 10 points     |       |
| **Sub Total**                                             | **45 points** |       |
| **PROJECT TOTAL**                                         | **80 points** |       |

