/******************************************************************************

WAP to print a Number in Words

*******************************************************************************/
#include <stdio.h>

int main()
{
   int N,M,d;
   N=M=0;
   
   printf("Enter Any Number: ");
   scanf("%d",&N);
   
      for(; N > 0; N = N / 10)
      {
          d = N % 10;
          M = M * 10 + d;
      }
    
         for(; M > 0; M = M / 10)
         {
             d =  M % 10;
             
             switch(d)
             {
                 case 0 : printf("Zero "); break;
                 case 1 : printf("One ");  break; 
                 case 2 : printf("Two ");  break;
                 case 3 : printf("Three ");break;
                 case 4 : printf("Four "); break;
                 case 5 : printf("Five "); break;
                 case 6 : printf("Six ");  break;
                 case 7 : printf("Seven ");break; 
                 case 8 : printf("Eight ");break; 
                 case 9 : printf("Nine "); break;
             }
         }
     
    return 0;
}
