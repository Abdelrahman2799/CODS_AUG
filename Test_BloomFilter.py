from Bloom_filter import BloomFilter
import string
from typing import List, Tuple
import random

def unique_words_generator(n: int, length: int) -> List:
    words = set()
    while len(words) < n:
        word = ''.join(random.choices(string.ascii_lowercase, k=length))
        words.add(word)
    return list(words)
