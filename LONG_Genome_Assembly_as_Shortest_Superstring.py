#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO


def glueTwoSeq(seq1, seq2):
    """
    connect two given overlap sequences into a new sequence
    return False if glue failed
    """
    # print '\nconnecting {} AND {}'.format(seq1, seq2)

    print '\nforward connecting:',
    print seq1[:5], '...', seq1[-5:], '--', seq2[:5], '...', seq2[-5:]
    for loci in range(len(seq2)/2, len(seq2)):
        overlap_seq2 = seq2[:loci]
        if seq1[-loci:] == overlap_seq2:
            print 'find overlap:\n{}\nlength:{}'.format(overlap_seq2,
                                                        len(overlap_seq2))
            return seq1 + seq2[loci:]
    print 'forward connect failed'

    print 'reverse connecting:',
    print seq2[:5], '...', seq2[-5:], '--', seq1[:5], '...', seq1[-5:]
    for loci in range(len(seq1)/2, len(seq1)):
        overlap_seq1 = seq1[:loci]
        if seq2[-loci:] == overlap_seq1:
            print 'find overlap:\n{}\nlength:{}'.format(overlap_seq1,
                                                        len(overlap_seq1))
            return seq2 + seq1[loci:]
    print 'reverse connect failed'

    print 'cannot connect this two seqs'
    return False


def assembly_sequences(seqs):
    """
    Assembly all sequences in seqs into a complete one
    """
    while len(seqs) != 1:
        start_seq = seqs[0]
        seqs = seqs[1:]
        for each in seqs:
            glue_seq = glueTwoSeq(start_seq, each)
            if glue_seq:
                seqs.append(glue_seq)
                seqs.remove(each)
                print 'assemblized:\n{}'.format(glue_seq)
                # print seqs
                break
    return seqs[0]


def main():
    fasta_file = SeqIO.parse(sys.argv[1], 'fasta')

    sequence_list = []
    for entry in fasta_file:
        sequence_list.append(str(entry.seq))

    print '\nsequences ...\n-'
    for seq in sequence_list:
        print seq[:20]

    print '-\n{} seqs {} bases\n-'.format(len(sequence_list),
                                          len(sequence_list[0]))

    result_sequence_1 = assembly_sequences(sequence_list)

    sequence_list.reverse()
    result_sequence_2 = assembly_sequences(sequence_list)

    print '\nresult1: \n{}\nlength:{}'.format(result_sequence_1,
                                              len(result_sequence_1))
    print '\nresult2: \n{}\nlength:{}'.format(result_sequence_2,
                                              len(result_sequence_2))

    print 'ATTAGACCTGCCGGAATAC'


if __name__ == '__main__':
    main()
