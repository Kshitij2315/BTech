/******************************************************************************

WAP tp print *****
             ****
             ***
             **
             * 

*******************************************************************************/
#include <stdio.h>

int main()
{
    int i,j,N,_N;
    N=0;
    
    printf("Enter Num: ");
    scanf("%d",&N);
    
    _N= N;
    
      for (i = 1; i <= _N; i++)
      {
          for(j = N; j >= 1; j--)
          {
              printf("*");
          }
          
          printf("\n");
          N = N - 1;
      }
   
      /*for (; N>0; N--)
      {
          for(j = N; j >= 1; j--)
          {
              printf("*");
          }
          
          printf("\n");
          
      }*/
    return 0;
}



