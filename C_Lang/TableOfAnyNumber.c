/******************************************************************************

WAP tp print Table of a Number

*******************************************************************************/
#include <stdio.h>

int main()
{
    int i=1;
    int a=0;
    int N=0;
    
    printf("Table of: ");
    scanf("%d",&N);
    
        while (i<=10)
        {
            a = N * i;
            
            printf("%d X %d = %d\n",N,i,a);
            
            i = i + 1;
        }
    
    return 0;
}