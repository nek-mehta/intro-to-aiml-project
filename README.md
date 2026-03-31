# intro-to-aiml-project

Food Quality Predictor 🍔
Python-based Machine Learning application, which predicts the quality score of a restaurant based on four major operational parameters. This project was created as a part of an Intro to AI & ML course.

# 📖 Overview
The Food Quality Predictor is a program that utilizes the Linear Regression model to determine the impact of various factors on the final performance of the restaurant. By training on the data set containing information about 15 restaurants, the program is capable of predicting the "Final Score" on a scale of 45 given the new data.

# Key Features
- Command-Line Interface (CLI): Simple interactive prompts (train, predict, exit).
- Data-Driven: Loads and processes restaurant metrics from a CSV/Excel file.
- Accuracy Tracking: Reports the Mean Absolute Error (MAE) to show how precise the predictions are.

# 🛠️ Tech Stack
- Language: Python 3.14
- Data Handling: pandas
- Machine Learning: scikit-learn (Linear Regression)
- Environment: Visual Studio Code

# 🚀 Getting Started
Prerequisites:
Ensure you have Python installed. You will need to install the following libraries:
bash
- pip install pandas scikit-learn

# File Setup
Ensure your directory is structured as follows:


📂 Project_Folder
 ├── model.py               # Main application logic
 └── restaurant_marks.csv   # Dataset containing the 15 restaurant records

# 📋 Usage
Run the script using the terminal:
python model.py

Once running, use the following commands:

- train -> Trains the ML model on the dataset and displays the MAE (Current Target: 0.69).
- predict -> Prompts you to enter values for Cleanliness, Raw Material, Employee, and Taste. Returns a predicted score out of 45.
- exit -> Safely closes the application.

# 📊 Dataset Features
The model evaluates restaurants based on:
- Cleanliness: Hygiene standards of the facility.
- Raw Material: Quality of ingredients used.
- Employee: Staff performance and service quality.
- Taste: The flavor profile and food quality.









