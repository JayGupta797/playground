'''
NAME: wordcloud_generator.py
DESCRIPTION: This script generates a word cloud from a pre-processed text file using the WordCloud library. 
The word frequencies are calculated from the text, and the word cloud is shaped according to a specified mask image. 
The resulting word cloud is saved as an SVG file.
'''

# Import libraries
import numpy as np
from PIL import Image
from os import path, getcwd
import os
from wordcloud import WordCloud, ImageColorGenerator

# Get the data directory
d = path.dirname(__file__) if "__file__" in locals() else getcwd()

# Read the pre-processed text from file
with open(path.join(d, './assets/shortGita.txt'), 'r', encoding='utf-8') as file:
    text = file.readlines()

# Create a dictionary to count word frequencies
word_freq = {}
for word in text:
    word = word.strip()
    word_freq[word] = word_freq.get(word, 0) + 1
word_freq.pop('', None)

# Load custom mask
mask = np.array(Image.open("./assets/download.png"))

# Generate the word cloud
image_colors = ImageColorGenerator(mask)
wc = WordCloud(
    # font_path="./assets/Sanskrit2003.ttf", 
    background_color=None, 
    mask=mask, 
    max_words=10000, 
    random_state=1, 
    mode="RGBA"
).fit_words(word_freq)
wc.recolor(color_func=image_colors)

# Save the word cloud as an SVG file
wc_svg = wc.to_svg(embed_font=True)
with open("gita.svg", "w+", encoding='utf-8') as f:
    f.write(wc_svg)