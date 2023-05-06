import os
from image_generation.generator import TextToImageGenerator

def generate_image_from_file(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read().strip()

    generator = TextToImageGenerator()
    img = generator.generate_image(text)
    img.save(output_file, format='PNG')

if __name__ == '__main__':
    input_folder = 'files'
    output_folder = 'files'

    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    input_file = os.path.join(input_folder, 'input.txt')
    output_file = os.path.join(output_folder, 'generated_art.png')

    generate_image_from_file(input_file, output_file)
