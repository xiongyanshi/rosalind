#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import itertools


def subseq(sequence):
    """return all sub-sequences as a list"""
    length = len(sequence)
    result = []
    for i in range(2, length):
        delete_index = itertools.permutations(range(length), i)
        for loci in delete_index:
            if increase(map(int, loci)):
                seq = [sequence[i] for i in loci]
                result.append(seq)
    return result


def increase(list, incre=True):
    """retur True if items in list is in increasing trend"""
    for i in range(len(list) - 1):
        if incre:
            if list[i + 1] < list[i]:
                return False
        else:
            if list[i + 1] > list[i]:
                return False
    return True


def longest_increasing_subseq(input_list, incre=True):
    """
    return the longest increasing subsequence
    """
    subseqs = subseq(input_list)
    if incre:
        incre_subseq = [sub for sub in subseqs if increase(sub)]
        return max(incre_subseq, key=len)
    else:
        decre_subseq = [sub for sub in subseqs if increase(sub, False)]
        return max(decre_subseq, key=len)


def main():
    with open(sys.argv[1]) as handle:
        file = handle.read()
    input_list = map(int, file.split('\n')[1].split())
    print input_list

    longest_incre_sub = longest_increasing_subseq(input_list)
    for i in longest_incre_sub:
        print i,
    print
    longest_decre_sub = longest_increasing_subseq(input_list, False)
    for j in longest_decre_sub:
        print j,


if __name__ == '__main__':
    main()
