#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LENMAX 1024

int main()
{
	char name[20];
	char seq[1000];

	int in_name = 0;
	int in_seq = 0;

	char c;
	int gc_base;

	while ((c = getchar()) != EOF)
	{
		if ((c == '>') && (! in_name))
			in_name = 1;
		else if (in_name)
		{
			if (c == '\n')
			{
				printf("name: %s\n", name);
				name[0] = '\0';
				in_name = 0;
				in_seq = 1;
			}
			else
			{
				strncat(name, &c, 1);
			}
		}
	}

}
