#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def p_nk(n, k):
    """return permutation counts of n, k"""
    multi = 1
    for i in range(n - k + 1, n + 1):
        multi *= i
    return multi


def main():
    with open(sys.argv[1]) as handle:
        file = handle.read()
    input = file.strip().split()
    print input
    print p_nk(int(input[0]), int(input[1])) % 1000000


if __name__ == '__main__':
    main()
