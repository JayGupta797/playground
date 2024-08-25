#!/usr/bin/env python
# coding: utf-8

import os
from os import path, getcwd

import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

# Get the data directory
d = path.dirname(__file__) if '__file__' in locals() else getcwd()

# Read the pre-processed text from file
with open(path.join(d, './assets/generated/clean-text.txt'), 'r', encoding='utf-8') as file:
    text = file.readlines()

# Create a dictionary to count word frequencies
word_freq = {}
for word in text:
    word = word.strip()
    word_freq[word] = word_freq.get(word, 0) + 1
word_freq.pop('', None)

# Load custom mask
mask = np.array(Image.open('./assets/generated/clean-background.png'))

# Generate the word cloud
image_colors = ImageColorGenerator(mask)
wc = WordCloud(
    background_color=None, 
    mask=mask, 
    max_words=10000, 
    random_state=1, 
    mode='RGBA'
).fit_words(word_freq)
wc.recolor(color_func=image_colors)

# Save the word cloud as an SVG file
wc_svg = wc.to_svg(embed_font=True)
with open('output.svg', 'w+', encoding='utf-8') as f:
    f.write(wc_svg)