import random
import os

# ========= Game Setup & Constants =========
HUMAN = 'X' 
AI = 'O' 
scores = {HUMAN: -1, AI: 1, 'tie': 0} 

# ========= Board Functions =========
def create_board():
    """Creates a new Tic-Tac-Toe board represented as a list of 9 'None' elements."""
    return [None] * 9

def display_board(board):
    """Prints the Tic-Tac-Toe board to the console."""
    print(str(board[0] or ' ') + " | " + str(board[1] or ' ') + " | " + str(board[2] or ' '))
    print("---------")
    print(str(board[3] or ' ') + " | " + str(board[4] or ' ') + " | " + str(board[5] or ' '))
    print("---------")
    print(str(board[6] or ' ') + " | " + str(board[7] or ' ') + " | " + str(board[8] or ' '))

def valid_move(board, move):
    """Checks if a given move (0-8) is valid (empty space) on the board."""
    return move in range(9) and board[move] is None

# ========= Player Input =========
def get_human_move(board):
    """Gets a valid move from the human player."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1 
            if valid_move(board, move):
                return move
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# ========= AI Logic (Minimax) =========
def get_ai_move(board):
    """Determines the best move for the AI using the Minimax algorithm."""
    best_score = -1000
    best_move = None
    for move in range(9):
        if board[move] is None:
            board[move] = AI
            score = minimax(board, 0, False)
            board[move] = None 
            if score > best_score:
                best_score = score
                best_move = move
    return best_move

def minimax(board, depth, is_maximizing):
    """Implements the core Minimax algorithm for evaluating board states."""
    result = check_winner(board)
    if result is not None:
        return scores[result]

    if is_maximizing:
        best_score = -1000
        for move in range(9):
            if board[move] is None:
                board[move] = AI
                score = minimax(board, depth + 1, False)
                board[move] = None 
                best_score = max(score, best_score)
        return best_score

    else: 
        best_score = 1000
        for move in range(9):
            if board[move] is None:
                board[move] = HUMAN
                score = minimax(board, depth + 1, True)
                board[move] = None
                best_score = min(score, best_score)
        return best_score

# ========= Game Logic  =========
def check_winner(board):
    """Checks for a winner or a tie."""
    # Check rows
    for row in range(0, 7, 3):
        if board[row] == board[row + 1] == board[row + 2] and board[row] is not None:
            return board[row]

    # Check columns
    for col in range(3):
        if board[col] == board[col + 3] == board[col + 6] and board[col] is not None:
            return board[col]

    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] is not None:
        return board[0]
    if board[2] == board[4] == board[6] and board[2] is not None:
        return board[2]

    # Check for a tie
    if all(cell is not None for cell in board):
        return 'tie'

    return None  

def play_game():
    """Starts and runs the Tic-Tac-Toe game."""
    board = create_board()
    display_board(board)

    if random.randint(0, 1) == 0:
        current_player = HUMAN
    else:
        current_player = AI

    while True:
        if current_player == HUMAN:
            move = get_human_move(board)
        else:
            move = get_ai_move(board)

        board[move] = current_player

        clear_terminal() 
        display_board(board)

        winner = check_winner(board)

        if winner is not None:
            if winner == 'tie':
                print("It's a tie!")
            else:
                print(winner, "wins!")
            break

        current_player = HUMAN if current_player == AI else AI

def clear_terminal():
    """Clears the terminal screen."""
    if os.name == 'nt': 
        os.system('cls')
    else:
        os.system('clear')

# Start the game
play_game() 
