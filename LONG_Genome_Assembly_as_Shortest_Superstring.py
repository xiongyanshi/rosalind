#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO
import re


def glueTwoSeq(seq1, seq2):
    """
    connect two given overlap sequences into a new sequence
    return False if glue failed
    """
    # print '\nconnecting {} AND {}'.format(seq1, seq2)
    if seq1 in seq2:
        print '-contain!'
        return seq2
    elif seq2 in seq1:
        print '-contain!'
        return seq1

    wid = len(seq1) if len(seq1) < len(seq2) else len(seq2)
    print '\nForward gluing...',
    # print seq1[:5], '...', seq1[-5:], '--', seq2[:5], '...', seq2[-5:],
    for loci in range(wid/2, wid+1):
        overlap_seq2 = seq2[:loci]
        if seq1[-loci:] == overlap_seq2:
            print '\nFind {}bases overlap'.format(len(overlap_seq2))
            return seq1 + seq2[loci:]

    print 'Reverse gluing...',
    # print seq2[:5], '...', seq2[-5:], '--', seq1[:5], '...', seq1[-5:],
    for loci in range(wid/2, wid+1):
        overlap_seq1 = seq1[:loci]
        if seq2[-loci:] == overlap_seq1:
            print '\nFind {}bases overlap'.format(len(overlap_seq1))
            return seq2 + seq1[loci:]

    return False


def glueSeqs(seq1, seq2):
    """Glue two sequences into one, return False if failed"""
    pass


def assembly_sequences(seqs):
    """
    Assembly all sequences in seqs into a complete one
    """
    while len(seqs) != 1:
        for each in seqs[1:]:
            contig = glueTwoSeq(seqs[0], each)
            if contig:
                seqs.append(contig)
                seqs.remove(seqs[0])
                seqs.remove(each)
                print 'assemblized:\n{}'.format(contig)
                print '{} sequences remained'.format(len(seqs))
                break
            else:
                pass
    return seqs[0]


def verify(superString, sequence_collection):
    """
    verify if every sequence in sequence_colllection
    is a substring of superString
    """
    for each in sequence_collection:
        if each not in superString:
            return False
    return True


def main():
    fasta_file = SeqIO.parse(sys.argv[1], 'fasta')

    sequence_list = []
    for entry in fasta_file:
        sequence_list.append(str(entry.seq))

    print '\nsequences ...\n-'
    for seq in sequence_list:
        print seq[:20]

    print '-\n{} seqs {} bases\n-'.format(len(sequence_list),
                                          len(sequence_list[0]))

    result_sequence_1 = assembly_sequences(sequence_list)

    sequence_list.reverse()
    # result_sequence_2 = assembly_sequences(sequence_list)

    print '\nresult1: \n{}\nlength:{}'.format(result_sequence_1,
                                              len(result_sequence_1))
    print verify(result_sequence_1, sequence_list)
    # print '\nresult2: \n{}\nlength:{}'.format(result_sequence_2,
    #                                           len(result_sequence_2))
    # print verify(result_sequence_2, sequence_list)

    print 'ATTAGACCTGCCGGAATAC'


if __name__ == '__main__':
    main()
