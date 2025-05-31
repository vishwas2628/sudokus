import numpy as np
def solveSudoku(board):
    # if not is_valid_sudoku(board):
    #     return False
    def backtrack(ind,rowcol,rset,cset,boxset,board):
        if ind == len(rowcol): 
            return True
        row = rowcol[ind][0]
        col = rowcol[ind][1]
        for num in range(1,10):
            if num not in rset[row] and num not in cset[col] and num not in boxset[3*(row//3) + (col//3)]:
                board[row][col]=num
                rset[row].add(num)
                cset[col].add(num)
                boxset[3*(row//3)+(col//3)].add(num)
                if backtrack(ind+1,rowcol,rset,cset,boxset,board):
                    return True
                rset[row].remove(num)
                cset[col].remove(num)
                boxset[3*(row//3)+(col//3)].remove(num)
                board[row][col]=0
        return False


    rset=[set() for _ in range(9)]
    cset=[set() for _ in range(9)]
    boxset=[set() for _ in range(9)]
    rowcol=[]
    # nums="123456789"

    for row in range(9):
        for col in range(9):
            num=board[row][col]
            if num !=0:
                rset[row].add(num)
                cset[col].add(num)
                boxset[3*(row//3)+(col//3)].add(num)
            else:
                rowcol.append((row,col))

    backtrack(0,rowcol,rset,cset,boxset,board)
    return board


def is_valid_sudoku(board):
    """
    Validates a given Sudoku board represented as a list of numpy arrays.

    :param board: List of numpy arrays (9 arrays of length 9).
    :return: True if valid Sudoku, False otherwise.
    """
    # Convert the board into a NumPy 2D array
    board = np.array(board)
    
    def is_valid_group(group):
        """Helper function to check if a group contains unique numbers 1–9 (ignoring 0)."""
        numbers = group[group != 0]  # Exclude zeros
        return len(numbers) == len(np.unique(numbers))

    # Check rows
    for row in board:
        if not is_valid_group(row):
            return False

    # Check columns
    for col in range(9):
        if not is_valid_group(board[:, col]):  # Access columns
            return False

    # Check 3x3 subgrids
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            subgrid = board[box_row:box_row + 3, box_col:box_col + 3].flatten()  # Extract and flatten subgrid
            if not is_valid_group(subgrid):
                return False

    return True

# def possible(s,r,c,e):
#     for i in range(9):
#         if s[i][c] == e:
#             return False
#         if s[r][i] == e:
#             return False
#         if s[3*(r//3)+i//3][3*(c//3) +i%3] == e:
#             return False
#     return True
# def backtrack(s):
#     for i in range(9):
#         for j in range(9):
#             if s[i][j] == 0:
#                 for e in range(1,10):
#                     if possible(s,i,j,e):
#                         s[i][j] = e
#                         if backtrack(s):
#                             return True
#                         else:
#                             s[i][j] = 0
#                 return False
#     return True
# def sudokuSolver(s):
#     backtrack(s)
#     return s