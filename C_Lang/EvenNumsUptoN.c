/******************************************************************************

WAP to print only Even Number Upto N Nums

*******************************************************************************/
#include <stdio.h>

int main()
{
   int i=0;
   int N=0;
   
   printf("Upto: ");
   scanf("%d",&N);
   
   printf("The Even Numbers are:");
   
       while (i<=N)
       {
           printf("%d\n",i);
           
           i = i + 1;
       }

    return 0;
}
