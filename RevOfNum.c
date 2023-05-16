/******************************************************************************

WAP to Print and Store Reverse of a Number 

*******************************************************************************/
#include <stdio.h>

int main()
{
    int N,d,M;
    
    printf("Enter Number: ");
    scanf("%d",&N);
    
    for(M=0; N>0; N=N/10)
    {
        d=N%10;
        
        printf("%d",d);
        
        M = M * 10 + d;
    }
    return 0;
}
