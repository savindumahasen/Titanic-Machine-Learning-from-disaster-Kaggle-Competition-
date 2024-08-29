import React, { useState } from 'react';
import './App.css';  // Assuming you have a CSS file for styling

function App() {
  const [formData, setFormData] = useState({
    '0': '',
    '1': '',
    '2': '',
    '3': '',
    '4': '',
    '5': '',
    '6': '',
    '7': ''
  });
  const [result, setResult] = useState('');
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevData => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (data.error) {
        setError(data.error);
        setResult('');
      } else {
        setResult(data.result);
        setError('');
      }
    } catch (err) {
      setError('An error occurred while making the prediction.');
      setResult('');
    }
  };

  const closePopup = () => {
    setResult('');
  };

  return (
    <div className="app-container">
      <div className="form-container">
        <h1 className="form-title">Survival Prediction</h1>

        <form method="post" onSubmit={handleSubmit} className="prediction-form">
          <div className="form-group">
            <label htmlFor="feature0" className="form-label">Passenger ID:</label>
            <input
              type="text"
              name="0"
              value={formData['0']}
              onChange={handleChange}
              required
              className="form-input"
            />
          </div>

          <div className="form-group0">
            <label htmlFor="feature1" className="form-label">Pclass:</label>
            <input
              type="text"
              name="1"
              value={formData['1']}
              onChange={handleChange}
              required
              className="form-input"
            />
          </div>

          <div className="form-group1">
            <label htmlFor="feature2" className="form-label">Sex:</label>
            <input
              type="number"
              name="2"
              value={formData['2']}
              onChange={handleChange}
              max="1"
              min="0"
              required
              className="form-input"
            />
          </div>

          <div className="form-group2">
            <label htmlFor="feature3" className="form-label">Age:</label>
            <input
              type="text"
              name="3"
              value={formData['3']}
              onChange={handleChange}
              required
              className="form-input"
            />
          </div>

          <div className="form-group3">
            <label htmlFor="feature4" className="form-label">SibSp:</label>
            <input
              type="text"
              name="4"
              value={formData['4']}
              onChange={handleChange}
              required
              className="form-input"
            />
          </div>

          <div className="form-group4">
            <label htmlFor="feature5" className="form-label">Parch:</label>
            <input
              type="text"
              name="5"
              value={formData['5']}
              onChange={handleChange}
              required
              className="form-input"
            />
          </div>

          <div className="form-group5">
            <label htmlFor="feature6" className="form-label">Fare:</label>
            <input
              type="text"
              name="6"
              value={formData['6']}
              onChange={handleChange}
              required
              className="form-input"
            />
          </div>

          <div className="form-group6">
            <label htmlFor="feature7" className="form-label">Embarked:</label>
            <input
              type="text"
              name="7"
              value={formData['7']}
              onChange={handleChange}
              required
              className="form-input"
            />
          </div>

          <button type="submit" className="submit-button">Predict</button>
        </form>
      </div>

      {/* Result Popup */}
      {result && (
        <div className="popup-overlay">
          <div className="popup">
            <h2>Prediction Result</h2>
            <p>{result}</p>
            <button onClick={closePopup} className="close-button">Close</button>
          </div>
        </div>
      )}

      {/* Error Popup */}
      {error && (
        <div className="popup-overlay">
          <div className="popup">
            <h2>Error</h2>
            <p>{error}</p>
            <button onClick={() => setError('')} className="close-button">Close</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
