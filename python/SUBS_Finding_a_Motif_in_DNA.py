#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def find_sub(string, sub_string):
    result = []
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:].startswith(sub_string):
            result.append(i + 1)
    return result


def main():
    with open(sys.argv[1]) as file:
        file = file.read().strip().split('\n')
    target_seq = file[0]
    sub_seq = file[1]
    print find_sub(target_seq, sub_seq)


if __name__ == '__main__':
    main()
