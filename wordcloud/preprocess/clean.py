'''
NAME: wordcloud_generator.py
DESCRIPTION: This script reads a Sanskrit text file, tokenizes it by splitting on whitespace and punctuation,
filters out specified stopwords and special characters, and writes the filtered tokens to a new file.
'''

# Import string utility
from boltons.strutils import split_punct_ws

# Read stopwords from file
def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return set(file.read().splitlines())

# Load stopwords
stopwords = load_stopwords('../assets/stopwords.txt')

# Read Sanskrit Text from file
with open('../assets/gita.txt', 'r', encoding='utf-8') as fhand:
    text = fhand.read()

# Split tokens by whitespace and punctuation
tokens = split_punct_ws(text)
print(f'There are {len(tokens)} tokens in the original')

# Filter out stopwords and special characters
filtered_tokens = [token for token in tokens if token not in stopwords and '॥' not in token]
print(f'There are {len(filtered_tokens)} tokens with stopwords removed')

# Write filtered tokens to a new file
with open('../assets/shortGita.txt', 'w', encoding='utf-8') as f:
    for word in filtered_tokens:
        f.write(word + '\n')