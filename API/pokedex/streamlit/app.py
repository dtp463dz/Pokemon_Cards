import streamlit as st
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from pySankey.sankey import sankey
from matplotlib.lines import Line2D
from matplotlib.cm import ScalarMappable
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import seaborn as sns


# Tạo sidebar để chọn trang
page = st.sidebar.selectbox("Chọn trang", ["Pokémon Stats", "Abilities Dataset", "Distribution Pokemon"])

# Trang Pokémon Stats
if page == "Pokémon Stats":
    # Set page title
    st.title("Pokémon Data Visualizations")

    # Function to load CSV data
    @st.cache_data
    def load_pokemon_data():
        return pd.read_csv('D:/Phenikaa/PTData/CK_Poke/API/pokedex/pokemonData.csv')

    # Load the Pokémon data
    df = load_pokemon_data()

    # Display a sample of the data
    st.subheader("Sample Pokémon Data")
    st.write(df.head())

    # Tiêu đề ứng dụng
    st.title('Biểu đồ chỉ số Pokémon')

    # Tạo layout cho các biểu đồ
    col1, col2 = st.columns(2)  # Tạo 2 cột

    # Biểu đồ Total
    with col1:
        st.subheader('Total (Tổng cộng)')
        plt.figure(figsize=(10, 6))
        df['Total'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
        plt.gca().spines[['top', 'right']].set_visible(False)
        plt.xlabel('Giá trị')
        plt.ylabel('Số lượng')
        plt.title('Total')
        st.pyplot(plt)

    # Biểu đồ HP
    with col2:
        st.subheader('HP (Máu)')
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
        st.subheader('Attack (Tấn công)')
        plt.figure(figsize=(10, 6))
        df['Attack'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
        plt.gca().spines[['top', 'right']].set_visible(False)
        plt.xlabel('Giá trị')
        plt.ylabel('Số lượng')
        plt.title('Attack')
        st.pyplot(plt)

    # Biểu đồ Defense
    with col4:
        st.subheader('Defense (Phòng thủ)')
        plt.figure(figsize=(10, 6))
        df['Defense'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
        plt.gca().spines[['top', 'right']].set_visible(False)
        plt.xlabel('Giá trị')
        plt.ylabel('Số lượng')
        plt.title('Defense')
        st.pyplot(plt)

    # Biểu đồ Speed ở hàng cuối
    st.subheader('Speed (Tốc độ)')
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

        # Các cột liên quan đến chỉ số
    stats = ['Total', 'HP', 'Attack', 'Defense', 'Sp.Atk', 'Sp.Def', 'Speed']

    def max_stats(df, col_list):
        """Function to return Pokémon with the highest stats."""
        message = {}
        for col in col_list:
            stat = df[col].max()
            name = df[df[col] == df[col].max()]['Name'].values[0]
            poke_id = df[df[col] == df[col].max()]['#'].values[0]
            message[col] = (name, stat, poke_id)
        return message

    def min_stats(df, col_list):
        """Function to return Pokémon with the lowest stats."""
        message = {}
        for col in col_list:
            stat = df[col].min()
            name = df[df[col] == df[col].min()]['Name'].values[0]
            poke_id = df[df[col] == df[col].min()]['#'].values[0]
            message[col] = (name, stat, poke_id)
        return message

    # Hàm lấy URL hình ảnh Pokémon dựa trên ID
    def get_pokemon_image_url(poke_id):
        """Function to get the image URL of a Pokémon based on its ID."""
        url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png"
        return url

    # Lấy dữ liệu các chỉ số cao nhất và thấp nhất
    highest_stats = max_stats(df, stats)
    lowest_stats = min_stats(df, stats)

    # Hiển thị các chỉ số cao nhất và thấp nhất trong Streamlit
    st.subheader("Pokémon có chỉ số cao nhất và thấp nhất")

    st.write("### Pokémon có chỉ số cao nhất")
    for col, (name, stat, poke_id) in highest_stats.items():
        image_url = get_pokemon_image_url(poke_id)
        st.image(image_url, caption=f"{name} có mức {col} cao là {stat}.")

    st.write("### Pokémon có chỉ số thấp nhất")
    for col, (name, stat, poke_id) in lowest_stats.items():
        image_url = get_pokemon_image_url(poke_id)
        st.image(image_url, caption=f"{name} có mức {col} thấp of {stat}.")

# Trang khác với dữ liệu khác
elif page == "Abilities Dataset":
    st.title("Trang dữ liệu khác")

    # Thêm chức năng tải dữ liệu mới
    @st.cache_data
    def load_another_data():
        return pd.read_csv('D:/Phenikaa/PTData/CK_Poke/API/pokedex/pokemon_abilities.csv')  # Đường dẫn đến file CSV khác

    # Load dữ liệu mới
    new_df = load_another_data()

    # Hiển thị một mẫu dữ liệu
    st.subheader("Sample Data")
    st.write(new_df.head())

    # Hiển thị một mẫu dữ liệu từ abilities
    st.subheader("Sample Data (Abilities)")
    st.write(new_df.head())

    # Các cột liên quan đến type và đối thủ
    types_columns = ['type1', 'against_bug', 'against_dark', 'against_dragon', 'against_electric',
                    'against_fairy', 'against_fight', 'against_fire', 'against_flying',
                    'against_ghost', 'against_grass', 'against_ground', 'against_ice',
                    'against_normal', 'against_poison', 'against_psychic', 'against_rock',
                    'against_steel', 'against_water']

    # Tạo một dataframe chỉ áp dụng với type1 và các chỉ số đối kháng
    types_df = new_df[types_columns]

    # Nhóm dữ liệu theo 'type1' và tính trung bình các cột against_x
    grouped_df = types_df.groupby('type1').mean()

    # Hàm dự đoán loại tốt nhất để đấu
    def predict_strongest_types(input_type):
        against_column = 'against_' + input_type
        against_values = grouped_df[against_column]
        strongest_type = against_values.idxmax()
        return strongest_type

    # Tạo DataFrame dự đoán loại tốt nhất để đối đầu
    predicted_df = pd.DataFrame(columns=['type_opponent', 'type_predicted_best'])
    for column in grouped_df.columns:
        if column.startswith('against_'):
            opponent_type = column.replace('against_', '')
            predicted_best_type = predict_strongest_types(opponent_type)
            new_row = pd.DataFrame({'type_opponent': [opponent_type], 'type_predicted_best': [predicted_best_type]})
            predicted_df = pd.concat([predicted_df, new_row], ignore_index=True)

    # Hiển thị dữ liệu dự đoán
    st.subheader('Loại đối thủ và loại tốt nhất để đấu')
    st.write(predicted_df)

    # Vẽ biểu đồ Sankey
    st.subheader('Biểu đồ Sankey: Loại đối thủ - Loại tốt nhất để đấu')
    fig, ax = plt.subplots(figsize=(12, 10))
    sankey(predicted_df['type_opponent'], predicted_df['type_predicted_best'], fontsize=16)
    plt.title('Opponent Type - Best Type to Choose', fontsize=20)
    plt.gcf().set_size_inches((12, 10))
    st.pyplot()


elif page == "Distribution Pokemon":
    st.title("Trang dữ liệu khác")

    # Thêm chức năng tải dữ liệu mới
    @st.cache_data
    def load_data():
        return pd.read_csv('D:/Phenikaa/PTData/CK_Poke/API/pokedex/pokemon_abilities.csv') 
    # Load dữ liệu mới
    data = load_data()
    st.subheader("Sample Data")
    st.write(data.head())


    # Streamlit app title
    st.title('PCA and Joint Plot of Pokémon Data')

    # Select features for PCA
    features = ['base_total', 'pokedex_number', 'base_egg_steps']

    # Run PCA
    pca = PCA(n_components=3)
    principal_components = pca.fit_transform(data[features])

    # Set up color map and markers
    colormap = plt.get_cmap('Spectral', 8)
    markers = ['o' if value == 0 else '^' for value in data['is_legendary']]

    # 3D PCA Plot
    fig = plt.figure(figsize=(16, 9))
    ax = fig.add_subplot(111, projection='3d')

    for i, marker in enumerate(markers):
        ax.scatter(principal_components[i, 0], principal_components[i, 1], principal_components[i, 2],
                c=colormap(data['generation'][i]), marker=marker, s=20)

    # Labels and title for 3D plot
    ax.set_xlabel('PC1 - Base Egg Steps', fontsize=12)
    ax.set_ylabel('PC2 - Pokedex Number', fontsize=12)
    ax.set_zlabel('PC3 - Base Total', fontsize=12)
    ax.set_title('3D PCA Plot', fontsize=16)

    # Legend for 3D plot
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Non-Legendary', markerfacecolor='black', markersize=8),
        Line2D([0], [0], marker='^', color='w', label='Legendary', markerfacecolor='black', markersize=8)
    ]
    ax.legend(handles=legend_elements)

    # Color bar
    sm = ScalarMappable(cmap=colormap)
    sm.set_array([])  # Set an empty array to avoid warnings
    cbar = plt.colorbar(sm, ax=ax)  # Associate color bar with the PCA plot's axis
    cbar.set_ticks(range(1, 8))
    cbar.set_label('Generation')
    # Show PCA plot in Streamlit
    st.pyplot(fig)

    # Split data by mean
    below_mean = data[data['base_total'] < data['base_total'].mean()]
    above_mean = data[data['base_total'] >= data['base_total'].mean()]

    # Joint plot
    g = sns.jointplot(data=data, x='base_total', y='pokedex_number', kind='kde', hue='is_legendary')
    g.ax_joint.axvline(below_mean['base_total'].mean(), color='black', linestyle='--', label='Below Average')
    g.ax_joint.axvline(above_mean['base_total'].mean(), color='red', linestyle='--', label='Above Average')

    # Legend for joint plot
    g.ax_joint.legend(['Below Average', 'Above Average'])

    # Show joint plot in Streamlit
    st.pyplot(g.fig)

    # Add a title for the joint plot
    st.subheader('Joint Plot of Base Total and Pokedex Number')