import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "student_model.pkl")
model = joblib.load(model_path)

def predict_performance(attendance, first_term, second_term, ca_score):
    prediction = model.predict([[attendance, first_term, second_term, ca_score]])

    if prediction[0] == 1:
        return "Likely to Pass 3rd Term"
    else:
        return "At Risk in 3rd Term"
