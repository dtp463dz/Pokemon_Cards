# app.py

import streamlit as st
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
# Set page title
st.title("Cards Poke Visualizations")

# Function to load CSV data
@st.cache_data
def load_data():
    return pd.read_csv('D:/Phenikaa/PTData/CK_Poke/API/carpoke/pokemon_cards1.csv')

# Load the Pokémon data
df = load_data()

# Display a sample of the data
st.subheader("Sample Cards Pokémon Data")
st.write(df.head())


# biểu đồ độ hiếm (tròn)
st.subheader('Phân loại độ hiếm của các loại thẻ')
rarity_counts = df['rarity'].value_counts()
st.dataframe(rarity_counts)

plt.figure(figsize=(10, 6))
rarity_counts.plot(kind='bar', color='skyblue')
plt.title('Số lượng các giá trị trong cột "rarity"')
plt.xlabel('Giá trị rarity')
plt.ylabel('Số lượng')
plt.xticks(rotation=45)
plt.grid(axis='y')
st.pyplot(plt)


# Độ hiếm
st.subheader('Giá theo Rarity (Độ hiếm)')
plt.figure(figsize=(10, 6))
df['tcgplayer_holofoil_market'] = pd.to_numeric(df['tcgplayer_holofoil_market'], errors='coerce')
rarity_price = df.groupby('rarity')['tcgplayer_holofoil_market'].max().reset_index()
rarity_price = rarity_price.sort_values(by='tcgplayer_holofoil_market', ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x='tcgplayer_holofoil_market', y='rarity', data=rarity_price, palette='viridis')
plt.title('Giá cao nhất theo Rarity (Độ hiếm)')
plt.xlabel('Giá cao nhất (USD)')
plt.ylabel('Độ hiếm (Rarity)')
plt.xticks(rotation=45)
plt.grid(axis='x')
st.pyplot(plt)

# Biểu đồ Types
st.subheader('Giá theo Types (Loại năng lượng)')
plt.figure(figsize=(10, 6))
df['tcgplayer_holofoil_market'] = pd.to_numeric(df['tcgplayer_holofoil_market'], errors='coerce')
types_price = df.groupby('types')['tcgplayer_holofoil_market'].max().reset_index()
types_price = types_price.sort_values(by='tcgplayer_holofoil_market', ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x='tcgplayer_holofoil_market', y='types', data=types_price, palette='viridis')
plt.title('Giá cao nhất theo Types (Năng lượng thẻ)')
plt.xlabel('Giá cao nhất (USD)')
plt.ylabel('Loại năng lượng (Types)')
plt.xticks(rotation=45)
plt.grid(axis='x')
st.pyplot(plt)

# thẻ có giá trị cao nhất
st.subheader('10 thẻ có giá trị cao nhất')
df['tcgplayer_holofoil_market'] = pd.to_numeric(df['tcgplayer_holofoil_market'], errors='coerce')

# Lấy 10 thẻ có giá trị cao nhất
top_10_cards = df.nlargest(10, 'tcgplayer_holofoil_market')

# Vẽ biểu đồ
plt.figure(figsize=(12, 6))
sns.barplot(x='tcgplayer_holofoil_market', y='name', data=top_10_cards, palette='viridis')
plt.title('Thẻ Pokémon Có Giá Trị Cao Nhất')
plt.xlabel('Giá cao nhất (USD)')
plt.ylabel('Tên thẻ')
plt.xticks(rotation=45)
plt.grid(axis='x')
st.pyplot(plt)
st.dataframe(top_10_cards[['name', 'tcgplayer_holofoil_market']])

