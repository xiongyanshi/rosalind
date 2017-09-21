#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO, ExPASy
import re


def find_motif(protein_seq):
    '''return the location of motif N{P}[ST]{P} in protein_seq '''
    p = re.compile(r'N[^P][ST][^P]')
    m = p.findall(protein_seq)
    loci = []
    for motif in m:
        loci.append(protein_seq.index(motif) + 1)
    return loci


def get_pro_from_uniport(id):
    '''return protein sequence of id in uniport database'''
    handle = ExPASy.get_sprot_raw(id)
    pro_record = SeqIO.read(handle, 'swiss')
    return str(pro_record.seq)


def main():
    with open(sys.argv[1]) as file:
        ID_list = file.read().strip().split()
    for i in ID_list:
        print i,
        # print '{} \t- \t{}'.format(i, get_pro_from_uniport(i))
        print find_motif(get_pro_from_uniport(i))


if __name__ == '__main__':
    main()
