from flask import Flask, render_template, request, jsonify
import numpy as np
import h5py

app = Flask(__name__)

# Load the HDF5 model
with h5py.File('./model.h5', 'r') as f:
    model_weights = f['model_weights']
    # Load your model architecture and weights using the HDF5 format

# Function to preprocess user input and make predictions
def predict_survival(data):
    # Preprocess user input
    pclass = int(data['pclass'])
    sex = 1 if data['sex'].lower() == 'female' else 0
    age = float(data['age'])
    sibsp = int(data['sibsp'])
    parch = int(data['parch'])
    fare = float(data['fare'])
    embarked = data['embarked']  # Assuming categorical: C, Q, S
    embarked_encoded = [1 if embarked.upper() == val else 0 for val in ['C', 'Q', 'S']]

    # Prepare input array for prediction
    user_data = np.array([[pclass, sex, age, sibsp, parch, fare] + embarked_encoded])

    # Make prediction
    prediction = model.predict(user_data)

    # Return prediction result
    return 'Survived' if prediction[0] >= 0.5 else 'Did not survive'

# Define route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Define route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    result = predict_survival(data)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
