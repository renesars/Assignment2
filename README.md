# Diabetes Prediction Web Application

A Flask-based web application for predicting diabetes using Machine Learning models. This project allows users to input their health data and receive predictions for diabetes status based on pre-trained machine learning models. The app provides an intuitive interface and supports three different prediction algorithms.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Model Details](#model-details)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Features

- **Simple User Interface**: Easy-to-use and visually appealing web design.
- **Multi-Model Predictions**:
  - Logistic Regression
  - Random Forest
  - Support Vector Machine (SVM)
- **Instant Results**: Real-time predictions based on user input.
- **Scalable**: Designed for further integration and deployment on cloud services.
- **Secure**: Lightweight and robust backend with Flask.

---

## Project Structure

The directory structure for the project is as follows:

assignment2/
├── app.py                  # Main entry point for the Flask application
├── app/
│   ├── __init__.py         # Flask app initialization
│   ├── routes.py           # Routing and logic for the web app
│   ├── templates/
│   │   └── index.html      # Frontend HTML template
│   ├── static/
│       └── style.css       # CSS file for styling the app
├── models/
│   ├── diabetes_best_model.pkl # Pre-trained ML model for diabetes prediction
│   ├── scaler.pkl              # Pre-fitted scaler for feature normalization
├── requirements.txt        # List of dependencies for the project
└── README.md               # Documentation for the project


---

## Technologies Used

- **Programming Language**: Python 3.7+
- **Framework**: Flask
- **Frontend**: HTML, CSS
- **Machine Learning Library**: Scikit-learn
- **Serialization**: Joblib
- **Version Control**: Git and GitHub

---

## Setup Instructions

### Prerequisites

1. **Python 3.7+**: Make sure Python is installed on your system.
2. **Git**: Ensure Git is installed to clone the repository.
3. **Virtual Environment**: Recommended for managing dependencies.
