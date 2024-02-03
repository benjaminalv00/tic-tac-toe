"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cantX = sum([row.count(X) for row in board])
    cantO = sum([row.count(O) for row in board])
    # initial state
    if cantX == 0 and cantO == 0:
        return X
    # if the number of X is equal to the number of O, then it's X's turn
    elif cantX == cantO:
        return X
    # if the number of X is greater than the number of O, then it's O's turn
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    Possible moves are any cells on the board that do not already have an X or an O in them.
    """
    actions = set()
    # iterate over the board
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # if the action is not valid, raise an exception
    if action not in actions(board):
        raise Exception("Invalid action")
    # create a copy of the board
    new_board = deepcopy(board)
    # get the current player
    current_player = player(board)
    # update the new board
    new_board[action[0]][action[1]] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if there is a winner, the game is over
    if winner(board) != None or not actions(board):
        return True
    return False 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    # if the current player is X, then we want to maximize the value, dont use min_value
    if player(board) == X:
        v = -math.inf
        best_action = None
        for action in actions(board):
            # get the value of the action
            value = min_value(result(board, action))
            # if the value is greater than the current value, update the value and the best action
            if value >= v:
                v = value
                best_action = action
        return best_action
    # if the current player is O, then we want to minimize the value, dont use max_value
    else:
        v = math.inf
        best_action = None
        for action in actions(board):
            # get the value of the action
            value = max_value(result(board, action))
            # if the value is less than the current value, update the value and the best action
            if value <= v:
                v = value
                best_action = action
        return best_action
    

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

