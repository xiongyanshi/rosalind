#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def countACGT(string):
    '''return base A C G T numbers occrued in string'''
    seq = string.upper()
    return seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T')


def main():
    filename = sys.argv[1]
    with open(filename) as file:
        file_seq = file.read()
    print countACGT(file_seq)


if __name__ == '__main__':
    main()
