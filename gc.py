#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def gc(dna_seq):
    '''return GC content of given dna sequence'''
    dna_seq = dna_seq.upper()
    gc = (dna_seq.count('G') + dna_seq.count('C'))*100.0 / len(dna_seq)
    return round(gc, 7)


def read_fasta(file_path):
    fasta_dict = {}
    with open(file_path) as file:
        file = file.read()
    for entry in file.split('>')[1:]:
        entry_name = entry.split()[0]
        entry_seq = ''.join(entry.split()[1:])
        fasta_dict[entry_name] = entry_seq
    return fasta_dict


def main():
    seq_dic = read_fasta(sys.argv[1])
    max_gc = 0

    for name, sequence in seq_dic.iteritems():
        seq_gc = gc(sequence)
        if seq_gc > max_gc:
            result_name = name
            max_gc = seq_gc
    print result_name, max_gc


if __name__ == '__main__':
    main()
