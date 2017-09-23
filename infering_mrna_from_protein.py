#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def amnio_dict():
    with open('./data/amnio_RNA.txt') as file:
        file = file.readlines()
    amnio_di = {}
    for line in file:
        line = line.split()
        amnio_di[line[0]] = line[2:]
    return amnio_di


def cal_mrna_trans(prot_seq):
    amnio_trans = amnio_dict()
    cal = 1
    for i in prot_seq.upper():
        cal *= len(amnio_trans[i])
    cal *= len(amnio_trans['STOP'])
    return cal


def main():
    with open(sys.argv[1]) as file:
        file = file.read().strip()
    print cal_mrna_trans(file)

if __name__ == '__main__':
    main()
