#include <stdio.h>
#include <string.h>

#define LENMAX 1024

int main()
{
	char a[LENMAX];
	char b[LENMAX];

	fgets(a, sizeof(a), stdin);
	//printf("%s\n", a);
	fgets(b, sizeof(b), stdin);
	//printf("%s\n", b);

	long len = strlen(a);
	long count = 0;
	while (--len >=0)
	{
		if (a[len] != b[len])
			count++;
	}
	printf("%ld\n",count);

}
