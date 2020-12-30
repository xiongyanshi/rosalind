#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import itertools


def lexiorder(s1, s2, order):
    """compare s1 and s2 based on order string"""
    check_length = len(s1) if len(s1) < len(s2) else len(s2)
    if s1[:check_length] == s2[:check_length]:
        return True if len(s1) < len(s2) else False
    else:
        for i in range(check_length):
            if s1[i] == s2[i]:
                pass
            elif order.index(s1[i]) < order.index(s2[i]):
                return True
            else:
                return False


def lexi_bubble_sort(input_list, order):
    """sort string in input_list lexicographically, using bubble sort"""
    for i in range(len(input_list)):
        for j in range(i):
            if lexiorder(input_list[i], input_list[j], order):
                input_list[j], input_list[i] = input_list[i], input_list[j]
    return input_list


def permu_str(string, n):
    """return all strings of length at most n formed from input string"""
    result_list = []
    for i in range(1, n + 1):
        permu_i = itertools.product(string, repeat=i)
        for j in permu_i:
            result_list.append(''.join(j))
    return result_list


def main():
    with open(sys.argv[1], 'r') as handle:
        file = handle.read()
    file = file.split('\n')
    in_string = ''.join(file[0].split())
    in_n = int(file[1])

    result = lexi_bubble_sort(permu_str(in_string, in_n), in_string)
    for i in result:
        print i


if __name__ == '__main__':
    main()
