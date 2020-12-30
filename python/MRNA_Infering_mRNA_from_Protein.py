#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def amnio_dict():
    """read source data ./data/amnio_RNA.txt, into a dictionary,
    Key:   amnio acid short name, like 'M'
    Value: list of all possible RNA codon code, like ['AUG']
    """
    with open('./data/amnio_RNA.txt') as file:
        file = file.readlines()
    amnio_di = {}
    for line in file:
        line = line.split()
        amnio_di[line[0]] = line[2:]
    return amnio_di


def cal_mrna_trans(prot_seq):
    """return all the possible mRNA translation chain,
    such as 'MA',
    'M':['AUG'],
    'A':['GCU', 'GCC', 'GCA', 'GCG']
    STOP:['UAA', 'UGA', 'UAG']
    return: 1*4*3 = 12
    """
    amnio_trans = amnio_dict()
    cal = 1
    for i in prot_seq.upper():
        cal *= len(amnio_trans[i])
    cal *= len(amnio_trans['STOP'])
    return cal


def main():
    """here mod by force, could be more elegent"""
    with open(sys.argv[1]) as file:
        file = file.read().strip()
    print cal_mrna_trans(file) % 1000000


if __name__ == '__main__':
    main()
