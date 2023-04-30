/******************************************************************************

WAP to find Whether a Number is Prime or Not

*******************************************************************************/
#include <stdio.h>

int main()
{
    int N=0;
    int ct=2;
    int flag=1;
    
    printf("Enter a Number: ");
    scanf("%d",&N);
    
       while (ct<N)
       {
           if (N % ct == 0)
           {
               flag=0;
           }
        
        ct = ct + 1;
       }
       
     if (flag == 1)
     {
         printf("%d is a prime number",N);
     }
     else
     {
         printf("%d is not a prime number",N);
     }
    return 0;
}
