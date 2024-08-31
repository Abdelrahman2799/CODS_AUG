from Bloom_Filter_AUG import BloomFilter
import random
import string
import time
import matplotlib.pyplot as plt
import numpy as np

# Function to generate unique words
def unique_words_generator(n, length):
#"""Generate a list of unique random strings."""
    words = set()
    while len(words) < n:
        word = ''.join(random.choices(string.ascii_lowercase, k=length))
        words.add(word)
    return list(words)

# Set parameters for the Bloom filter
exp_count = 100000  # Smaller expected number to achieve saturation
fp_rate = 0.01  # Desired false positive rate
word_length = 10 
fpr_test_size = 10000 # Number of words to test FPR
repetition = 10 # Number of repetitions for averaging
steps = 10000 # Number of elements to add at each step for FPR testing

## Initialize Bloom filter
bf = BloomFilter(exp_count, fp_rate) 

# Calculate the array size (m) and the number of hash functions (k)
m = bf.compute_size(exp_count, fp_rate)
k = bf.compute_hash_count(m, exp_count)

## Generate the words to insert and test
words_to_insert = unique_words_generator(10 * exp_count, word_length)
fpr_test_words = unique_words_generator(fpr_test_size, word_length)

## Lists to store the results
sizes = [10000, 20000, 50000, 100000, 200000, 500000, 1000000]

insertion_time = []
search_time = []
compression_rates = []
fps_counts = []
observed_fprs = []

# Benchmarking loop for insertion, search, and compression
for size in sizes:
    insert_durations = []
    search_durations = []
    compression_list = []

    for rep in range(repetition):
        bloom = BloomFilter(exp_count, fp_rate)
        sample = words_to_insert[:size]

        # Benchmark insertion time
        start_time = time.time()
        for word in sample:
            bloom.insert(word)
        insert_duration = time.time() - start_time
        insert_durations.append(insert_duration)

        # Benchmark search time
        start_time = time.time()
        for word in sample:
            bloom.search(word)
        search_duration = time.time() - start_time
        search_durations.append(search_duration)

        # Calculate compression rate
        compression_rate = m / size
        compression_list.append(compression_rate)

    # Average the results
    insertion_time.append(np.mean(insert_durations))
    search_time.append(np.mean(search_durations))
    compression_rates.append(np.mean(compression_list))

# Separate loop to continue inserting more elements to observe FPR accurately
for i in range(0, len(words_to_insert), steps):
    bloom = BloomFilter(exp_count, fp_rate)
    sample = words_to_insert[:i + steps]
    
    # Insert words into the Bloom filter
    for word in sample:
        bloom.insert(word)

    # Measure the FPR
    false_positives = sum(1 for word in fpr_test_words if bloom.search(word))
    observed_fpr = false_positives / len(fpr_test_words)

    # Store the results
    fps_counts.append(i + steps)
    observed_fprs.append(observed_fpr)


# Plotting the results
plt.figure(figsize=(18, 12))

#Insertion

plt.subplot(2, 2, 1)
plt.plot(sizes, insertion_time, marker='o')
plt.title('Input Size vs Insertion Time')
plt.xlabel('Number Of Elements')
plt.ylabel('Insertion time (seconds)')


#Search
plt.subplot(2, 2, 2)
plt.plot(sizes, search_time, marker='o')
plt.title('Input Size vs Search Time')
plt.xlabel('Number Of Elements')
plt.ylabel('Search time (seconds)')


#fpr
plt.subplot(2, 2, 3)
plt.plot(fps_counts, observed_fprs, marker='o')
plt.axhline(y=fp_rate, color='r', linestyle='--', label='Expected FPR = 0.01')
plt.title('Observed False Positive Rate')
plt.xlabel('Number Of Elements')
plt.ylabel('False Positive Rate')
plt.legend()

#compression
plt.subplot(2, 2, 4)
plt.plot(sizes, compression_rates, marker='o')
plt.title('Input Size vs Compression Rate')
plt.xlabel('Number Of Elements')
plt.ylabel('Compression Rate')
plt.ylim(0, 80)

plt.tight_layout()
plt.show()


