#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
# from Bio.Seq import Seq
from Bio import SeqIO
import re


def six_transcribe_DNA_seq(dna_sequence):
    """
    return all six possible transcribe dna sequences,
    3 by forward, 3 by reverse complement sequences
    """
    dna_seq = dna_sequence.upper()
    reverse_complement_seq = dna_seq.reverse_complement()
    result = []
    for i in range(3):
        result.append(dna_seq[i:])
        result.append(reverse_complement_seq[i:])
    return result


def make_seq_length_3x(sequence):
    """making the length of sequence to be multiples of 3, for translate
    """
    return sequence[:(len(sequence)/3)*3]


def find_motif(protein_sequence):
    """return the protein sequence in given protein_sequence,
    input:  'SHVANSGYMGMTPRLGLESLLE*A*MIRVASQ'
    output: ['MGMTPRLGLESLLE*', 'MTPRLGLESLLE*']
    """
    protein = re.findall(r'(?=(M[^*]*\*))', protein_sequence)
    return protein


def find_motif_from_dna(dna_seq):
    pro_seq = dna_seq.translate()
    motifs = find_motif(str(pro_seq))
    return motifs


def main():
    fasta_file = SeqIO.read(sys.argv[1], 'fasta')
    # print fasta_file, '\n'

    result_protein_sequence = []
    six_candidate_dna = six_transcribe_DNA_seq(fasta_file)
    for each_dna_candidate in six_candidate_dna:
        each = make_seq_length_3x(each_dna_candidate)
        # print each.seq.translate(), '\n'
        result_protein_sequence += find_motif_from_dna(each.seq)

    for i in set(result_protein_sequence):
        print i[:-1]


if __name__ == '__main__':
    main()
