/******************************************************************************

WAP to print 1
             22
             333
             4444
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
         for(j=1; j<=i; j++)
         {
             printf("%d",i);
         }
         
       printf("\n");     
     }

    return 0;
}
