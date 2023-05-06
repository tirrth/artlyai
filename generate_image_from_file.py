import os
import requests
import json

def generate_image_from_file(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read().strip()

    api_key = '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'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    payload = {
        'prompt': text,
        'n': 1,
        'size': '1024x1024'
    }

    response = requests.post('https://api.openai.com/v1/images/generations', headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        image_url = response.json()['data'][0]['url']
        # Download and save the image to output_file
        img_response = requests.get(image_url)
        with open(output_file, 'wb') as f:
            f.write(img_response.content)
    else:
        print("Error:", response.status_code, response.text)

if __name__ == '__main__':
    input_folder = '/Users/tirth/Documents/final-py/project/files'
    output_folder = '/Users/tirth/Documents/final-py/project/files'

    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    input_file = os.path.join(input_folder, 'input.txt')
    output_file = os.path.join(output_folder, 'generated_art.png')

    generate_image_from_file(input_file, output_file)
