#include <stdio.h>
#include <string.h>

char seq[1000];
void reverse(char *s);
void complement(char *s);

void reverse(char *s)
{
	char *start, *end, tmp;

	start = s;
	end = s + strlen(s) - 1;

	while (start < end)
	{
		tmp = *start;
		*start = *end;
		*end = tmp;
		start++;
		end--;
	}
}

void complement(char *s)
{
	while (*s != '\0')
	{
		if (*s == 'A') *s = 'T';
		else if (*s == 'T') *s = 'A';
		else if (*s == 'C') *s = 'G';
		else if (*s == 'G') *s = 'C';
		s++;
	}
}


int main()
{
	fgets(seq, 1000, stdin);
	reverse(seq);
	complement(seq);
	printf("%s\n", seq);

}
