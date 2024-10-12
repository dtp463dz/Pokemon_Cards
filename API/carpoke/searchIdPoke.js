class PokemonCard {
    static baseUrl = "https://api.pokemontcg.io/v2/cards/";

    static find(cardId) {
        return fetch(this.baseUrl + cardId)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Card not found');
                }
                return response.json();
            })
            .then(data => {
                return data.data; // Trả về đối tượng 'data'
            })
            .catch(error => {
                console.error('Error:', error);
                return null;
            });
    }
}

document.getElementById('find-card').addEventListener('click', () => {
    const cardId = document.getElementById('card-id').value;
    if (cardId) {
        PokemonCard.find(cardId).then(card => {
            if (card) {
                // Hiển thị thông tin thẻ
                document.getElementById('card-info').innerHTML = `
                    <img src="${card.images.large}" alt="${card.name}">
                    <p><strong>Name:</strong> ${card.name}</p>
                    <p><strong>Set:</strong> ${card.set.name}</p>
                    <p><strong>Type:</strong> ${card.types ? card.types.join(', ') : 'N/A'}</p>
                    <div class="prices">
                        <h3>Prices (from TCGPlayer):</h3>
                        <p><strong>Normal:</strong> $${card.cardmarket?.prices?.averageSellPrice || 'N/A'}</p>
                        <p><strong>Holofoil:</strong> $${card.tcgplayer?.prices?.holofoil?.market || 'N/A'}</p>
                        <p><strong>Reverse Holofoil:</strong> $${card.tcgplayer?.prices?.reverseHolofoil?.market || 'N/A'}</p>
                    </div>
                `;
            } else {
                document.getElementById('card-info').innerHTML = `<p>Card not found.</p>`;
            }
        });
    }
});