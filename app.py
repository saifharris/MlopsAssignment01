from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Create a Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('house-predict-model.pkl')

# Initialize the scaler (if you used a scaler during model training)
scaler = StandardScaler()


# Input validation and prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the POST request
        data = request.json
        required_fields = [
            'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
            'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'
        ]
        # Check for missing fields
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        # Prepare the input for the model
        input_data = np.array([
            [
                data['CRIM'], data['ZN'], data['INDUS'], data['CHAS'],
                data['NOX'], data['RM'], data['AGE'], data['DIS'],
                data['RAD'], data['TAX'], data['PTRATIO'], data['B'],
                data['LSTAT']
            ]
        ])
        
        # Scale the input data 
        input_data_scaled = scaler.fit_transform(input_data)
        
        # Predict the house price
        prediction = model.predict(input_data_scaled)
        
        return jsonify({'predicted_price': prediction[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Serve the index.html file from the templates folder
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return '', 204


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
