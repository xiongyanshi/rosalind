#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO


def complement_dna(base):
    if base == 'A' or base == 'a':
        return 'T'
    if base == 'T' or base == 't':
        return 'A'
    if base == 'G' or base == 'g':
        return 'C'
    if base == 'C' or base == 'c':
        return 'G'


def reverse_palindrome(sequence):
    i = 0
    for i in range(len(sequence)//2):
        if sequence[i] != complement_dna(sequence[-1-i]):
            return False
    return True


def main():
    fasta = SeqIO.read(sys.argv[1], 'fasta')
    seq = str(fasta.seq)

    for start_pos in range(0, len(seq)-4):
        for length in range(4, min(12, len(seq) - start_pos) + 1, 2):
            test_seq = seq[start_pos:start_pos+length]
            if reverse_palindrome(test_seq):
                print start_pos + 1, len(test_seq), test_seq


if __name__ == '__main__':
    main()
