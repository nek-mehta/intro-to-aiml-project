# intro-to-aiml-project

# Food Quality Predictor 🍔
Python-based Machine Learning application, which predicts the quality score of a restaurant based on four major operational parameters. This project was created as a part of an Intro to AI & ML course.

# How to Use:
- Copy the code provided in this repository into Visual Studio Code or any other IDE and import pandas scikit-learn
- Install the data folder which has the restaurant_marks.csv file
Commands:
train : Train the model using data from data/restaurant_marks.csv
predict : Enter your scores and get the guessed final score
exit : To close the program
Input Scores for Predicting:
cleanliness_avg: Score out of 10
rmaterial_avg: Score out of 10
employee_percent: Enter employee quality percent (0 to 100). The program changes it internally as:
Less than 75% = 0 points
75% to 80% = 1 point
80% to 85% = 2 points
85% to 90% = 3 points
90% to 95% = 4 points
95% to 100% = 5 points
project_score: Score out of 20
Output:
The guessed final score is out of 45.
Data File:
The data/restaurant_marks.csv file should have these columns:
cleanliness_avg, rmaterial_avg, employee_percent, taste_score, final_score
Notes:
Run 'train' before 'predict'
Model saves weights in model_weights.txt after training
No extra software needed, simple Python code
This is a student project to learn basic machine learning with Python.









