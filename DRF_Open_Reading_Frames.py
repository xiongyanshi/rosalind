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
    protein = re.match(r'(?=(M[^*]*\*))', protein_sequence)
    return protein


def find_protein_seq(dna_seq):
    """
    find candidate reading frames for given dna_seq
    return as protein sequence(s)
    """
    pro_seq = dna_seq.translate()
    if 'M' not in pro_seq:
        return [None]
    elif pro_seq.count('M') == 1:
        start_position = str(pro_seq).index('M')
        end_position = str(pro_seq).index('*')
        return [pro_seq[start_position:end_position]]
    else:
        candidate_pro_list = []
        protein_cut = pro_seq.split('*')
        for protein in protein_cut:
            while 'M' in protein:
                start_index = str(protein).index('M')
                candidate_pro_list.append(protein[start_index:])
                protein = protein[start_index + 1:]
        return candidate_pro_list


def main():
    fasta_file = SeqIO.read(sys.argv[1], 'fasta')
    print fasta_file, '\n'

    result_protein_sequence = []
    six_candidate = six_transcribe_DNA_seq(fasta_file)
    for each in six_candidate:
        print each.seq.translate(), '\n'
        dna_sequence = make_seq_length_3x(each.seq)
        result_protein_sequence += find_protein_seq(dna_sequence)

    for pro in result_protein_sequence:
        if pro:
            pass
            # print str(pro)


if __name__ == '__main__':
    main()
