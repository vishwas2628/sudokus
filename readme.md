# Sudoku Solver App

A Django web application that solves Sudoku puzzles from images. Upload an image of a Sudoku puzzle, and the app will return the same image with the puzzle solved.

## Features

* Upload an image of a Sudoku puzzle.
* Automatically detects and solves the puzzle.
* Uses an advanced **LLM-based model** for accurate digit recognition.
* Returns the solved puzzle as an image.

## Technologies Used

* **Django**: Web framework for building the app.
* **OpenCV**: For image processing and Sudoku grid detection.
* **TensorFlow**: For model integration and digit recognition.
* **LLM Model**: Enhances accuracy in digit recognition by leveraging machine learning techniques for precise number identification.
* **Pillow**: To manipulate and annotate the output image.
* **NumPy**: For handling Sudoku grid computations.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vishwas2628/sudoku-solver.git
   cd sudoku-solver
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:

   ```bash
   python manage.py runserver
   ```

4. Access the app in your browser at `http://127.0.0.1:8000`.

## Usage

1. Navigate to the homepage.
2. Upload an image of a Sudoku puzzle.
3. The app will process the image, accurately identify numbers using the LLM-based model, and return the solved puzzle.

