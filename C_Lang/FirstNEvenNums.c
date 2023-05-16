/******************************************************************************

WAP to print First N even Numbers

*******************************************************************************/
#include <stdio.h>

int main()
{
    int i=2;
    int N=0;
    
    printf("FILL: First ______ Even Numbers: ");
    scanf("%d",&N);
    
    int c=2*N;
    
       while (i<=c)
       {
           printf("%d\n",i);
           i = i + 2;
       }

    return 0;
}