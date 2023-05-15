/******************************************************************************

WAP to print Fibonacci Series upto N

*******************************************************************************/
#include <stdio.h>

int main()
{
    int i,N,ct,c,d;
    i=N=d=0;
    ct=c=1;
    
    printf("Enter how many steps: ");
    scanf("%d",&N);
    
      for(;ct<=N;)
       {
           i = c + d;
           
           printf("%d  ",i);
           
           c = d;
           d = i;
           ct = ct + 1;
       }

    return 0;
}
