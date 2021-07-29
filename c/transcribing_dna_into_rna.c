#include <stdio.h>
#include <ctype.h>

int main()
{
	int n;
	while ( (n=getchar()) != EOF)
	{
		if (n == 'T')
		{
			putchar('U');
			continue;
		}
		putchar(n);
	}
}
