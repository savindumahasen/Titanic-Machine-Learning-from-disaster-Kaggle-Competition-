from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
model_path = './TitanicDisaterModel.h5'
model = pickle.load(open(model_path, 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    feature_names = ['0', '1', '2', '3', '4', '5', '6', '7']

    try:
        features = [float(request.json[f]) for f in feature_names]
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter numeric values.'})

    input_data = [features]

    # Make prediction
    pred = model.predict(input_data)

    # Prepare the result
    if pred[0] == 0:
        result = "Not survived"
    else:
        result = "Survived"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
