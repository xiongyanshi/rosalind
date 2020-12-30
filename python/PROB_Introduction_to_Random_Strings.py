#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import math


def prob_gcat(GCcontent):
    """
    return the probablity of G C A T with given GC content as a dictionary
    """
    GCcontent = float(GCcontent)
    return {'G': GCcontent/2.0,
            'C': GCcontent/2.0,
            'A': (1 - GCcontent)/2.0,
            'T': (1 - GCcontent)/2.0}


def prob_string(dna_sequence, prob_distribution_of_gcat):
    dna_sequence = dna_sequence.upper()
    probablity = 1.0
    for base in dna_sequence:
        probablity *= prob_distribution_of_gcat[base]
    return math.log10(probablity)


def main():
    with open(sys.argv[1]) as handle:
        file = handle.read().strip().split()
    dnastring = file[0]
    gc_list = file[1:]
    print 'result:'
    for gc in gc_list:
        print round(prob_string(dnastring, prob_gcat(gc)), 3),


if __name__ == '__main__':
    main()
