from flask import Flask, render_template
import json

app = Flask(__name__)

def load_assets():
    try:
        with open("assets.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("forex", [])
    except Exception as e:
        print("Помилка завантаження assets.json:", e)
        return []

@app.route("/")
def index():
    assets = load_assets()
    selected_asset = assets[0] if assets else {"name": "EUR/USD", "symbol": "EURUSD"}
    return render_template("index.html", selected_asset=selected_asset, assets=assets)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=10000)
