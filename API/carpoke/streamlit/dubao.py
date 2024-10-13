import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.graph_objs as go

# Tải dữ liệu CSV (sử dụng st.cache_data thay vì st.cache)
@st.cache_data
def load_data():
    data = pd.read_csv('D:/Phenikaa/PTData/CK_Poke/API/carpoke/price_pika_full.csv')
    return data

# Hàm dự đoán giá dựa trên hồi quy tuyến tính
def predict_future_price(prices):
    if len(prices) < 2:
        return None

    X = np.array([0, 1, 2, 3, 4]).reshape(-1, 1)  # Thời gian
    y = np.array(prices)

    model = LinearRegression().fit(X, y)
    future_days = np.array([5, 6]).reshape(-1, 1)
    future_prices = model.predict(future_days)

    return {
        '7-day': round(future_prices[0], 2),
        '30-day': round(future_prices[1], 2)
    }, future_prices.flatten()

# Hiển thị chi tiết thẻ và dự đoán giá
def show_card_details(card_id, data):
    card_data = data[data['id'] == card_id]
    
    if card_data.empty:
        st.write(f"Không tìm thấy thông tin cho thẻ với ID: {card_id}")
        return

    st.write(f"### Thông tin chi tiết cho thẻ ID: {card_id}")
    st.write(f"**Tên thẻ**: {card_data.iloc[0]['name']}")
    st.write(f"**Độ hiếm**: {card_data.iloc[0]['rarity']}")

    price_columns = ['Jul-24', 'Aug-24', 'Sep-24', '1/10/2024', '8/10/2024']
    prices = card_data[price_columns].values.flatten().astype(float)

    # Sử dụng Plotly để hiển thị biểu đồ
    fig = go.Figure()

    # Biểu đồ giá thị trường
    fig.add_trace(go.Scatter(
        x=price_columns,  # Thời gian trên trục X
        y=prices,         # Giá trên trục Y
        mode='lines+markers',
        name='Giá Thị Trường',
        line=dict(color='royalblue', width=2),
        marker=dict(size=8)
    ))

    # Dự đoán giá
    prediction, future_prices = predict_future_price(prices)

    # Thêm biểu đồ dự đoán giá cho 7 ngày
    if prediction:
        future_labels = ['7-day', '30-day']
        future_x = price_columns + future_labels  # Gộp trục X với giá dự đoán
        future_prices_full = np.concatenate((prices, future_prices))  # Gộp giá thực tế và giá dự đoán

        fig.add_trace(go.Scatter(
            x=future_x,
            y=future_prices_full,
            mode='lines+markers',
            name='Dự Đoán Giá',
            line=dict(color='orange', width=2, dash='dash'),  # Đường gạch cho dự đoán
            marker=dict(size=8)
        ))

        # Hiển thị dự đoán giá
        st.write(f"**Dự đoán giá sau 7 ngày**: ${prediction['7-day']}")
        st.write(f"**Dự đoán giá sau 30 ngày**: ${prediction['30-day']}")

    else:
        st.write("Không đủ dữ liệu để dự đoán giá.")

    # Tùy chỉnh trục X để hiển thị rõ hơn
    fig.update_layout(
        title=f"Lịch Sử Giá Thị Trường cho Thẻ ID: {card_id}",
        xaxis_title="Thời gian",
        yaxis_title="Giá ($)",
        xaxis_tickangle=-45,  # Xoay nhãn trục X để nhìn rõ hơn
        template="plotly_white"
    )

    st.plotly_chart(fig)

# Main app logic
st.title('Pokemon Card Price Predictor')

# Lấy ID thẻ từ URL
query_params = st.experimental_get_query_params()
card_id_input = query_params.get('id', [None])[0]  # Ensure full ID is extracted

# Tải dữ liệu
data = load_data()

if card_id_input:
    show_card_details(card_id_input, data)
else:
    st.write("Vui lòng cung cấp ID thẻ Pokémon để xem dự đoán.")
