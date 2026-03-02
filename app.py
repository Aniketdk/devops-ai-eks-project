from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from AI CI/CD App!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    number = data.get('number', 0)
    prediction = "even" if number % 2 == 0 else "odd"
    return jsonify({"number": number, "prediction": prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)