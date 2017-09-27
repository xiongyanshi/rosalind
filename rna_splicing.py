#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO
from Bio.Seq import Seq
import re


def requence_and_intro_read(file_path):
    fasta = SeqIO.parse(file_path, 'fasta')
    seq_list = []
    for entry in fasta:
        seq_list.append(str(entry.seq))
    dna_seq = seq_list[0]
    intro_seqs = seq_list[1:]
    return dna_seq, intro_seqs


def main():
    dna_sequence, intro_seq_list = requence_and_intro_read(sys.argv[1])
    # mrna = ''
    for intro in intro_seq_list:
        intro_start = dna_sequence.index(intro)
        intro_stop = intro_start + len(intro)
        # print intro_start, intro_stop
        mrna = dna_sequence[:intro_start]
        mrna += dna_sequence[intro_stop:]
        dna_sequence = mrna
        # print mrna, len(mrna)
    print Seq(mrna).translate()[:-1]


if __name__ == '__main__':
    main()
