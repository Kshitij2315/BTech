/******************************************************************************

WAP to convert Decimal Number to Binary Equivalent Number

*******************************************************************************/
#include <stdio.h>

int main()
{
    int N, N1, M, rem;
    N=M=0;
    
    printf("Enter a Number: ");
    scanf("%d",&N);
    
    N1 = N;
    
       for(; N > 0; N = N / 2)
       {
           rem = N % 2;
           M = M * 10 + rem;
       }  
          
          for(; M > 0; M = M / 10)
          {
             rem = M % 10;
             printf("%d", rem);
          }
             
             if(N1 % 2 == 0)
             {
                printf("0");
             }
       
    return 0;
}
