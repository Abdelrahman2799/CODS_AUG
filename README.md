Bloom Filter is a space-efficient-probabilistic data structure. It is used to test whether an element is a member of a set or not. It makes use of bit arrays and hash functions for insertion and search of elements. Bloom Filter usually comes with a trade-off between efficiency and accuracy. This means that there is a probability of false positives. For example, if the Bloof Filter says that it has inserted a given string, this means that it might or might not br inserted. However, there is no place for false negatives in a bloom filter. So, if the bloom says that a given element does not exist, we are 100% sure it doesn't exist. The lower the false positive rate a user tolerates, the larger the array used for insertion, hence more storage needed, and more hash functions also. Inserting 10,000 word requires larger array than inserting 500 words, so the aim is to find the balance between efficiency and accuracy.

This repository includes: 1- Bloom_Filter_AUG.py: A module that contains the BloomFilter class with insert, search count strings, compute array size and compute number of hash functions methods. This file is the file which contains the implementation of the bloom filter algorithm.

2- Test_BloomFilter.py: A test file to test the correctness of the code, the distribution of the hash functions, and whether the actual false positive rate exceeds what is expected or not, and the accuracy of the hash functions given different data types.

3- Benchmark_AUG.py: A performance test for the bloom filter methods with large sample sizes. Using visualization, we assess the insertion and search times as a function of increasing words counts, as well as assesing changes in the compression rate and false positive rates as a function of increasing words counts. This script is furhter used in the HPC infrastructure to test and do experiments.

4- Benchmark_AUG_error.txt and Benchmark_AUG_output.txt: Outputs from the HPC infrastructure after doing the experiment.

5- Benchmark_AUG.png: The visual output of the experiment done by the HPC.

6- Discussion of the results.docx: Discussion for the results of the experiment.

Conclusions:

- On average, as the number of inserted words increases, the time needed for insertion increases.
- On average, as the number of inserted words increases, the time needed for searching increases.
- As the number of elements approaches the capacity of the Bloom filter, the false positive rate increases more exponentially.
- The compression rate decreases with increasing word counts untill a certain size is reached where it nearly stabilizes at 0.
