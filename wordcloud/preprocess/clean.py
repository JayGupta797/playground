#!/usr/bin/env python
# coding: utf-8

# Import string utility
from boltons.strutils import split_punct_ws

# Read Sanskrit text from file
with open('../assets/gita.txt', 'r', encoding='utf-8') as fhand:
    text = fhand.read()

# Read stopwords from file
with open('../assets/stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set(file.read().splitlines())

# Split tokens by whitespace and punctuation
tokens = split_punct_ws(text)
print(f'There are {len(tokens)} tokens in the original')

# Filter out stopwords and special characters
filtered_tokens = [token for token in tokens if token not in stopwords and '॥' not in token]
print(f'There are {len(filtered_tokens)} tokens with stopwords removed')

# Write filtered tokens to a new file
with open('../assets/generated/clean-text.txt', 'w', encoding='utf-8') as f:
    for word in filtered_tokens:
        f.write(word + '\n')