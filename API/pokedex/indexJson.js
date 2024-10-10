// Lấy dữ liệu từ file JSON
fetch('pokemonData.json')
    .then(response => response.json())
    .then(data => {
        const pokemonList = document.getElementById('pokemon-list');
        const loadingElement = document.getElementById('loading');

        // Ẩn thông báo loading sau khi dữ liệu được tải
        loadingElement.style.display = 'none';

        // Hiển thị danh sách Pokémon
        data.forEach(pokemon => {
            // Tạo thẻ HTML cho từng Pokémon
            const pokemonCard = document.createElement('div');
            pokemonCard.classList.add('pokemon-card');

            pokemonCard.innerHTML = `
                <img src="${pokemon.image_url}" alt="${pokemon.Name}">
                <div class="pokemon-name">${pokemon.Name}</div>
                <div class="pokemon-type">Type: ${pokemon.Type}</div>
                <div class="pokemon-stats">
                    <p>Total: ${pokemon.Total}</p>
                    <p>HP: ${pokemon.HP}</p>
                    <p>Attack: ${pokemon.Attack}</p>
                    <p>Defense: ${pokemon.Defense}</p>
                    <p>Sp.Atk: ${pokemon["Sp.Atk"]}</p>
                    <p>Sp.Def: ${pokemon["Sp.Def"]}</p>
                    <p>Speed: ${pokemon.Speed}</p>
                </div>
            `;

            // Thêm card vào danh sách
            pokemonList.appendChild(pokemonCard);
        });
    })
    .catch(error => {
        // Hiển thị lỗi nếu có
        console.error('Error fetching Pokémon data:', error);
        document.getElementById('loading').textContent = 'Failed to load data';
    });
