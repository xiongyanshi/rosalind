#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def main():
    filename = sys.argv[1]
    with open(filename) as file:
        seq_dna = file.read().upper()
    seq_rna = seq_dna.replace('T', 'U')
    print seq_rna


if __name__ == '__main__':
    main()
