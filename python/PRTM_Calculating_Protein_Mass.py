#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys


def main():
    mass_dict = {}
    with open('./data/monoisotopic_mass_table.txt', 'r') as file:
        for i in file.readlines():
            mass_dict[i.split()[0]] = float(i.split()[-1])
    with open(sys.argv[1]) as para_file:
        protein_seq = para_file.read().strip()
    mass = 0.0
    for peptide in protein_seq:
        mass += mass_dict[peptide]
    print mass

if __name__ == '__main__':
    main()
