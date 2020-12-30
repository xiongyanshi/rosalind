#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO
from Bio import Seq


def judge(seq_list):
    """return the error sequences and right sequences"""
    error = []
    right = []
    for i in seq_list:
        revcomp = str(Seq.Seq(i).reverse_complement())
        if seq_list.count(i) + seq_list.count(revcomp) >= 2:
            right.append(i)
        else:
            error.append(i)
    return error, right


def himm(seq1, seq2):
    """return the himming distence between two sequences"""
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count


def find_substitution(seqlist1, seqlist2):
    """
    find the substitution site
    seqlist1: error sequence list
    seqlist2: right sequence list(maybe with reverse complement)
    """
    result = set()
    for error_seq in seqlist1:
        for right_seq in seqlist2:
            revcomp_right = str(Seq.Seq(right_seq).reverse_complement())
            if himm(error_seq, right_seq) == 1:
                result.add('{}->{}'.format(error_seq, right_seq))
                break
            elif himm(error_seq, revcomp_right) == 1:
                result.add('{}->{}'.format(error_seq, revcomp_right))
    return list(result)


def main():
    fasta = SeqIO.parse(sys.argv[1], 'fasta')
    inseqs = []
    for entry in fasta:
        inseqs.append(str(entry.seq))
    print 'all seqs NO. : {}'.format(len(inseqs))
    error_seqs, right_seqs = judge(inseqs)
    print '{} error\n{} right\n'.format(len(error_seqs), len(right_seqs))
    for i in find_substitution(error_seqs, right_seqs):
        print i


if __name__ == '__main__':
    main()
