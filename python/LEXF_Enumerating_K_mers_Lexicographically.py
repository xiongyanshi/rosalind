#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import itertools


def lexi(string):
    """
    return True if string is ordered lexicographically
    """
    pass


def main():
    with open(sys.argv[1]) as handle:
        file = handle.read().strip().split('\n')
    input_str = ''.join(file[0].split())
    input_k = int(file[1])

    pool = []
    for i in itertools.product(input_str, repeat=input_k):
        pool.append(''.join(i))
    for j in sorted(pool):
        print j


if __name__ == '__main__':
    main()
