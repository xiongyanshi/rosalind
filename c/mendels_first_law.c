#include <stdio.h>

int main()
{
	long k,m,n;
	float a;
	float f;
	float f_AA_AA, f_AA_Aa, f_AA_aa;
	float f_Aa_AA, f_Aa_Aa, f_Aa_aa;
	float f_aa_AA, f_aa_Aa;

	scanf("%ld%ld%ld", &k, &m,&n);
	a = k + m + n;
	//printf("k=%ld, m=%ld, n=%ld\n", k, m, n);

	f_AA_AA = k/a * ((k-1)/(a-1));
	f_AA_Aa = k/a * (m/(a-1));
	f_AA_aa = k/a * (n/(a-1));

	f_Aa_AA = m/a * (k/(a-1));
	f_Aa_Aa = m/a * ((m-1)/(a-1)) * 3/4;
	f_Aa_aa = m/a * (n/(a-1)) * 1/2;

	f_aa_AA = n/a * (k/(a-1));
	f_aa_Aa = n/a * (m/(a-1)) * 1/2;

    f = f_AA_AA + f_AA_Aa + f_AA_aa + \
	    f_Aa_AA + f_Aa_Aa + f_Aa_aa + \
		f_aa_AA + f_aa_Aa;

	printf("%f\n", f);
}
