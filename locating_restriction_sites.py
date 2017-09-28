#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO
from Bio.Seq import Seq


def reverse_palindrome_v2(sequence):
    '''return true if 'sequence' is a reverse palindrome sequence'''
    seq = Seq(sequence)
    return str(seq) == str(seq.reverse_complement())


def main():
    fasta = SeqIO.read(sys.argv[1], 'fasta')
    seq = str(fasta.seq)

    for start_pos in range(0, len(seq)-3):
        for length in range(4, 13):
            test_seq = seq[start_pos:start_pos+length]
            if reverse_palindrome_v2(test_seq) and len(test_seq) == length:
                print start_pos + 1, len(test_seq), test_seq


if __name__ == '__main__':
    main()
