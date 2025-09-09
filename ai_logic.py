"""
AI logic for Gomoku: move selection and evaluation.
"""
import random
from game_logic import BOARD_SIZE

SCORE_GRADE = 10
MAX_SCORE = 1008611

def scan_board(board, color):
    """
    Scan each empty cell and evaluate its potential in all directions for the given color.
    Returns a 3D list of scores for each cell and direction.
    """
    shape = [[[0 for _ in range(5)] for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    # TODO: Implement actual evaluation logic
    return shape

def sort_shape(shape):
    """
    Sorts the score matrix for each cell and direction.
    """
    # TODO: Implement actual sorting logic
    return shape

def evaluate_shape(shape):
    """
    Evaluates the score matrix and returns the best move coordinates and score.
    """
    # TODO: Implement actual evaluation logic
    return (0, 0, 0)  # placeholder

def autoplay(board, m, n):
    """
    Selects a random valid move near the last move.
    """
    a1 = [1,-1,1,-1,1,-1,0,0]
    b1 = [1,-1,-1,1,0,0,1,-1]
    rand = random.randint(0,7)
    while m+a1[rand]>=0 and m+a1[rand]<BOARD_SIZE and n+b1[rand]>=0 and n+b1[rand]<BOARD_SIZE and board[m+a1[rand]][n+b1[rand]]!=0 :
        rand = random.randint(0,7)
    return m + a1[rand], n+b1[rand]

def beta_go(board, m, n, color, times, difficulty='medium'):
    """
    AI move selection: chooses move based on difficulty.
    - easy: random
    - medium: current evaluation
    - hard: prioritize blocking/winning
    """
    if difficulty == 'easy':
        return autoplay(board, m, n)
    elif difficulty == 'medium':
        # Use current evaluation logic
        shape_P = scan_board(board, -color)
        shape_C = scan_board(board, color)
        shape_P = sort_shape(shape_P)
        shape_C = sort_shape(shape_C)
        max_x_P, max_y_P, max_P = evaluate_shape(shape_P)
        max_x_C, max_y_C, max_C = evaluate_shape(shape_C)
        if max_P > max_C and max_C < MAX_SCORE:
            return max_x_P, max_y_P
        else:
            return max_x_C, max_y_C
    elif difficulty == 'hard':
        # Prioritize blocking opponent or winning
        shape_P = scan_board(board, -color)
        shape_C = scan_board(board, color)
        shape_P = sort_shape(shape_P)
        shape_C = sort_shape(shape_C)
        max_x_P, max_y_P, max_P = evaluate_shape(shape_P)
        max_x_C, max_y_C, max_C = evaluate_shape(shape_C)
        # If can win, do it
        if max_C >= MAX_SCORE:
            return max_x_C, max_y_C
        # If opponent can win, block
        if max_P >= MAX_SCORE:
            return max_x_P, max_y_P
        # Otherwise, best move
        if max_P > max_C:
            return max_x_P, max_y_P
        else:
            return max_x_C, max_y_C
    else:
        return autoplay(board, m, n)
