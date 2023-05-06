# from flask import Flask, render_template, request, send_file
# from text_to_image_generator import generate_image
# import io

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/generate', methods=['POST'])
# def generate():
#     # Get the text input from the user.
#     text = request.form.get('text', '')

#     # Generate the image based on the text input.
#     img = generate_image(text)

#     # Convert the image to PNG format and send it as a response.
#     img_data = io.BytesIO()
#     img.save(img_data, format='PNG')
#     img_data.seek(0)
#     return send_file(img_data, mimetype='image/png', as_attachment=True, attachment_filename='generated_art.png')


# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, send_file
# from text_to_image_generator import generate_image

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         prompt = request.form['prompt']
#         image = generate_image(prompt)
#         image.save('static/generated_image.jpg')
#         return send_file('static/generated_image.jpg', mimetype='image/jpeg')
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)


import os
import json
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

OPENAI_API_KEY = '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'  # Make sure to set this environment variable or replace it with your actual API key

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