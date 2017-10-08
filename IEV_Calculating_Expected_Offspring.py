#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def main():
    with open(sys.argv[1]) as file:
        parameter = file.read().strip().split()
    parameter = [int(i) for i in parameter]
    print (parameter[0]*2 + parameter[1]*2 + parameter[2]*2 +
           parameter[3]*1.5 + parameter[4]*1)


if __name__ == '__main__':
    main()
