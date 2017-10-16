#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO
# import re


def find_head(seq1, seq2):
    """
    return the head sequence in the whole chromosome
    """
    wid = len(seq1) if len(seq1) < len(seq2) else len(seq2)

    for loci in range(wid-1, wid/2, -1):
        overlap_seq1 = seq1[:loci]
        if seq2[-loci:] == overlap_seq1:
            return False
    return True
    

def glueTwoSeq(seq1, seq2):
    """
    connect two given overlap sequences into a new sequence
    return overlap length, glued sequence
    return '', '' if glue failed
    """
    if seq1 in seq2:
        return seq2
    elif seq2 in seq1:
        return seq1

    wid = len(seq1) if len(seq1) < len(seq2) else len(seq2)

    contig1 = ''
    for loci in range(wid-1, wid/2, -1):
        overlap_seq2 = seq2[:loci]
        if seq1[-loci:] == overlap_seq2:
            contig1 = seq1 + seq2[loci:]

    contig2 = ''
    for loci in range(wid-1, wid/2, -1):
        overlap_seq1 = seq1[:loci]
        if seq2[-loci:] == overlap_seq1:
            contig2 = seq2 + seq1[loci:]
    
    if len(contig1) > 0:
        if len(contig2) > 0:
            return contig1, contig2
        else:
            return contig1
    else:
        if len(contig2) > 0:
            return contig2
        else:
            return None


def assembly2(seqlist):
    """try to assembly sequences in seqlist"""
    for i in seqlist:
        seqlist.remove(i)
        for j in seqlist:
            if find_head(i, j):
                print 'find head: {}'.format(i)
        seqlist += [i]
    return 'finish!'


def assembly(seqlist):
    """
    Assembly seq with sequence in seqList into a shortest one
    """
    seqlist = list(seqlist)
    while len(seqlist) > 1:
        start_seq = seqlist[0]
        remain_seqs = seqlist[1:]
        overlap_len_list = []
        contigs = []

        for each in remain_seqs:
            glue_result = glueTwoSeq(start_seq, each)
            overlap_len_list.append(glue_result[0])
            contigs.append(glue_result[1])

        print 'over:', overlap_len_list
        print 'cont:', contigs

        max_overlaplen = max(overlap_len_list)
        if max_overlaplen == 0:
            print 'connection failed !'
            return None
        else:
            best_index = overlap_len_list.index(max_overlaplen)
            best_contig = contigs[best_index]
            best_follow = remain_seqs[best_index]
            seqlist.remove(start_seq)
            seqlist.remove(best_follow)
            seqlist.append(best_contig)
            print 'remain:{}'.format(len(seqlist))
    return seqlist[0]


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
    print '-\n{} seqs {} bases\n-'.format(len(sequence_list),
                                          len(sequence_list[0]))
    print '*' * 20
    '''
    sequence_list.reverse()
    result_sequence_1 = assembly(set(sequence_list))

    print '\nresult:\n{}\n'.format(result_sequence_1)
    print 'verify:', verify(result_sequence_1, sequence_list)
    if sys.argv[1] == 'data/rosalind.txt':
        print 'right answer:\nATTAGACCTGCCGGAATAC'
    '''
    print assembly2(sequence_list)


if __name__ == '__main__':
    main()
