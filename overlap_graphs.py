#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO


def fasta_to_dict(filepath):
    dict = {}
    for entry in SeqIO.parse(filepath, 'fasta'):
        dict[entry.name] = str(entry.seq)
    return dict


def main():
    fasta_dict = fasta_to_dict(sys.argv[1])
    for i in fasta_dict:
        for j in fasta_dict:
            if fasta_dict[i][-3:] == fasta_dict[j][:3] and i != j:
                print i, j


if __name__ == '__main__':
    main()
