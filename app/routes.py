from flask import render_template, request
import joblib
import numpy as np
from app import app

# Load the best model and scaler once when the app starts
best_model = joblib.load('diabetes_best_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from form
    pregnancies = float(request.form['Pregnancies'])
    glucose = float(request.form['Glucose'])
    blood_pressure = float(request.form['BloodPressure'])
    skin_thickness = float(request.form['SkinThickness'])
    insulin = float(request.form['Insulin'])
    bmi = float(request.form['BMI'])
    diabetes_pedigree = float(request.form['DiabetesPedigreeFunction'])
    age = float(request.form['Age'])
    
    # Input data for prediction
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])

    # Scale the input data using the scaler
    input_data_scaled = scaler.transform(input_data)

    # Make prediction using the best model
    prediction = best_model.predict(input_data_scaled)[0]
    
    # Return the prediction result
    if prediction == 0:
        result = "No Diabetes"
    else:
        result = "Diabetes"

    return render_template('index.html', prediction=result)

