# Sudoku Web App (Solver & Player)

A Django web application featuring two main modules:
- **Sudoku Solver**: Upload an image of a Sudoku puzzle, and the app will return the same image with the puzzle solved.
- **Sudoku Player**: Play randomly generated Sudoku puzzles directly in your browser.

---

## How the LLM Model Works

The Sudoku Solver app leverages a Large Language Model (LLM)-based approach for digit recognition:
- **Image Preprocessing**: The uploaded Sudoku image is processed using OpenCV to detect and extract the Sudoku grid and individual cells.
- **Digit Recognition**: Each cell image is passed through a deep learning model (LLM/CNN) trained to recognize handwritten or printed digits with high accuracy.
- **LLM Enhancement**: The LLM model further refines predictions by considering the context of the Sudoku grid, improving recognition in ambiguous or low-quality images.
- **Puzzle Solving**: Once the grid is digitized, a backtracking algorithm solves the puzzle, and the solution is overlaid on the original image using Pillow.

---

## Features

### Sudoku Solver
- Upload an image of a Sudoku puzzle.
- Automatic grid detection and digit recognition using advanced ML models.
- Solves the puzzle and returns the solution overlaid on the original image.
- Uses LLM-based and CNN models for high-accuracy digit recognition.

### Sudoku Player
- Play randomly generated Sudoku puzzles.
- Interactive web interface for solving puzzles.
- Validates your solution and provides hints.

---

## Technologies Used

- **Django**: Web framework for backend and routing.
- **OpenCV**: Image processing and grid detection (solver).
- **TensorFlow/Keras**: Deep learning models for digit recognition (solver).
- **LLM Model**: For enhanced digit recognition accuracy (solver).
- **Pillow**: Image manipulation and annotation (solver).
- **NumPy**: Sudoku grid computations.
- **HTML/CSS/JS**: Frontend for player and solver interfaces.

---

## Project Structure

```
sudoku/
  ├── sudokugenrator/      # Player app: generates and serves Sudoku puzzles
  ├── sudokusolver/        # Solver app: image upload, digit recognition, solving
  ├── static/              # CSS and static assets
  ├── templates/           # HTML templates for both apps
  └── manage.py            # Django management script
```

---

## Assets

**Note:**  
The `Resources/assets` folder is missing. However, image asset links are referenced in `sudokusolver/Resources/create_new.py`. If you need these images, please ensure to add them to the correct directory as referenced in the code.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vishwas2628/sudoku-solver.git
   cd sudoku-solver
   ```

2. **(Recommended) Create and activate a virtual environment:**
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the app:**
   Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Usage

- **Solver:**  
  Go to the solver page, upload a Sudoku image, and get the solved puzzle image.

- **Player:**  
  Go to the player page, generate a new puzzle, and play Sudoku interactively.

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

