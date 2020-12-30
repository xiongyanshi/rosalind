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
    if m:
        loci = []
        for motif in m:
            for i in range(len(protein_seq)):
                if motif == protein_seq[i:i + len(motif)]:
                    loci.append(i + 1)
        return loci
    return None


def find_motif_overlap(pro_seq):
    '''return motif location(s) in pro_seq, even overlapping'''
    resultlist = []
    pos = 0
    p = re.compile(r'N[^P][ST][^P]')
    while True:
        result = p.search(pro_seq, pos)
        if result is None:
            break
        resultlist.append(result.start() + 1)
        pos = result.start() + 1
    return resultlist


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
        return str(SeqIO.read(seq_handle, 'uniprot-xml').seq)
    return None


def main():
    with open(sys.argv[1]) as file:
        ID_list = file.read().strip().split()
    for i in ID_list:
        i_find = find_motif_overlap(get_pro_from_SwissProt(i))
        if i_find:
            print '\n' + i
            for loci in i_find:
                print loci,

if __name__ == '__main__':
    main()
