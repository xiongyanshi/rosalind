#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO


def product(n):
    i = 1
    for j in xrange(1, n + 1):
        i *= j
    return i


def main():
    sequence = SeqIO.read(sys.argv[1], 'fasta')
    seq = str(sequence.seq)
    at_pair = seq.count('A')
    cg_pair = seq.count('C')
    print product(at_pair) * product(cg_pair)


if __name__ == '__main__':
    main()
