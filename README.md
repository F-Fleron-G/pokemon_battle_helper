# Pokémon Battle Helper

Welcome to the **Pokémon Battle Helper**, a FastAPI-based application designed to help kids build Pokémon battle decks and optimize their strategies! This app connects to a PostgreSQL database for managing user accounts, Pokémon data, and battle decks, offering an educational and fun experience for young Pokémon enthusiasts.

---

## Features
- **Pokémon Data**: Search and retrieve detailed Pokémon stats, types, strengths, weaknesses, and moves.
- **Build Battle Decks**: Create and manage Pokémon decks for battles.
- **Suggestions**: Get recommendations on the most effective Pokémon to include in your deck.
- **User Authentication**: Secure user accounts using JWT-based authentication.

---

## Technologies
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JSON Web Tokens (JWT)
- **Deployment**: (Planned for future development)

---

## Setup Instructions

### Prerequisites
- Python 3.10+ installed on your system.
- PostgreSQL installed and running.

### Step 1: Clone the Repository
```bash
git clone https://github.com/F-Fleron-G/pokemon_battle_helper.git
cd pokemon_battle_helper
```

### Step 2: Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a .env file in the root folder with the following content:
```env
DATABASE_URL=postgresql://postgres:<your_password>@localhost/pokemon_battle_helper
```
Replace <your_password> with your PostgreSQL postgres user's password.

### Step 5: Start the Application
Run the FastAPI application:
```bash
uvicorn main:app --reload
```
Open your browser and visit http://127.0.0.1:8000 to access the app.

---

## Endpoints Overview
- Root: GET / - Welcome message.
- About: GET /about - App details.
- Pokémon Search: GET /pokemon/{name} - Retrieve details for a specific Pokémon.
- Filter Pokémon: GET /pokemon/{name}/filter - Filter Pokémon by type.

---

## Future Enhancements
- Add frontend interface for kids to easily interact with the app.
- Implement advanced Pokémon suggestion algorithms.
- Deploy the application on a cloud platform (e.g., Render, AWS).

---

## Credits
- Pokémon data sourced from PokeAPI.
- Built by Frederic G. Fleron Grignard.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
