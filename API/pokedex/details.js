// Lấy tham số id từ URL
const urlParams = new URLSearchParams(window.location.search);
const pokemonId = urlParams.get('id');

// Đường dẫn đến file JSON chứa dữ liệu Pokémon
const jsonUrl = 'pokemonData.json';

const colors = {
    fire: '#FDDFDF',      // Lửa
    grass: '#DEFDE0',     // Cỏ
    electric: '#FCF7DE',  // Điện
    water: '#DEF3FD',     // Nước
    ground: '#f4e7da',    // Đất
    rock: '#d5d5d4',      // Đá
    fairy: '#fceaff',     // Tiên
    poison: '#98d7a5',    // Độc
    bug: '#f8d5a3',       // Sâu bọ
    dragon: '#97b3e6',    // Rồng
    psychic: '#eaeda1',   // Tâm linh
    flying: '#F5F5F5',    // Bay
    fighting: '#E6E0D4',  // Đối kháng
    normal: '#F5F5F5'     // Bình thường
};

// Hàm để hiển thị chi tiết Pokémon
const showPokemonDetails = (pokemon) => {
    const pokemonDetailDiv = document.getElementById('pokemonDetail');

    // Lấy màu dựa trên loại (Type) của Pokémon
    const typeColor = colors[pokemon.Type.toLowerCase()] || '#F5F5F5'; // Mặc định màu trắng nếu không tìm thấy loại

    // Tạo nội dung HTML cho chi tiết Pokémon
    const detailHTML = `
        <div class="pokemon-detail" style="background-color: ${typeColor}; border-radius: 15px; padding: 20px;">
            <h2>${pokemon.Name}</h2>
            <img src="${pokemon.image_url}" alt="${pokemon.Name}" style="max-width: 200px;">
            <p><strong>Type:</strong> ${pokemon.Type}</p>
            <p><strong>Total Stats:</strong> ${pokemon.Total}</p>
            <p><strong>HP:</strong> ${pokemon.HP}</p>
            <p><strong>Attack:</strong> ${pokemon.Attack}</p>
            <p><strong>Defense:</strong> ${pokemon.Defense}</p>
            <p><strong>Sp.Atk:</strong> ${pokemon["Sp.Atk"]}</p>
            <p><strong>Sp.Def:</strong> ${pokemon["Sp.Def"]}</p>
            <p><strong>Speed:</strong> ${pokemon.Speed}</p>
        </div>
    `;

    // Gắn HTML vào thẻ div chi tiết Pokémon
    pokemonDetailDiv.innerHTML = detailHTML;
};

// Hàm để tìm Pokémon theo ID trong file JSON
const getPokemonById = async (id) => {
    const response = await fetch(jsonUrl);
    const data = await response.json();

    // Tìm Pokémon có id tương ứng
    const pokemon = data.find(p => parseInt(p["#"]) === parseInt(id));

    // Hiển thị chi tiết Pokémon nếu tìm thấy
    if (pokemon) {
        showPokemonDetails(pokemon);
    } else {
        document.getElementById('pokemonDetail').innerHTML = '<p>Pokémon not found!</p>';
    }
};

// Gọi hàm tìm Pokémon theo ID
getPokemonById(pokemonId);
