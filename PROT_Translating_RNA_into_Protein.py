#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def translate_rna(string):
    with open('./data/RNA_amnio.txt') as file:
        file = file.read().upper().strip()
    translate_dict = {}
    for line in file.split('\n'):
        rna = line.split()[0]
        amnio = line.split()[1]
        translate_dict[rna] = amnio
    return translate_dict[string.upper()]


def main():
    with open(sys.argv[1]) as file:
        rna_seq = file.read().upper().strip()
    amnio_seq = ''
    i = 0
    while rna_seq[i:i + 3]:
        amnio_seq += translate_rna(rna_seq[i:i + 3])
        i += 3
    print amnio_seq


if __name__ == '__main__':
    main()
