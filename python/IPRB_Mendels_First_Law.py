#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from fractions import Fraction as fb


def aa_prob(k, m, n):
    size = k + m + n
    prob_aa_aa = fb(n, size) * fb(n-1, size - 1)
    prob_Aa_aa = fb(m, size) * fb(n, size - 1)
    prob_Aa_Aa = fb(1, 4) * fb(m, size) * fb(m - 1, size - 1)
    return prob_aa_aa + prob_Aa_aa + prob_Aa_Aa


def main():
    with open(sys.argv[1]) as file:
        file = file.read().strip()
    k = int(file.split()[0])
    m = int(file.split()[1])
    n = int(file.split()[2])
    size = k + m + n
    print round(1 - aa_prob(k, m, n), 5)


if __name__ == '__main__':
    main()
