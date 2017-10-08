#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import itertools

def main():
    n = int(sys.argv[1])
    n_permutations = itertools.permutations(range(1, n+1))
    count = 0
    print_string = ''
    for i in n_permutations:
        count += 1
        for j in i:
            print_string += str(j) + ' '
        print_string += '\n'
    print count
    print print_string


if __name__ == '__main__':
    main()
