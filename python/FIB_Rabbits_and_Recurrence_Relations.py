#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def seq_rab(n, k):
    a = 1
    b = 1
    i = 1
    while i < n:
        a, b = b, b + 3*a
        i += 1
    return a


def main():
    filename = sys.argv[1]
    with open(filename) as file:
        file = file.read().strip().split()
    n_month = int(file[0])
    k_little = int(file[-1])
    print seq_rab(n_month, k_little)


if __name__ == '__main__':
    main()
