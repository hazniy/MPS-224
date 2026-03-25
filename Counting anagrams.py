from itertools import permutations
import unittest
from math import factorial

def list_anagrams(word):
    """
    Returns a list of (real or fake) anagrams of word.
    """
    word = word.lower()
    anagrams = [str.join('', w) for w in permutations(word)]
    anagrams = sorted(list(set(anagrams)))
    return anagrams

def count_anagrams(word):
    """
    Returns the number of anagrams of word.

    This function counts all anagrams; the anagrams do not have to be real words.
    """
    letter_counts = {}
    for c in word:
        if c in letter_counts:
            letter_counts[c] += 1
        else:
            letter_counts[c] = 1
    m = factorial(len(word))
    for key in letter_counts:
        m = m // factorial(letter_counts[key])
    return m

# This cell might take 10 seconds to run.
L = []
n = 0
%timeit -n1 L = list_anagrams('beeblebrox')
%timeit -n1 n = count_anagrams('beeblebrox')
print(f"n={n}, len(L)={len(L)}")
