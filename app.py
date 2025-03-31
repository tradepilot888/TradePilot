from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('assets.json', 'r') as file:
        assets = json.load(file)['forex']
    return render_template('index.html', assets=assets)

if __name__ == '__main__':
    app.run(debug=True)
