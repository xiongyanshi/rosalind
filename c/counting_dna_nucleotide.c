#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int a,c,g,t;
	int n;

	a = c = g = t = 0;

	while ( (n=getchar()) != EOF)
		if (toupper(n) == 'A')
			a++;
		else if (toupper(n) == 'C')
			c++;
		else if (toupper(n) == 'G')
			g++;
		else if (toupper(n) == 'T')
			t++;

	printf("%d %d %d %d\n", a, c, g, t);
}
