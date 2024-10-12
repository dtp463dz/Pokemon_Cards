# app.py

import streamlit as st
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Set page title
st.title("Pokémon Data Visualizations")

# Function to load CSV data
@st.cache_data
def load_data():
    return pd.read_csv('D:/Phenikaa/PTData/CK_Poke/API/pokedex/pokemonData.csv')

# Load the Pokémon data
df = load_data()

# Display a sample of the data
st.subheader("Sample Pokémon Data")
st.write(df.head())

# Tiêu đề ứng dụng
st.title('Biểu đồ chỉ số Pokémon')

# Tạo layout cho các biểu đồ
col1, col2 = st.columns(2)  # Tạo 2 cột

# Biểu đồ Total
with col1:
    st.subheader('Total')
    plt.figure(figsize=(10, 6))
    df['Total'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.xlabel('Giá trị')
    plt.ylabel('Số lượng')
    plt.title('Total')
    st.pyplot(plt)

# Biểu đồ HP
with col2:
    st.subheader('HP')
    plt.figure(figsize=(10, 6))
    df['HP'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.xlabel('Giá trị')
    plt.ylabel('Số lượng')
    plt.title('HP')
    st.pyplot(plt)

# Tạo hàng thứ hai cho Attack và Defense
col3, col4 = st.columns(2)  # Tạo 2 cột

# Biểu đồ Attack
with col3:
    st.subheader('Attack')
    plt.figure(figsize=(10, 6))
    df['Attack'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.xlabel('Giá trị')
    plt.ylabel('Số lượng')
    plt.title('Attack')
    st.pyplot(plt)

# Biểu đồ Defense
with col4:
    st.subheader('Defense')
    plt.figure(figsize=(10, 6))
    df['Defense'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.xlabel('Giá trị')
    plt.ylabel('Số lượng')
    plt.title('Defense')
    st.pyplot(plt)

# Biểu đồ Speed ở hàng cuối
st.subheader('Speed')
plt.figure(figsize=(10, 6))
df['Speed'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
plt.gca().spines[['top', 'right']].set_visible(False)
plt.xlabel('Giá trị')
plt.ylabel('Số lượng')
plt.title('Speed')
st.pyplot(plt)

# Phân bố chỉ số
st.subheader('Phân bố chỉ số')
plt.figure(figsize=(10, 6))
df.boxplot(column=['HP', 'Attack', 'Defense', 'Sp.Atk', 'Sp.Def', 'Speed'])
plt.title('Phân bổ chỉ số của Pokemon')
plt.ylabel('Value')
_ = plt.xticks(rotation=45)
st.pyplot(plt)

# Scatter Matrix of Pokémon Stats
st.subheader("Scatter Matrix of Pokémon Stats")
stats = ['Attack', 'Defense', 'HP', 'Sp.Atk', 'Sp.Def', 'Speed', 'Total']
fig, ax = plt.subplots(figsize=(10, 10))
scatter_matrix(df[stats], alpha=0.2, figsize=(10, 10), diagonal='kde', ax=ax)
st.pyplot(fig)

# Exploding the Pokémon types to count them individually
df['Type'] = df['Type'].str.split()  # Split the 'Type' column
df_ex = df.explode('Type')           # Create separate rows for each type

# Display type counts in the sidebar
st.sidebar.subheader("Type Count")
type_counts = df_ex['Type'].value_counts()
st.sidebar.write(type_counts)

# Pie Chart of Pokémon Types
st.subheader("Pie Chart: Pokémon Types Distribution")
fig, ax = plt.subplots(figsize=(10, 10))
wp = {'linewidth': 2, 'edgecolor': "black"}
explode = [0.1] * len(type_counts)  # Adjust the 'explode' for each type
type_counts.plot(kind='pie', autopct="%0.1f%%", explode=explode, wedgeprops=wp, ax=ax)
ax.set_ylabel('')
ax.legend(title="Type", loc='center right', bbox_to_anchor=(1.2, 0.5))
ax.set_title("Pokémon Type Distribution", fontsize=25, fontweight='bold')
st.pyplot(fig)

# Pokémon with highest and lowest stats
def max_stats(df, col_list):
    """Function to return Pokémon with the highest stats."""
    message = ''
    for col in col_list:
        stat = df[col].max()
        name = df[df[col] == df[col].max()]['Name'].values[0]
        message += f"{name} has the highest {col} of {stat}.\n"
    return message

def min_stats(df, col_list):
    """Function to return Pokémon with the lowest stats."""
    message = ''
    for col in col_list:
        stat = df[col].min()
        name = df[df[col] == df[col].min()]['Name'].values[0]
        message += f"{name} has the lowest {col} of {stat}.\n"
    return message

# Display Pokémon with highest and lowest stats
st.subheader("Pokémon with Highest and Lowest Stats")
st.write(max_stats(df, stats))
st.write(min_stats(df, stats))
