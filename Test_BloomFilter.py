from Bloom_Filter_AUG import BloomFilter
import string
from typing import List, Tuple
import random
from scipy.stats import chi2_contingency
import numpy as np
import mmh3

def unique_words_generator(n: int, length: int) -> List:
    # """Generate a list of unique random strings."""
    words = set()
    while len(words) < n:
        word = ''.join(random.choices(string.ascii_lowercase, k=length))
        words.add(word)
    return list(words)

def test_insert(exp_count: int, fp_rate: float, words_length:int=10):
    # """Test that all inserted words are found in the Bloom filter."""

    # Generate unique words for insertion
    add_words = unique_words_generator(exp_count, words_length)

    # Insert words into the Bloom filter
    bf = BloomFilter(exp_count, fp_rate)
    for word in add_words:
        bf.insert(word)

    # Check that all inserted words are correctly identified by the Bloom filter
    for word in add_words:
        assert bf.search(word), f"'{word}' was not found even though it was inserted!"
    

def test_search(exp_count: int, fp_rate: float, words_length:int=10, size:int=10000) -> float:
#   """Test the Bloom filter and return the observed false positive rate."""
    # Generate words for insertion and testing
    add_words = unique_words_generator(exp_count, words_length)
    to_test = unique_words_generator(size, words_length)

    # Ensure no overlap between insert and test words
    to_test = [word for word in to_test if word not in add_words]

    # Initialize Bloom filter
    bloom = BloomFilter(exp_count, fp_rate)
      
    # Insert words into the Bloom filter
    for word in add_words:
        bloom.insert(word)
    # Check test words and count false positives
    fp_count = 0
    for word in to_test:
        if bloom.search(word):
            fp_count += 1
            
    # Calculate observed false positive rate
    observed_fp_rate = fp_count / len(to_test)
    print(f'Expected FPR: {fp_rate}, Observed FPR: {observed_fp_rate}')

    return observed_fp_rate

def test_natural_language_words(exp_count: int, fp_rate: float) -> None:
    #Test hash functions with natural language words
    words = ['apple', 'banana', 'tomato', 'orange', 'watermelon']
    bf = BloomFilter(exp_count, fp_rate)
    for word in words:
        bf.insert(word)
    for word in words:
        assert bf.search(word), f'"{word}" was not found even though it was inserted'
    
def test_dna_seq(exp_count:int, fp_rate:float, seq_length:int=10, num_seq:int=100) -> None:
    #Test hash functions using DNA sequences
    dna_sequences = generate_DNA_sequences(num_seq, seq_length)
    bloom = BloomFilter(exp_count, fp_rate)
    for seq in dna_sequences:
        bloom.insert(seq)
    for seq in dna_sequences:
        assert bloom.search(seq), f'"{seq}" was not found even though it was inserted'

def generate_DNA_sequences(count:int, length:int) -> list:
    #Generate unique random DNA sequences
    return [''.join(random.choices('ACGT', k=length)) for _ in range(count)]

# Examples for insertion test:
test_insert(exp_count=100, fp_rate=0.01, words_length=10)
test_insert(exp_count=1000, fp_rate=0.01, words_length=15)
test_insert(exp_count=10000, fp_rate=0.05, words_length=10)
test_insert(exp_count=10000, fp_rate=0.01, words_length=5)

# Examples for fpr test:
test_search(exp_count=100, fp_rate=0.01, words_length=10, size=100)
test_search(exp_count=1000, fp_rate=0.01, words_length=10, size=1000)
test_search(exp_count=1000, fp_rate=0.01, words_length=15, size=1000)
test_search(exp_count=1000, fp_rate=0.05, words_length=10, size=1000)
test_search(exp_count=10000, fp_rate=0.01, words_length=10, size=10000)
test_search(exp_count=10000, fp_rate=0.01, words_length=10, size=100000)

test_natural_language_words(10000, 0.01)
test_natural_language_words(1000, 0.05)
test_natural_language_words(100, 0.01)
test_dna_seq(10000, 0.01)
test_dna_seq(100, 0.01)
test_dna_seq(1000, 0.05)

def random_strings_generator(n: int, length: int) -> List:
  #"""Generate a list of unique random strings."""
    words = set()
    while len(words) < n:
        word = ''.join(random.choices(string.ascii_lowercase, k=length))
        words.add(word)
    return list(words)

def hash(words: List, size: int) -> List:
    # """Hash each string and return the hash values."""
    hash_values = []
    for word in words:
        hash_value = mmh3.hash(word) % size
        hash_values.append(hash_value)
    return hash_values

def test_uniformity(hash_values: List, size: int):
    # Chi-square test for uniformity
    observed_freq, _ = np.histogram(hash_values, bins=size, range=(0, size))
    expected_freq = [len(hash_values) / size] * size
    test_stat, p_value = chi2_contingency([observed_freq, expected_freq])[:2]

    print(f"Chi Squared test statistic: {test_stat}")
    print(f'P-value: {p_value}')
    
    if p_value < 0.05:
        print('The hash values do not follow an uniform distribution, so we reject the Null Hypothesis')
    else:
        print('The hash values follow an uniform distribution, so we fail to reject the Null Hypothesis')


# Examples
count = 100
length = 5
size = 10

random_strings = random_strings_generator(count, length)
hash_values = hash(random_strings, size)
test_uniformity(hash_values, size)


count = 1000
length = 10
size = 1000

random_strings = random_strings_generator(count, length)
hash_values = hash(random_strings, size)
test_uniformity(hash_values, size)


count = 100000
length = 10
size = 1000

random_strings = random_strings_generator(count, length)
hash_values = hash(random_strings, size)
test_uniformity(hash_values, size)






