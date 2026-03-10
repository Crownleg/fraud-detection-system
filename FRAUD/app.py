from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    amount = float(request.form["amount"])
    location = int(request.form["location"])
    time = int(request.form["time"])
    device = int(request.form["device"])

    features = np.array([[amount, location, time, device]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "⚠ Fraudulent Transaction"
    else:
        result = "✅ Legitimate Transaction"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)