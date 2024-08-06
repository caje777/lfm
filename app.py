from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)

API_KEY = 'YOUR_LASTFM_API_KEY'
USER = 'YOUR_LASTFM_USERNAME'

def fetch_lastfm_data():
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={USER}&api_key={API_KEY}&format=json'
    response = requests.get(url)
    data = response.json()
    with open('data/lastfm_data.json', 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    with open('data/lastfm_data.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    fetch_lastfm_data()
    app.run(debug=True)
