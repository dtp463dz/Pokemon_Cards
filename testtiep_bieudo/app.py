from flask import Flask, jsonify
import pandas as pd
import numpy as np
import requests
from statsmodels.tsa.arima.model import ARIMA
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dữ liệu giả lập về giá thẻ Pokémon theo thời gian (bạn nên lấy dữ liệu thực từ API)
historical_data = {
    "date": pd.date_range(start="2024-10-08", periods=30, freq="D"),
    "market_price": [3.5 + i*0.05 for i in range(30)]  # Tăng giả định giá qua thời gian
}

df = pd.DataFrame(historical_data)

# Hàm để dự đoán giá trong tương lai
def predict_future_price(data, steps=7):
    model = ARIMA(data['market_price'], order=(5, 1, 0))  # ARIMA(p,d,q), đây là mô hình đơn giản
    model_fit = model.fit()
    
    # Dự đoán giá cho "steps" ngày tới
    forecast = model_fit.forecast(steps=steps)
    return forecast

@app.route('/api/predict_price', methods=['GET'])
def predict_price():
    # Sử dụng mô hình ARIMA để dự đoán giá cho 7 ngày tới
    predicted_prices = predict_future_price(df, steps=7)
    
    # Trả về dữ liệu JSON
    future_dates = pd.date_range(start=df['date'].max(), periods=7, freq="D").strftime('%Y-%m-%d').tolist()
    result = {
        "dates": future_dates,
        "predicted_prices": predicted_prices.tolist()
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
