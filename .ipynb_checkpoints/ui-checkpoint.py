import tkinter as tk
from tkinter import messagebox
import numpy as np
import h5py

# Create the main window
root = tk.Tk()
root.title("Survival Prediction")

# Load the HDF5 model
with h5py.File('model.h5', 'r') as f:
    model_weights = f['model_weights']
    # Load your model architecture and weights using the HDF5 format

# Function to predict survival based on user input
def predict_survival():
    try:
        # Collect user input
        pclass = int(pclass_entry.get())
        sex = sex_entry.get()  # Assuming binary: male/female
        age = float(age_entry.get())
        sibsp = int(sibsp_entry.get())
        parch = int(parch_entry.get())
        fare = float(fare_entry.get())
        embarked = embarked_entry.get()  # Assuming categorical: C, Q, S

        # Preprocess user input
        # Convert categorical variables to one-hot encoding
        sex_encoded = 1 if sex.lower() == 'female' else 0
        embarked_encoded = [1 if embarked.upper() == val else 0 for val in ['C', 'Q', 'S']]

        # Prepare input array for prediction
        user_data = np.array([[pclass, sex_encoded, age, sibsp, parch, fare] + embarked_encoded])

        # Make prediction
        prediction = model.predict(user_data)

        # Display prediction result
        if prediction[0] >= 0.5:
            messagebox.showinfo("Prediction", "Survived")
        else:
            messagebox.showinfo("Prediction", "Did not survive")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid data")

# Create labels and entry widgets for user input
pclass_label = tk.Label(root, text="Pclass:")
pclass_label.pack(pady=5)
pclass_entry = tk.Entry(root)
pclass_entry.pack(pady=5)

sex_label = tk.Label(root, text="Sex (male/female):")
sex_label.pack(pady=5)
sex_entry = tk.Entry(root)
sex_entry.pack(pady=5)

age_label = tk.Label(root, text="Age:")
age_label.pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

sibsp_label = tk.Label(root, text="SibSp:")
sibsp_label.pack(pady=5)
sibsp_entry = tk.Entry(root)
sibsp_entry.pack(pady=5)

parch_label = tk.Label(root, text="Parch:")
parch_label.pack(pady=5)
parch_entry = tk.Entry(root)
parch_entry.pack(pady=5)

fare_label = tk.Label(root, text="Fare:")
fare_label.pack(pady=5)
fare_entry = tk.Entry(root)
fare_entry.pack(pady=5)

embarked_label = tk.Label(root, text="Embarked (C/Q/S):")
embarked_label.pack(pady=5)
embarked_entry = tk.Entry(root)
embarked_entry.pack(pady=5)

# Create a button to predict survival
predict_button = tk.Button(root, text="Predict Survival", command=predict_survival)
predict_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
