#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def complement_base(base):
    '''return complement base of given base'''
    base = base.upper()
    if base == 'A':
        return 'T'
    elif base == 'T':
        return 'A'
    elif base == 'G':
        return 'C'
    elif base == 'C':
        return 'G'
    else:
        return '-'


def main():
    filename = sys.argv[1]

    with open(filename) as file:
        seq_origin = file.read().upper().strip()
    seq_complement = ''

    for base in seq_origin:
        seq_complement = seq_complement + complement_base(base)

    print seq_complement[::-1]


if __name__ == '__main__':
    main()
