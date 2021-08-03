#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char s[1000];
	char t[1000];
	int i=0;


	fgets(s, 1000, stdin);
	fgets(t, 1000, stdin);

	s[strcspn(s, "\n")] = '\0';
	t[strcspn(t, "\n")] = '\0';

    while (i <= (strlen(s) - strlen(t)) )
	{
		if (strncmp(s+i, t, strlen(t)) == 0)
			printf("%d ", i+1);
		i++;
	}
	printf("\n");
}
