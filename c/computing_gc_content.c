#include <stdio.h>
#include <stdlib.h>

#define LENMAX 1024

int main(int argc, char **argv)
{
	FILE *input;
	input = fopen( argv[1], "r");
	fclose(input);
}
