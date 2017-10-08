#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def main():
    with open(sys.argv[1]) as file:
        file = file.read().strip().split()
    seq_1 = file[0]
    seq_2 = file[1]
    mutations = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            mutations += 1
    print mutations


if __name__ == '__main__':
    main()
