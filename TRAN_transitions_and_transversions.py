#!/usr/bin/python
# _*_ coding: utf-8 _*_


import sys
from Bio import SeqIO


def transition(base1, base2):
    """return True if two bases is transition relationship"""
    base1 = base1.upper()
    base2 = base2.upper()
    if set([base1, base2]) in [set(['A', 'G']), set(['C', 'T'])]:
        return True
    return False


def transversion(base1, base2):
    """return True if two bases is transversion relationship"""
    base1 = base1.upper()
    base2 = base2.upper()
    if set([base1, base2]) in [set(['A', 'C']),
                               set(['G', 'T']),
                               set(['A', 'T']),
                               set(['C', 'G'])]:
        return True
    return False


def ratio(seq1, seq2):
    transi = 0.0
    transv = 0.0
    for i in xrange(len(seq1)):
        if transition(seq1[i], seq2[i]):
            transi += 1
        if transversion(seq1[i], seq2[i]):
            transv += 1
    print 'transition: {}\ntransversion: {}'.format(transi, transv)
    return round(transi / transv, 11)


def main():
    fastafile = SeqIO.parse(sys.argv[1], 'fasta')
    [seq1, seq2] = [str(entry.seq) for entry in fastafile]
    # print seq1
    # print seq2
    print ratio(seq1, seq2)


if __name__ == '__main__':
    main()
