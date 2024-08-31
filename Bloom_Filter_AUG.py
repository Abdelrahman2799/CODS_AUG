#import necessary packages
import math
import mmh3
from bitarray import bitarray
import typing

class BloomFilter:
    def __init__(self, exp_count: int, fp_rate: float):
        self.fp_rate = fp_rate
        self.size = self.compute_size(exp_count, self.fp_rate)
      
    def compute_size(self, count, prob) -> int:
        size = - (count * math.log(prob)) / (math.log(2) ** 2)
        return int(size)


