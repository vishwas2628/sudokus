# from static.dataset import path
import pandas as pd
import numpy as np

import kagglehub

# Download latest version
path = kagglehub.dataset_download("bryanpark/sudoku")

print("Path to dataset files:", path)

#path = "C:/Users/HP/OneDrive/Desktop/sudokus/sudoku/static/sudoku.csv"
def genrateRandom():
    try:
        chunk_container = pd.read_csv(f"{path}")
        # chunks = list(chunk_container)
        df = pd.DataFrame(chunk_container)
        
        random_index = np.random.choice(df.index)
        random_row_iloc = df.iloc[[random_index]]
        
        return random_row_iloc.to_numpy().flatten()
    except FileNotFoundError:
         print(f"Error: File not found at '{path}'")
         return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def sudoku_string_to_array(sudoku_str):
    if len(sudoku_str) != 81 or not sudoku_str.isdigit():
        raise ValueError("Input must be a string of 81 digits.")

    # Convert the string into a list of integers
    sudoku_list = [int(char) for char in sudoku_str]

    # Reshape the list into a 9x9 numpy array
    sudoku_array = np.array(sudoku_list).reshape(9, 9)

    return sudoku_array


def genrate_sudoku():
    row = genrateRandom()
    
    if row is None:
        return None

    puzzle = sudoku_string_to_array(row[0])
    solution = sudoku_string_to_array(row[1])

    return puzzle, solution