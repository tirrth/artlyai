from flask import Flask, render_template, request, send_file
from text_to_image_generator import generate_image
import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', '/generate', methods=['POST'])
def generate():
    # Get the text input from the user.
    text = request.form.get('text', '')

    # Generate the image based on the text input.
    img = generate_image(text)

    # Convert the image to PNG format and send it as a response.
    img_data = io.BytesIO()
    img.save(img_data, format='PNG')
    img_data.seek(0)
    return send_file(img_data, mimetype='image/png', as_attachment=True, attachment_filename='generated_art.png')


if __name__ == '__main__':
    app.run(debug=True)
