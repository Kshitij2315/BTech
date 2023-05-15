/******************************************************************************

WAP to print Prime Numbers upto N

*******************************************************************************/
#include <stdio.h>

int main()
{
    int N,ct,i,flag ;
    N=0;
    flag=i=1;
    ct=2;
    
    printf("Enter: Upto Which Numbers: ");
    scanf("%d", &N);
    
     for(i=1; i<=N; i++)
     {
         for(ct=2,flag=1; ct<i; ct++)
         {
             if(i%ct==0)
             {
             flag=0;
             
             }
         }
         
       if (flag==1)
       {
           printf("%d\n",i);
       }
     }
   
    return 0;
}
