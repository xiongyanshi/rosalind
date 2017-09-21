#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO, ExPASy
import uniprot as uni
import StringIO
import re


def find_motif(protein_seq):
    '''return the location of motif N{P}[ST]{P} in protein_seq '''
    p = re.compile(r'N[^P][ST][^P]')
    m = p.findall(protein_seq)
    loci = []
    for motif in m:
        loci.append(protein_seq.index(motif) + 1)
    return loci


def get_pro_from_SwissProt(id):
    '''return protein sequence of id from swiss protein database
    module used: Bio.ExPASy, SeqIO.read'''
    handle = ExPASy.get_sprot_raw(id)
    if handle:
        pro_record = SeqIO.read(handle, 'swiss')
        return str(pro_record.seq)
    return None


def get_pro_from_uniprot(id):
    '''return protein sequence by uniprot retrieve method
    module used:uniprot.retrieve, SeqIo.read'''
    seq = uni.retrieve(id, 'xml')
    if seq:
        seq_handle = StringIO.StringIO(seq)
        return SeqIO.read(seq_handle, 'uniprot-xml').seq
    return None


def main():
    with open(sys.argv[1]) as file:
        ID_list = file.read().strip().split()
    for i in ID_list:
        print i
        print 'swiss:\t', get_pro_from_SwissProt(i)
        print 'unipr:\t', get_pro_from_uniprot(i)
        print '\n'
        # print '{} \t- \t{}'.format(i, get_pro_from_uniport(i))


if __name__ == '__main__':
    main()
