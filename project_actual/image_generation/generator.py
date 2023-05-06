import torch
import io
import numpy as np
from PIL import Image
import clip
from model import load_pretrained_model

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load the CLIP model
clip_model, preprocess = clip.load('ViT-B/32', device=device)

# Load the pre-trained art StyleGAN2 model
model = load_pretrained_model(device=device)

class TextToImageGenerator:
    def generate_image(self, text, truncation=0.5, num_images=1):
        # Tokenize the text input
        tokens = clip.tokenize([text]).to(device)

        # Calculate the text features using CLIP
        with torch.no_grad():
            text_features = clip_model.encode_text(tokens).float()

        # Optimize the latent vector to generate images that match the text features
        latent = torch.randn(num_images, 512).to(device).requires_grad_()
        optimizer = torch.optim.Adam([latent], lr=0.05)

        for _ in range(200):
            optimizer.zero_grad()

            with torch.no_grad():
                latent_numpy = latent.cpu().numpy()
                images = model(latent, None, truncation)

            image_input = torch.stack([preprocess(img)
                                      for img in images]).to(device)
            image_features = clip_model.encode_image(image_input)

            loss = -torch.cosine_similarity(text_features, image_features).mean()
            loss.backward()
            optimizer.step()

        # Generate the final images
        with torch.no_grad():
            generated_images = model(latent, None, truncation)
            generated_images = [(img.permute(1, 2, 0) * 127.5 + 128).clamp(0,
                                                                           255).to(torch.uint8).cpu().numpy() for img in generated_images]
            generated_images = [Image.fromarray(
                img, 'RGB') for img in generated_images]

        return generated_images[0]
