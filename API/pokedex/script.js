// Lấy phần tử chứa Pokémon từ DOM
const pokeContainer = document.querySelector("#pokeContainer");

// Số lượng Pokémon cần lấy
const pokemonCount = 150;

// Định nghĩa màu sắc cho các loại Pokémon
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

// Lấy danh sách các loại Pokémon
const mainTypes = Object.keys(colors);

// Hàm để lấy thông tin của tất cả Pokémon
const fetchPokemons = async () => {
    for (let i = 1; i <= pokemonCount; i++) {
        await getPokemons(i); // Gọi hàm lấy thông tin Pokémon theo ID
    }
};

// Hàm để lấy thông tin của một Pokémon theo ID
const getPokemons = async (id) => {
    // Đường dẫn API để lấy thông tin Pokémon
    const url = `https://pokeapi.co/api/v2/pokemon/${id}`;
    const resp = await fetch(url); // Gọi API và chờ phản hồi
    const data = await resp.json(); // Chuyển đổi phản hồi sang định dạng JSON
    createPokemonCard(data)
    // console.log(data)
};

const createPokemonCard = (poke) => {
    const card = document.createElement('div')
    card.classList.add("pokemon")

    const name = poke.name[0].toUpperCase() + poke.name.slice(1)
    const id = poke.id.toString().padStart(3, '0')

    const pokeTypes = poke.types.map(type => type.type.name)
    const type = mainTypes.find(type => pokeTypes.indexOf(type) > -1)
    const color = colors[type]

    card.style.backgroundColor = color
    
    const pokemonInnerHTML = `
        <div class="imgContainer">
            <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${poke.id}.png" alt="${name}">
    
        </div>
        <div class="info">
            <span class="number">#${id}</span>
            <h3 class="name">${name}</h3>
            <small class="type">Type: <span>${type}</span></small>
        </div>
    `
    
    card.innerHTML = pokemonInnerHTML

    pokeContainer.appendChild(card)
}

// Gọi hàm để bắt đầu quá trình lấy thông tin Pokémon
fetchPokemons();