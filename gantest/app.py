from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

# Đọc dữ liệu từ CSV
data = pd.read_csv('data.csv')

# Dự đoán giá cho một thẻ cụ thể
def predict_prices(card_id):
    card_data = data[data['id'] == card_id]
    if not card_data.empty:
        current_price = card_data['avg30'].values[0]
        
        # Giả định biến động giá trong 30 ngày
        days = 30
        price_predictions = [current_price + np.random.normal(0, 0.1) for _ in range(days)]
        return price_predictions
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/<card_id>')
def predict(card_id):
    predictions = predict_prices(card_id)
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)