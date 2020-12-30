#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import mlpy
# import itertools


def incre_sub(sequence):
    """return all the increasing subsequences as a list"""
    result = []
    for i in range(len(sequence)):
        i_above = [sequence[i], ]
        for j in sequence[i:]:
            if j > sequence[i]:
                i_above.append(j)

        result.append(i_above)
    return result


def lcs(xstr, ystr):
    """
    >>> lcs('thisisatest', 'testing123testing')
    'tsitest'
    """
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + lcs(xs, ys)
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)


def longest_increasing_subseq(input_list, incre=True):
    """
    return the longest increasing subsequence
    """
    """
    subseqs = subseq(input_list)
    if incre:
        incre_subseq = [sub for sub in subseqs if increase(sub)]
        return max(incre_subseq, key=len)
    else:
        decre_subseq = [sub for sub in subseqs if increase(sub, False)]
        return max(decre_subseq, key=len)
    """
    pass


def main():
    with open(sys.argv[1]) as handle:
        file = handle.read()
    n = int(file.split('\n')[0])
    input_list = map(int, file.split('\n')[1].split())
    print n # , input_list
    x_incre = range(1, n + 1)
    x_decre = x_incre[::-1]
    y = input_list
    incre_path = mlpy.lcs_std(x_incre, y)[1][1]
    decre_path = mlpy.lcs_std(x_decre, y)[1][1]
    incre_sub_list = [input_list[i] for i in incre_path]
    decre_sub_list = [input_list[i] for i in decre_path]
    for i in incre_sub_list:
        print i,
    print
    for j in decre_sub_list:
        print j,
    '''
    for i in incre_sub(input_list):
        print len(i), i
    '''


if __name__ == '__main__':
    main()
