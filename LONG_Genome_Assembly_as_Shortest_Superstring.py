#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO
# import re


def glue(seq1, seq2):
    """
    try to glue seq1 + seq2
    overlap length over at least half of shorter sequence
    """
    winlen = len(seq1) if len(seq1) < len(seq2) else len(seq2)
    # try seq1 + seq2 pattern
    for win in range(winlen, winlen/2, -1):
        overlapseq1 = seq2[:win]
        if seq1.endswith(overlapseq1):
            print 'overlap {}/{}'.format(len(overlapseq1), winlen)
            return seq1 + seq2[win:]
    return False


def head(seqlist):
    print 'searching head...'
    seqpool = tuple(seqlist)
    for startseq in seqpool:
        Hcount = 0
        Tcount = 0
        index = seqpool.index(startseq)
        seqlist.pop(index)
        for restseq in seqlist:
            if glue(restseq, startseq):
                Tcount += 1
            if glue(startseq, restseq):
                Hcount += 1
        print 'as head {} times, as tail {} times'.format(Hcount, Tcount)
        if Hcount == 1 and Tcount == 0:
            print 'done'
            return startseq
        seqlist.insert(index, startseq)
    print 'failed!'
    return None


def verify(superString, sequence_collection):
    """
    verify if every sequence in sequence_colllection
    is a substring of superString
    """
    if not isinstance(superString, str):
        return False
    for each in sequence_collection:
        if each not in superString:
            return False
    return True


def main():
    fasta_file = SeqIO.parse(sys.argv[1], 'fasta')

    sequence_list = []
    for entry in fasta_file:
        sequence_list.append(str(entry.seq))
    print '*' * 20
    print 'all: {} sequences'.format(len(sequence_list))
    sequence_length = map(len, sequence_list)
    print 'min length: {0}'.format(min(sequence_length))
    print 'max length: {0}'.format(max(sequence_length))
    print '*' * 20
    print head(sequence_list)

    '''
    sequence_list.reverse()
    result_sequence_1 = assembly(set(sequence_list))

    print '\nresult:\n{}\n'.format(result_sequence_1)
    print 'verify:', verify(result_sequence_1, sequence_list)
    if sys.argv[1] == 'data/rosalind.txt':
        print 'right answer:\nATTAGACCTGCCGGAATAC'
    '''


if __name__ == '__main__':
    main()
