import os
import json
import requests
from os import environ
from flask import Flask, request, render_template

app = Flask(__name__)

OPENAI_API_KEY = environ.get('OPENAI_API_KEY')  # Make sure to set this environment variable or replace it with your actual API key
print(OPENAI_API_KEY)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None

    if request.method == 'POST':
        text = request.form.get('text')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {OPENAI_API_KEY}',
        }

        payload = {
            'prompt': text,
            'n': 1,
            'size': '1024x1024',
        }

        response = requests.post('https://api.openai.com/v1/images/generations', headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            image_url = response.json()['data'][0]['url']

    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)