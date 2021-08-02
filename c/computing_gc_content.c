#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LENMAX 1024

float gc(char *s)
{
	int c=0;
	int i=0;
	while ((s[i] == 'A') || (s[i] == 'C') || (s[i] == 'G') || (s[i] == 'T'))
	{
		if (s[i] == 'G' || s[i] == 'C')
			c++;
		i++;
	}
	return  100.0*c/i;
}


int main()
{
	char name[20];
	char seq[1000];

	int in_name = 0;
	int in_seq = 0;

	char c;

	char max_name[20];
	float max_gc = 0.0;
	float igc = 0.0;

	while ((c = getchar()) != EOF)
	{
		if (c == '>')
		{
			if (! in_seq)
				in_name = 1;
			else
			{
				//printf("name: %s\n", name);
				//printf("seq : %s\n", seq);
				igc = gc(seq);
				if (igc >= max_gc)
				{
					max_gc = igc;
					strcpy(max_name, name);
				}
				name[0] = '\0';
				seq[0] = '\0';
				in_name = 1;
				in_seq = 0;
			}
		}
		else if (in_name)
		{
			if (c == '\n')
			{
				in_name = 0;
				in_seq = 1;
			}
			else
				strncat(name, &c, 1);
		}
		else if (in_seq)
		{
			if (c == '\n')
				;
			else
				strncat(seq, &c, 1);
		}
	}

	//printf("name: %s\n", name);
	//printf("seq : %s\n", seq);
	igc = gc(seq);
	if (igc >= max_gc)
	{
		max_gc = igc;
		strcpy(max_name, name);
	}

	printf("%s\n%f\n", max_name, max_gc);

}
