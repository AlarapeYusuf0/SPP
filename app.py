from flask import Flask, render_template, request, jsonify
from model import predict_performance

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    attendance = float(data['attendance'])
    first_term = float(data['first_term'])
    second_term = float(data['second_term'])
    ca_score = float(data['ca_score'])

    prediction = predict_performance(
        attendance, first_term, second_term, ca_score
    )

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
