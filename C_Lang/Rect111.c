/******************************************************************************

WAP to print 11111
             22222
             33333
             44444
             55555
             
*******************************************************************************/
#include <stdio.h>

int main()
{
    int i,j,N;
    i=j=1;
    N=0;
    
    printf("Enter Number: ");
    scanf("%d",&N);
    
     for(i=1; i<=N; i++)
     {
         for(j=1; j<=N; j++)
         {
             printf("%d",i);
         }
         
       printf("\n");     
     }

    return 0;
}