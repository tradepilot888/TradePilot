from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

# Завантаження списку активів з файлу
with open("assets.json", "r") as file:
    ASSETS = json.load(file)

@app.route('/')
def index():
    selected_asset = request.args.get('asset', 'EURUSD')
    return render_template('index.html', selected_asset=selected_asset, assets=ASSETS)

# Запуск з правильним портом
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
