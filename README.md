# TikTakToeAI
Play the classic game of Tic-Tac-Toe against a challenging AI opponent powered by the Minimax algorithm!

----

## Features
- Human vs. AI gameplay
- Unbeatable AI using the optimal Minimax strategy
- Clear and well-formatted game board display

---- 

## Getting Started
Although i used Python 3.12 to make this project this should work on most if not all available versions.

### Prerequisites

[Install Python 3.x](https://www.python.org/downloads/)

### Installation 
##### Clone the repository:

```
https://github.com/unofficialdxnny/TikTakToeAI/
```
```
cd TikTakToeAI
```
```
python tictactoe.py 
```

## How to Play
- Enter a number (1-9) corresponding to an empty square on the board.
- The AI will then make its move.
- Continue playing until there's a winner or a tie.

## Gameplay Example

 X |   | O 
-----------
   | X |  
-----------
 O |   |  

 ## Code Structure

- tictactoe.py: The main Python file containing the game logic, board representation, - - Minimax implementation, and gameplay functions.
- create_board(): Creates a new empty Tic-Tac-Toe board.
- display_board(): Prints the current state of the board.
- get_human_move(): Handles human player input and validation.
- get_ai_move(): Implements the AI's decision-making using Minimax.
- minimax(): The core Minimax algorithm with alpha-beta pruning (optional).
- check_winner(): Determines if there's a winner or a tie.

## Contributing
Contributions to improve the game or its documentation are welcome! Feel free to open a pull request.

