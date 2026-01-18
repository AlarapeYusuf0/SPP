import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
data = pd.read_csv("student_data.csv")

X = data[['attendance', 'first_term', 'second_term', 'ca_score']]
y = data['performance']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "student_model.pkl")

print("3rd Term Prediction Model trained successfully.")
