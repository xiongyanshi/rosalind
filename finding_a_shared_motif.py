#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO


def fasta_to_dict(filepath):
    '''parse fasta file in filepath into a dictionary'''
    dict = {}
    fasta = SeqIO.parse(filepath, 'fasta')
    for entry in fasta:
        dict[str(entry.name)] = str(entry.seq)
    return dict


def motif_in_all(motif, all_seq_list):
    '''return true if motif sequence in each sequences in all_seq_list'''
    for i in all_seq_list:
        if motif not in i:
            return False
    return True


def substring(seq):
    '''return all subsrings of seq into a list,
    from longest(len(seq) - 1) to shoortest, 2'''
    pass


def main():
    fasta_dict = fasta_to_dict(sys.argv[1])
    seq_list = []
    for i in fasta_dict.values():
        seq_list.append(i)
    print seq_list


if __name__ == '__main__':
    main()
