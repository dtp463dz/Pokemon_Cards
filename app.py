import streamlit as st
import requests

# Hàm lấy tất cả các thẻ Pokémon
def get_all_cards():
    url = "https://api.pokemontcg.io/v2/cards?pageSize=20"
    response = requests.get(url)
    if response.ok:
        return response.json()['data']
    else:
        st.error("Failed to fetch cards")
        return []

# Hàm tìm kiếm thẻ Pokémon
def search_card(query):
    url = f"https://api.pokemontcg.io/v2/cards?q=name:{query}* OR id:{query}*"
    response = requests.get(url)
    if response.ok:
        return response.json()['data']
    else:
        st.error("No cards found")
        return []

# Hàm hiển thị các thẻ Pokémon
def display_cards(cards):
    for card in cards:
        st.subheader(card['name'])
        st.image(card['images']['small'], width=100)
        st.write(f"Set: {card['set']['name']}")

        # Kiểm tra và hiển thị giá
        normal_price = card['cardmarket']['prices'].get('averageSellPrice', 'N/A')
        holofoil_price = card['tcgplayer']['prices'].get('holofoil', {}).get('market', 'N/A')
        reverse_holofoil_price = card['tcgplayer']['prices'].get('reverseHolofoil', {}).get('market', 'N/A')

        st.write(f"Normal Price: ${normal_price}")
        st.write(f"Holofoil Price: ${holofoil_price if holofoil_price != 'N/A' else 'N/A'}")
        st.write(f"Reverse Holofoil Price: ${reverse_holofoil_price if reverse_holofoil_price != 'N/A' else 'N/A'}")
        st.markdown("---")

# Tiêu đề trang
st.title("Pokemon Cards Gallery")

# Phần tìm kiếm
search_query = st.text_input("Enter card name or ID")
if st.button("Search"):
    if search_query:
        cards = search_card(search_query)
        display_cards(cards)
    else:
        st.warning("Please enter a search query.")

# Phần lấy tất cả thẻ Pokémon khi không tìm kiếm
if not search_query:
    all_cards = get_all_cards()
    display_cards(all_cards)
