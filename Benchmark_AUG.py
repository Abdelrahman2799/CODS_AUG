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

words_to_insert = unique_words_generator(10 * exp_count, word_length)
fpr_test_words = unique_words_generator(fpr_test_size, word_length)


sizes = [10000, 20000, 50000, 100000, 200000, 500000, 1000000]

insertion_time = []
search_time = []
compression_rates = []
fps_counts = []
observed_fprs = []

for size in sizes:
    insert_durations = []
    search_durations = []
    compression_list = []

    for rep in range(repetition):
        bloom = BloomFilter(exp_count, fp_rate)
        sample = words_to_insert[:size]

        start_time = time.time()
        for word in sample:
            bloom.insert(word)
        insert_duration = time.time() - start_time
        insert_durations.append(insert_duration)

        start_time = time.time()
        for word in sample:
            bloom.search(word)
        search_duration = time.time() - start_time
        search_durations.append(search_duration)

        compression_rate = m / size
        compression_list.append(compression_rate)

    
    insertion_time.append(np.mean(insert_durations))
    search_time.append(np.mean(search_durations))
    compression_rates.append(np.mean(compression_list))


for i in range(0, len(words_to_insert), steps):
    bloom = BloomFilter(exp_count, fp_rate)
    sample = words_to_insert[:i + steps]

    for word in sample:
        bloom.insert(word)

    false_positives = sum(1 for word in fpr_test_words if bloom.search(word))
    observed_fpr = false_positives / len(fpr_test_words)

    fps_counts.append(i + steps)
    observed_fprs.append(observed_fpr)



