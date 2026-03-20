from flask import Flask, render_template, request, redirect, url_for
import json
import requests
import os

app = Flask(__name__)

# ---------- API CONFIG ----------

API_TOKEN = os.getenv("CLASH_API_TOKEN", ".env")  # safer
API_BASE = "https://proxy.royaleapi.dev/v1"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# ---------- DATA HELPERS ----------

def load_card_roles():
    with open("card_roles.json", "r", encoding="utf-8") as f:
        return json.load(f)

CARD_ROLES = load_card_roles()

def infer_role(card):
    elixir = card.get("elixirCost", 0)
    rarity = card.get("rarity")
    name = card.get("name", "")

    if rarity == "champion":
        return "Champions"

    if name in CARD_ROLES.get("spells", []):
        return "Spells"

    if name in CARD_ROLES.get("buildings", []):
        return "Buildings"

    if elixir >= 6:
        return "Heavy Units"

    if elixir <= 2:
        return "Cycle Cards"

    return "Support Units"


def load_cards():
    with open("cards.json", "r", encoding="utf-8") as f:
        return json.load(f)["items"]

def fetch_player(tag):
    if not tag:
        return None

    tag = tag.replace("#", "%23")
    url = f"{API_BASE}/players/{tag}"

    print(f"DEBUG: Fetching player from {url}")
    print(f"DEBUG: Using API_BASE: {API_BASE}")
    print(f"DEBUG: Token set: {bool(API_TOKEN)}")
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        if res.status_code == 200:
            print(f"DEBUG: Response status: {res.status_code}")
            return res.json()
            print(f"DEBUG: Error response: {res.text[:200]}")
    except requests.RequestException as e:
        print(f"DEBUG: Exception = {e}")
        pass

    return None

def calculate_average_elixir(deck):
    if not deck:
        return 0
    total = sum(card.get("elixirCost", 0) for card in deck)
    return round(total / len(deck), 1) if deck else 0

def calculate_f2p_score(deck):
    weights = {
        "common": 3,
        "rare": 2,
        "epic": 1,
        "legendary": 0,
        "champion": -1
    }
    return (sum(weights.get(card.get("rarity"), 0) for card in deck)/24)*100

def get_deck_warnings(categories):
    warnings = []

    # No building
    if not categories.get("Buildings"):
        warnings.append("❗ No building")

    # Spells
    spells = categories.get("Spells", [])
    small_spells = [
        c for c in spells
        if c.get("elixirCost", 10) <= 2
    ]
    big_spells = [
        c for c in spells
        if c.get("elixirCost", 0) >= 4
    ]

    if len(small_spells) == 0:
        warnings.append("❗ No small spell")

    if len(big_spells) == 0:
        warnings.append("❗ No big spell")

    # Win conditions
    if not categories.get("Primary Win Condition"):
        warnings.append("❗ No clear win condition")

    return warnings


# ---------- CARD CATEGORIES ----------

def categorize_deck(deck):
    categories = {
        "Primary Win Condition": [],
        "Secondary Win Condition": [],
        "Spells": [],
        "Buildings": [],
        "Tanks / Mini-Tanks": [],
        "Ranged Support": [],
        "Swarm / Cycle": [],
        "Champions": [],
        "Heavy Units": [],
        "Cycle Cards": [],
        "Support Units": []
    }

    role_map = {
        "primary_win": "Primary Win Condition",
        "secondary_win": "Secondary Win Condition",
        "spells": "Spells",
        "buildings": "Buildings",
        "tanks": "Tanks / Mini-Tanks",
        "ranged_support": "Ranged Support",
        "swarm_cycle": "Swarm / Cycle",
        "champions": "Champions"
    }

    for card in deck:
        name = card["name"]
        placed = False

        for role_key, card_list in CARD_ROLES.items():
            if name in card_list:
                categories[role_map[role_key]].append(card)
                placed = True

        if not placed:
            inferred = infer_role(card)
            categories[inferred].append(card)

    return categories

def detect_archetype(deck, categories, avg_elixir):
    names = {c["name"] for c in deck}

    # Siege
    if "X-Bow" in names or "Mortar" in names:
        return "Siege"

    # Beatdown
    beatdown_cards = {
        "Golem", "Lava Hound", "Electro Giant",
        "Goblin Giant", "Mega Knight"
    }
    if names & beatdown_cards:
        return "Beatdown"

    # Balloon cycle / pressure
    if "Balloon" in names and avg_elixir <= 3.8:
        return "Balloon Cycle / Pressure"

    # Cycle
    if avg_elixir <= 3.2:
        return "Fast Cycle"

    # Control
    if len(categories.get("Spells", [])) >= 2:
        return "Control"

    return "Mixed / Off-Meta"



# ---------- ROUTES ----------

@app.route("/")
def home():
    return redirect(url_for("deck_analysis"))

@app.route("/cards")
def all_cards():
    cards = load_cards()
    return render_template("cards.html", cards=cards)

@app.route("/deck", methods=["GET", "POST"])
def deck_analysis():
    deck = []
    avg_elixir = 0
    f2p_score = 0
    categories = {}
    error = None
    warnings = None
    archetype = None


    if request.method == "POST":
        tag = request.form.get("player_tag")
        player = fetch_player(tag)

        if player:
            deck = player.get("currentDeck", [])
            avg_elixir = calculate_average_elixir(deck)
            f2p_score = calculate_f2p_score(deck)
            categories = categorize_deck(deck)
            warnings = get_deck_warnings(categories)
            archetype = detect_archetype(deck, categories, avg_elixir)            
        else:
            error = "Invalid player tag or API error"

    return render_template(
        "deck.html",
        deck=deck,
        avg_elixir=avg_elixir,
        f2p_score=f2p_score,
        categories=categories,
        warnings=warnings,
        archetype=archetype,
        error=error
    )

@app.route("/collection", methods=["GET", "POST"])
def collection():
    cards = []
    error = None

    if request.method == "POST":
        tag = request.form.get("player_tag")
        player = fetch_player(tag)

        if player:
            cards = player.get("cards", [])
            print(cards)
        else:
            error = "Invalid player tag or API error"

    return render_template(
        "collection.html",
        cards=cards,
        error=error
    )

# ---------- RUN ----------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
