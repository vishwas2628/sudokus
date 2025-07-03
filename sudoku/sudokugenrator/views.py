from django.shortcuts import render
import numpy as np
from sudokugenrator.forms import SudokuForm
from .genrateRandom import genrate_sudoku
from sudokugenrator.solver import solveSudoku

def solve_sudoku(puzzle):
    """Solve the Sudoku puzzle."""
    solveSudoku(puzzle)
    return puzzle


def sudoku_view(request):
    # Generate a new puzzle and its solution
    result = genrate_sudoku()
    if result is not None:  
        default_puzzle, solution = result
    else:
        default_puzzle, solution = None, None

    message = None  # Initialize message

    if request.method == 'POST':
        # Check which button was pressed
        if 'generate' in request.POST:
            # Generate a new puzzle
            result = genrate_sudoku()
            if result is not None:
                default_puzzle, solution = result
            else:
                default_puzzle, solution = None, None
            form = SudokuForm(default_puzzle)
        elif 'reset' in request.POST:
            # Reset to the default puzzle
            form = SudokuForm(default_puzzle)
        elif 'submit' in request.POST:
            # Validate the user-submitted puzzle
            puzzle = [[int(request.POST.get(f'cell_{i}_{j}', 0) or 0) for j in range(9)] for i in range(9)]
            if solution is None:
                message = "Error: No solution available to check against. Please generate a new puzzle."
                form = SudokuForm(puzzle)
            else:
                # Use numpy.array_equal to compare arrays
                is_correct = np.array_equal(np.array(puzzle), np.array(solution))
                message = "Correct!" if is_correct else "Incorrect!"
                form = SudokuForm(puzzle)
            return render(request, 'sudokugenrator/sudoku.html', {'form': form, 'message': message})
        elif 'solve' in request.POST:
            form = SudokuForm(solution)
    else:
        # Display the default puzzle
        form = SudokuForm(default_puzzle)

    return render(request, 'sudokugenrator/sudoku.html', {'form': form, 'message': message})
