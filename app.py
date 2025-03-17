from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np
import requests

app = Flask(__name__)

# Load trained model
model = joblib.load("power_prediction_model.pkl")

# OpenWeather API Key
API_KEY = "your_openweather_api_key"

def get_weather(city="YourCity"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    
    temperature = response['main']['temp']
    humidity = response['main']['humidity']
    
    return temperature, humidity

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        input_data = np.array([[data['hour'], data['day_of_week'], data['temperature'], data['humidity']]])
        prediction = model.predict(input_data)[0]
        return jsonify({"predicted_power_usage": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
