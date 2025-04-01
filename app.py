from flask import Flask, render_template, request
import pickle

# Load the trained BMI model
model = pickle.load(open("bmi_model.pkl", "rb"))

app = Flask(__name__)

# Home route to display the form
@app.route("/")
def home():
    return render_template("index.html")

# Predict route to process input and return the result
@app.route("/predict", methods=["POST"])
def predict():
    try:
        height = float(request.form["height"]) / 100  # Convert cm to meters
        weight = float(request.form["weight"])
        bmi = round(weight / (height ** 2), 2)

        # Define BMI categories with images
        if bmi < 18.5:
            category = "Underweight"
            risk = "Higher risk of nutritional deficiency and osteoporosis."
            advice = "Eat nutrient-rich foods and increase calorie intake."
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Underweight_icon.svg/1200px-Underweight_icon.svg.png"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight"
            risk = "Low risk."
            advice = "Maintain a balanced diet and regular exercise."
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Healthy_weight_icon.svg/1200px-Healthy_weight_icon.svg.png"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            risk = "Increased risk of heart disease and diabetes."
            advice = "Consider a healthier diet and regular physical activity."
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Overweight_icon.svg/1200px-Overweight_icon.svg.png"
        else:
            category = "Obese"
            risk = "High risk of severe health conditions."
            advice = "Consult a healthcare provider for weight management."
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Obese_icon.svg/1200px-Obese_icon.svg.png"

        return render_template(
            "index.html",
            prediction_text=f"Your BMI: {bmi} ({category})",
            risk_text=f"Health Risk: {risk}",
            advice_text=f"Tip: {advice}",
            image_url=image_url
        )
    except Exception as e:
        return render_template("index.html", prediction_text="Error: Invalid input!")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)





