import itertools
import sys

def main():
    filename = 'data/rosalind_kmer.txt'
    seq = ''
    for line in open(filename):
        if line.startswith('>'):
            continue
        seq += line.strip()
    kseq = []
    for i in range(len(seq) - 3):
        kseq.append(seq[i:i+4])

    for i in itertools.product('ACGT',repeat=4):
        mer = ''.join(i)
        print kseq.count(mer),
    return 0

if __name__ == "__main__":
    main()
