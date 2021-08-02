#include <stdio.h>

int main()
{
	int n, k;

	scanf("%d%d", &n, &k);
	//printf("n=%d, k=%d\n", n, k);

	long a=1, b=1, c;
	while (n-2 > 0)
	{
		c = b + a*k;
		a = b;
		b = c;
		n--;
	}
	printf("%ld\n",c);

}

