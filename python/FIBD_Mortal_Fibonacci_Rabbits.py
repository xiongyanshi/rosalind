#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
memo = {}


def fib(n, m):
    args = (n, m)
    if args in memo:
        return memo[args]
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n < m + 1:
        ans = fib(n-1, m) + fib(n-2, m)
    else:
        ans = fib(n-1, m) + fib(n-2, m) - fib(n-m-1, m)
    memo[args] = ans
    return ans


def main():
    filename = sys.argv[1]
    with open(filename) as file:
        file = file.read().strip().split()
    n_month = int(file[0])
    m_life = int(file[-1])
    print fib(n_month, m_life)
    '''
    for i in range(1, 10):
        print '{} -> {}'.format(i, fib(i, 3))
    '''


if __name__ == '__main__':
    main()
