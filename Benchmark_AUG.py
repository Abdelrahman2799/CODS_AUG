from Bloom_Filter_AUG import BloomFilter
import random
import string
import time
import matplotlib.pyplot as plt
import numpy as np


def unique_words_generator(n, length):
    words = set()
    while len(words) < n:
        word = ''.join(random.choices(string.ascii_lowercase, k=length))
        words.add(word)
    return list(words)

