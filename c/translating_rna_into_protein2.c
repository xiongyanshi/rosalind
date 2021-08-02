#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "bio.h"


int main()
{
	char *seq_rna = (char *) malloc(10000);
	char *seq_aa = (char *) malloc(3334);

	fgets(seq_rna, 10000, stdin);
	//printf("%s\n", seq_rna);

	int i=0;
	char a;
	while (i < strlen(seq_rna)/3)
	{
		a = translate(seq_rna + i*3);
		if (a == '*')
			break;
		*(seq_aa + i) = a;
		i++;
	}
    *(seq_aa + i) = '\0';
	printf("%s\n", seq_aa);

	free(seq_rna);
	free(seq_aa);
}
