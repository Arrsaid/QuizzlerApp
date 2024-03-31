# QuizllerApp

QuizllerApp is an interactive quiz application built with Python. Utilizing Object-Oriented Programming (OOP), the app provides users with a series of questions fetched from the Open Trivia Database API. The app is divided into several modules: `ui.py` for the user interface, `quiz_brain.py` for quiz logic, `question_model.py` for the question data structure, and `data.py` for fetching and parsing quiz data.

## Features

- Sleek and simple user interface for quiz interaction.
- Dynamic question generation from an online API.
- Real-time score tracking as users progress through the quiz.
- Support for True/False questions
  
## Modules

### `ui.py`
Handles the graphical user interface of the application, as demonstrated in the included screenshot.

### `quiz_brain.py`
Manages the quiz logic, keeping track of questions and user's answers.

### `question_model.py`
Defines the structure of a question object used throughout the application.

### `data.py`
Responsible for fetching and parsing data from the Open Trivia Database API (`https://opentdb.com/api.php?amount=10`).

## Installation

To run the QuizllerApp, you need Python installed on your system. No additional libraries are required as the project uses native Python modules for GUI and HTTP requests.

```bash
git clone <Your-Project-Repository-URL>
cd <Your-Project-Directory>
python main.py
