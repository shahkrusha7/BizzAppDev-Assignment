# Text Analysis Tool
#
# This program analyzes a block of text:
# - Counts how often each word appears (ignoring common stop words)
# - Lets you quickly find the most frequent words that start with a given prefix
# - Optimized for speed using built-in data structures

import re
from collections import defaultdict, Counter

# List of common words to ignore (stop words)
STOP_WORDS = {"the", "is", "at", "on", "in", "and", "a", "an", "to", "of", "for", "with", "that", "this", "it"}

def clean_and_tokenize(text):
    # Remove punctuation, make lowercase, and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    return [word for word in words if word not in STOP_WORDS]

def build_word_frequency(words):
    return Counter(words)

def top_k_with_prefix(word_freq, prefix, k):
    # Filter words that start with the prefix
    filtered = [(word, freq) for word, freq in word_freq.items() if word.startswith(prefix)]
    # Sort by frequency (highest first), then alphabetically
    filtered.sort(key=lambda x: (-x[1], x[0]))
    return filtered[:k]

# --- Example usage ---

text = """
Learning Python is fun and rewarding. Many people use Python to build websites, analyze data, 
automate tasks, and create games. It is one of the most popular programming languages today. 
With clear syntax and a large community, Python is a great choice for beginners and professionals alike.
"""

words = clean_and_tokenize(text)
word_freq = build_word_frequency(words)

# Example query: top 3 words starting with 'a'
results = top_k_with_prefix(word_freq, "p", 3)

print("Top 3 words starting with 'a':")
for word, freq in results:
    print(f"{word}: {freq}")
