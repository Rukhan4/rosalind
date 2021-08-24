"""
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""
import sys

    
def count_nuc(dna):
    BaseList = []
    for base in 'ACGT':
        BaseList.append(dna.count(base))
    return BaseList
    

with open(sys.argv[1], mode = 'r') as inpfile:
    dna = str(inpfile.readline())

print(*count_nuc(dna))

# IN BASH: py Counting_DNA_Nucleotides.py inputs/counting_dna_nucleotides.txt > countout.txt