
from flask import Flask, request, jsonify

app = Flask(__name__)

# Condition multipliers for laptops
CONDITION_MAP = {
    'Excellent': 0.85,
    'Very Good': 0.75,
    'Good': 0.65,
    'Poor': 0.45
}

@app.route('/')
def home():
    return jsonify({
        "message": "💻 Laptop Resale Price Predictor API is running!",
        "usage": "Send POST request to /predict with JSON input."
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        brand = data.get('brand', 'Unknown')
        model_name = data.get('model', 'Unknown')
        cpu = data.get('cpu', 'Unknown')
        ram = float(data.get('ram', 0))
        memory = data.get('memory', 'Unknown')
        gpu = data.get('gpu', 'Unknown')
        condition = data.get('condition', 'Good')
        age_years = float(data.get('age_years', 1))
        original_price = float(data.get('original_price', 0))

        # Depreciation logic
        multiplier = CONDITION_MAP.get(condition, 0.65)
        resale_price = original_price * multiplier * (0.85 ** age_years)

        return jsonify({
            "predicted_resale_price": round(resale_price, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
