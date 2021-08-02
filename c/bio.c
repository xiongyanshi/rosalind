#include <string.h>
#include "bio.h"

char translate(char s[])
{
	if      (strncmp(s, "UUU", 3) == 0) return 'F';
	else if (strncmp(s, "CUU", 3) == 0) return 'L';
	else if (strncmp(s, "AUU", 3) == 0) return 'I';
    else if (strncmp(s, "GUU", 3) == 0) return 'V';
    else if (strncmp(s, "UUC", 3) == 0) return 'F';
    else if (strncmp(s, "CUC", 3) == 0) return 'L';
    else if (strncmp(s, "AUC", 3) == 0) return 'I';
    else if (strncmp(s, "GUC", 3) == 0) return 'V';
    else if (strncmp(s, "UUA", 3) == 0) return 'L';
    else if (strncmp(s, "CUA", 3) == 0) return 'L';
    else if (strncmp(s, "AUA", 3) == 0) return 'I';
    else if (strncmp(s, "GUA", 3) == 0) return 'V';
    else if (strncmp(s, "UUG", 3) == 0) return 'L';
    else if (strncmp(s, "CUG", 3) == 0) return 'L';
    else if (strncmp(s, "AUG", 3) == 0) return 'M';
    else if (strncmp(s, "GUG", 3) == 0) return 'V';
    else if (strncmp(s, "UCU", 3) == 0) return 'S';
    else if (strncmp(s, "CCU", 3) == 0) return 'P';
    else if (strncmp(s, "ACU", 3) == 0) return 'T';
    else if (strncmp(s, "GCU", 3) == 0) return 'A';
    else if (strncmp(s, "UCC", 3) == 0) return 'S';
    else if (strncmp(s, "CCC", 3) == 0) return 'P';
    else if (strncmp(s, "ACC", 3) == 0) return 'T';
    else if (strncmp(s, "GCC", 3) == 0) return 'A';
    else if (strncmp(s, "UCA", 3) == 0) return 'S';
    else if (strncmp(s, "CCA", 3) == 0) return 'P';
    else if (strncmp(s, "ACA", 3) == 0) return 'T';
    else if (strncmp(s, "GCA", 3) == 0) return 'A';
    else if (strncmp(s, "UCG", 3) == 0) return 'S';
    else if (strncmp(s, "CCG", 3) == 0) return 'P';
    else if (strncmp(s, "ACG", 3) == 0) return 'T';
    else if (strncmp(s, "GCG", 3) == 0) return 'A';
    else if (strncmp(s, "UAU", 3) == 0) return 'Y';
    else if (strncmp(s, "CAU", 3) == 0) return 'H';
    else if (strncmp(s, "AAU", 3) == 0) return 'N';
    else if (strncmp(s, "GAU", 3) == 0) return 'D';
    else if (strncmp(s, "UAC", 3) == 0) return 'Y';
    else if (strncmp(s, "CAC", 3) == 0) return 'H';
    else if (strncmp(s, "AAC", 3) == 0) return 'N';
    else if (strncmp(s, "GAC", 3) == 0) return 'D';
    else if (strncmp(s, "UAA", 3) == 0) return '*';
    else if (strncmp(s, "CAA", 3) == 0) return 'Q';
    else if (strncmp(s, "AAA", 3) == 0) return 'K';
    else if (strncmp(s, "GAA", 3) == 0) return 'E';
    else if (strncmp(s, "UAG", 3) == 0) return '*';
    else if (strncmp(s, "CAG", 3) == 0) return 'Q';
    else if (strncmp(s, "AAG", 3) == 0) return 'K';
    else if (strncmp(s, "GAG", 3) == 0) return 'E';
    else if (strncmp(s, "UGU", 3) == 0) return 'C';
    else if (strncmp(s, "CGU", 3) == 0) return 'R';
    else if (strncmp(s, "AGU", 3) == 0) return 'S';
    else if (strncmp(s, "GGU", 3) == 0) return 'G';
    else if (strncmp(s, "UGC", 3) == 0) return 'C';
    else if (strncmp(s, "CGC", 3) == 0) return 'R';
    else if (strncmp(s, "AGC", 3) == 0) return 'S';
    else if (strncmp(s, "GGC", 3) == 0) return 'G';
    else if (strncmp(s, "UGA", 3) == 0) return '*';
    else if (strncmp(s, "CGA", 3) == 0) return 'R';
    else if (strncmp(s, "AGA", 3) == 0) return 'R';
    else if (strncmp(s, "GGA", 3) == 0) return 'G';
    else if (strncmp(s, "UGG", 3) == 0) return 'W';
    else if (strncmp(s, "CGG", 3) == 0) return 'R';
    else if (strncmp(s, "AGG", 3) == 0) return 'R';
    else if (strncmp(s, "GGG", 3) == 0) return 'G';
	else                                return '*';
}

