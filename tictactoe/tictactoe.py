"""
Tic Tac Toe Player
"""

import math

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


def player(board): #done
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0
    for i in board :
        xcount += i.count(X)
        ocount += i.count(O)
    if xcount <= ocount:
        return X
    else :
        return O


def actions(board): #done
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = set()
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element == EMPTY:
                act.add((i,j))
    return act


def result(board, action): #done
    """
    Returns the board that results from making move (i, j) on the board.
    """
    curr_player = player(board)
    # We can use new_board = board but it creates a reference to the original board and hence changes the original board, so we use this method to create a new board.
    new_board = []
    for i in board:
        new_board.append(i.copy())
    i, j = action #unpacking the tuple
    if board[i][j] != EMPTY:
        raise Exception("Invalid Move")
    if not (0 <= i < 3) or not (0 <= j < 3):
        raise Exception("Invalid Move")
    new_board[i][j] = curr_player
    return new_board

def winner(board): #done
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] is not None and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] is not None and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def terminal(board): #done
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in board:
        if EMPTY in i:
            return False
    return True



def utility(board): #done
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board): #done
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board), None
        v = -1000
        move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = X
                    temp, _ = min_value(board)
                    board[i][j] = EMPTY
                    if temp > v:
                        v = temp
                        move = (i, j)
        return v, move

    def min_value(board):
        if terminal(board):
            return utility(board), None
        v = 1000
        move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = O
                    temp, _ = max_value(board)
                    board[i][j] = EMPTY
                    if temp < v:
                        v = temp
                        move = (i, j)
        return v, move

    if player(board) == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]

# """
# Tic Tac Toe Player
# """

# import math
# from copy import deepcopy

# X = "X"
# O = "O"
# EMPTY = None


# def initial_state():
#     """
#     Returns starting state of the board.
#     """
#     return [[EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY]]


# def player(board):
#     """
#     Returns player who has the next turn on a board.
#     """
#     Xcount = 0
#     Ocount = 0

#     for row in board:
#         Xcount += row.count(X)
#         Ocount += row.count(O)

#     if Xcount <= Ocount:
#         return X
#     else:
#         return O


# def actions(board):
#     """
#     Returns set of all possible actions (i, j) available on the board.
#     """

#     possible_moves = set()

#     for row_index, row in enumerate(board):
#         for column_index, item in enumerate(row):
#             if item == None:
#                 possible_moves.add((row_index, column_index))
    
#     return possible_moves


# def result(board, action):
#     """
#     Returns the board that results from making move (i, j) on the board.
#     """
#     player_move = player(board)

#     new_board = deepcopy(board)
#     i, j = action

#     if board[i][j] != None:
#         raise Exception
#     else:
#         new_board[i][j] = player_move

#     return new_board


# def winner(board):
#     """
#     Returns the winner of the game, if there is one.
#     """
#     for player in (X, O):
#         # check vertical
#             for row in board:
#                 if row == [player] * 3:
#                     return player

#         # check horizontal
#             for i in range(3):
#                 column = [board[x][i] for x in range(3)]
#                 if column == [player] * 3:
#                     return player
        
#         # check diagonal
#             if [board[i][i] for i in range(0, 3)] == [player] * 3:
#                 return player

#             elif [board[i][~i] for i in range(0, 3)] == [player] * 3:
#                 return player
#     return None
                               

# def terminal(board):
#     """
#     Returns True if game is over, False otherwise.
#     """
#     # game is won by one of the players
#     if winner(board) != None:
#         return True

#     # moves still possible
#     for row in board:
#         if EMPTY in row:
#             return False

#     # no possible moves
#     return True


# def utility(board):
#     """
#     Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
#     """

#     win_player = winner(board)

#     if win_player == X:
#         return 1
#     elif win_player == O:
#         return -1
#     else:
#         return 0


# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """

#     def max_value(board):
#         optimal_move = ()
#         if terminal(board):
#             return utility(board), optimal_move
#         else:
#             v = -5
#             for action in actions(board):
#                 minval = min_value(result(board, action))[0]
#                 if minval > v:
#                     v = minval
#                     optimal_move = action
#             return v, optimal_move

#     def min_value(board):
#         optimal_move = ()
#         if terminal(board):
#             return utility(board), optimal_move
#         else:
#             v = 5
#             for action in actions(board):
#                 maxval = max_value(result(board, action))[0]
#                 if maxval < v:
#                     v = maxval
#                     optimal_move = action
#             return v, optimal_move

#     curr_player = player(board)

#     if terminal(board):
#         return None

#     if curr_player == X:
#         return max_value(board)[1]

#     else:
#         return min_value(board)[1]