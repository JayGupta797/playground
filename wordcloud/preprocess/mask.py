#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import numpy as np

# Load the image and convert it to a numpy array
pim = Image.open('../assets/webb.png').convert('RGB')
im = np.asarray(pim, dtype="int32")

# Extract image dimensions
width, height = pim.size

# Define color range
from_color = [0, 0, 0]
to_color = [100, 100, 100]

# Extract pixels in color range and replace with white
copy = im.copy()
mask = (im >= from_color).all(axis=-1) & (im <= to_color).all(axis=-1)
copy[mask] = [255, 255, 255]

# Save the resulting image
output_image = Image.fromarray(copy.astype(np.uint8))
output_image.save('./assets/generated/clean-background.png')