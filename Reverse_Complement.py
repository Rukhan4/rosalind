""" 
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol 
(e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

import sys

def reverse_complement(dna):
    #have to use common letters in replace because it will potentially replace a letter more than once as it goes down the bases
    return dna[::-1].replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper()

#print(reverse_complement("AAAACCCGGT"))

with open(sys.argv[1], mode='r') as inpfile:
    dna = str(inpfile.readline())

print(reverse_complement(dna))