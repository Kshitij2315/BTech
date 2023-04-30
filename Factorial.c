/******************************************************************************

WAP to print Factorial of a Number

*******************************************************************************/
#include <stdio.h>

int main()
{
    int i=0;
    int N=0;
    int a=1;
    
    printf("Enter a Number to Factorize: ");
    scanf("%d",&N);
    
        while (N>=1)
        {
            a = a * N;
            
            printf("%d X ",N);
            
            N = N - 1;
        }
    printf("\b\b\b = %d",a);
    
    return 0;
}

