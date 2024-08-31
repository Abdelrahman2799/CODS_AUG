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

exp_count = 100000
fp_rate = 0.01
word_length = 10
fpr_test_size = 10000
repetition = 10
steps = 10000 

bf = BloomFilter(exp_count, fp_rate)

m = bf.compute_size(exp_count, fp_rate)
k = bf.compute_hash_count(m, exp_count)



