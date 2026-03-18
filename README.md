# Clash Royale Deck Analyzer

A Flask-based web application that analyzes Clash Royale player decks and collections using the official Clash Royale API.

![Flask](https://img.shields.io/badge/Flask-2.0+-blue) ![Python](https://img.shields.io/badge/Python-3.6+-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎮 Features

### Deck Analysis
- Fetch and display a player's current deck
- Calculate average elixir cost
- Detect deck archetype (Beatdown, Control, Siege, Cycle, etc.)
- Categorize cards by role (Win Conditions, Tanks, Spells, Buildings, etc.)
- F2P (Free-to-Play) scoring system
- Deck warnings (missing spells, buildings, win conditions)

### Card Collection Viewer
- Browse all available cards in the game
- View player's card collection with levels
- Visual rarity-based styling (Common, Rare, Epic, Legendary, Champion)

### Card Management
- View all game cards with detailed information
- Rarity-based card displays with unique styling
- Interactive card grids with hover effects

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Jinja2 templates
- **API**: Clash Royale API v1
- **Styling**: Night mode / dark theme with modern UI

## 📦 Requirements

```txt
Flask==2.3.2
requests==2.31.0
python-dotenv
```

## 🔧 Installation

1. Clone or download the project files
2. Install dependencies:
   ```bash
   pip install flask requests python-dotenv
   ```

3. Create a `.env` file in the root directory with your Clash Royale API token:
   ```
   CLASH_API_TOKEN=your_api_token_here
   ```

   To get an API token:
   - Visit [Clash Royale for Developers](https://developer.clashroyale.com)
   - Create an account and log in
   - Create a new API token
   - Copy your token to the `.env` file

## 🚀 Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Features available:
   - **Deck Analysis**: Enter a player tag (e.g., `#2GY9JCJYP`) to analyze their current deck
   - **My Collection**: Enter a player tag to view their full card collection
   - **All Cards**: Browse all cards available in the game

## 📁 Project Structure

```
DECK/
├── app.py                      # Main Flask application
├── test.py                     # Test script for API connectivity
├── .env                        # Environment variables (API token)
├── requirements.txt           # Project dependencies
├── cards.json                 # Game card data (all cards)
├── leaderboard.json          # Arena/leaderboard data
├── card_roles.json           # Card categorization mapping
├── static/
│   └── style.css             # CSS styling
├── templates/
│   ├── base.html             # Base template
│   ├── index.html            # Home/redirect page
│   ├── deck.html             # Deck analysis template
│   ├── collection.html       # Collection viewer template
│   └── cards.html            # All cards viewer template
└── README.md                 # This file
```

## 🎨 Features in Detail

### Deck Archetype Detection
The app automatically detects deck archetypes including:
- **Beatdown**: Heavy tank decks (Golem, Lava Hound, etc.)
- **Siege**: X-Bow or Mortar decks
- **Control**: Decks with multiple spells
- **Fast Cycle**: Low elixir cost decks (≤3.2)
- **Balloon Cycle**: Balloon with low elixir
- **Mixed / Off-Meta**: Non-standard combinations

### Card Categories
Cards are categorized into:
- Primary Win Condition
- Secondary Win Condition
- Spells (small and big)
- Buildings
- Tanks / Mini-Tanks
- Ranged Support
- Swarm / Cycle
- Champions
- Heavy Units
- Support Units

### Rarity Styling
Cards are visually distinguished by rarity:
- **Common**: Gray borders
- **Rare**: Orange borders with glow
- **Epic**: Purple borders with glow
- **Legendary**: Animated gradient borders
- **Champion**: Gold borders with glow

## 🔐 API Configuration

The app uses the Clash Royale API with Bearer token authentication. Ensure your token has:
- `royale` scope access
- Valid IP restrictions (if configured)
- Proper rate limit handling

## 🧪 Testing

Run the provided test script to verify API connectivity:
```bash
python test.py
```

This tests basic API access and saves sample data to `leaderboard.json`.

## 🤝 Contributing

1. Fork the project
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This is an unofficial project and is not affiliated with or endorsed by Supercell. Clash Royale and its assets are trademarks of Supercell Oy. For more information, see Supercell's [Fan Content Policy](https://supercell.com/en/fan-content-policy/).

---

**Enjoy analyzing your Clash Royale decks!** 🎮
