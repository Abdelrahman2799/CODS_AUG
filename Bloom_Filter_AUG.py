#import necessary packages
import math
import mmh3
from bitarray import bitarray
import typing

class BloomFilter:
    def __init__(self, exp_count: int, fp_rate: float):
        self.fp_rate = fp_rate
        self.size = self.compute_size(exp_count, self.fp_rate)
        self.array = bitarray(self.size)
        self.array.setall(0)
        self.hfunctions = self.compute_hash_count(self.size, exp_count)
        self.strings_count = 0

    def count_strings(self) -> int:
        return self.strings_count

    
    def compute_size(self, count, prob) -> int:
        size = - (count * math.log(prob)) / (math.log(2) ** 2)
        return int(size)

    def compute_hash_count(self, arraysize: int, exp_words: int) -> int:
        hash_count = (arraysize / exp_words) * math.log(2)
        return int(hash_count)
