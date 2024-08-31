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

def test_insert(exp_count: int, fp_rate: float, words_length:int=10):
    add_words = unique_words_generator(exp_count, words_length)
    bf = BloomFilter(exp_count, fp_rate)
    for word in add_words:
        bf.insert(word)

    for word in add_words:
        assert bf.search(word), f"'{word}' was not found even though it was inserted!"
    

def test_search(exp_count: int, fp_rate: float, words_length:int=10, size:int=10000) -> float:
    add_words = unique_words_generator(exp_count, words_length)
    to_test = unique_words_generator(size, words_length)

    to_test = [word for word in to_test if word not in add_words]
    bloom = BloomFilter(exp_count, fp_rate)
    for word in add_words:
        bloom.insert(word)
    fp_count = 0
    for word in to_test:
        if bloom.search(word):
            fp_count += 1
    
    observed_fp_rate = fp_count / len(to_test)
    print(f'Expected FPR: {fp_rate}, Observed FPR: {observed_fp_rate}')

    return observed_fp_rate

test_insert(exp_count=100, fp_rate=0.01, words_length=10)
test_insert(exp_count=1000, fp_rate=0.01, words_length=15)
test_insert(exp_count=10000, fp_rate=0.05, words_length=10)
test_insert(exp_count=10000, fp_rate=0.01, words_length=5)

test_search(exp_count=100, fp_rate=0.01, words_length=10, size=100)
test_search(exp_count=1000, fp_rate=0.01, words_length=10, size=1000)
test_search(exp_count=1000, fp_rate=0.01, words_length=15, size=1000)
test_search(exp_count=1000, fp_rate=0.05, words_length=10, size=1000)
test_search(exp_count=10000, fp_rate=0.01, words_length=10, size=10000)
test_search(exp_count=10000, fp_rate=0.01, words_length=10, size=100000)

def random_strings_generator(n: int, length: int) -> List:
    words = set()
    while len(words) < n:
        word = ''.join(random.choices(string.ascii_lowercase, k=length))
        words.add(word)
    return list(words)





