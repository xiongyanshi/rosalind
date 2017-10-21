#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO
import re


def findindex(seq1, seq2):
    """
    return the index of seq2 in seq1 as a subsequence
    """
    index_base = 0
    for i in seq2:
        # print 'searching {} in {}'.format(i, seq1[index_base:])
        index_i = re.search(i, seq1[index_base:]).start()
        # print 'find index is {}'.format(index_i + index_base + 1)
        print index_i + index_base + 1,
        index_base += index_i + 1


def main():
    fastafile = SeqIO.parse(sys.argv[1], 'fasta')
    seqs = [str(entry.seq) for entry in fastafile]
    superseq = seqs[0]
    subseq = seqs[1]
    findindex(superseq, subseq)


if __name__ == '__main__':
    main()
