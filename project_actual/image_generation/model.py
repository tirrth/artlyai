import torch
from torch import nn
from torch.nn import functional as F
import numpy as np


class Generator(nn.Module):
    def __init__(self, G):
        super(Generator, self).__init__()
        self.G = G

    def forward(self, z, truncation=0.5):
        with torch.no_grad():
            # Generate images using the pre-trained StyleGAN2 model
            images = self.G.test(z, truncation)
        return images


def load_pretrained_model(device='cpu'):
    # Load the pre-trained StyleGAN2 model.
    G = torch.hub.load('facebookresearch/pytorch_GAN_zoo:hub', 'PGAN', model_name='celebAHQ-512', pretrained=True, useGPU=torch.cuda.is_available())

    # Wrap the loaded model with the custom Generator class
    model = Generator(G).to(device)
    model.eval()

    return model
