from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Meme API URL
MEME_API_URL = "https://api.imgflip.com/get_memes"

@app.route('/')
def home():
    """Home page showing a random meme."""
    # Fetch memes from API
    response = requests.get(MEME_API_URL)
    if response.status_code == 200:
        memes = response.json()["data"]["memes"]
    else:
        memes = []

    # Pick a random meme
    import random
    selected_meme = random.choice(memes) if memes else None

    return render_template("index.html", meme=selected_meme)

if __name__ == "__main__":
    app.run(debug=True)
