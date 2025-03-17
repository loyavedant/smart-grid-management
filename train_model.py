import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib  # For saving the model

df = pd.read_csv("cleaned_data.csv")

# Define features and target
X = df[['hour', 'day_of_week', 'temperature', 'humidity']]
y = df['power_usage']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))


joblib.dump(model, "power_prediction_model.pkl")
print("Model saved as power_prediction_model.pkl")
