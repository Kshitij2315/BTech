/******************************************************************************

WAP to Read an Array and Print Sum of ONLY Prime Numbers

******************************************************************************/
#include <stdio.h>

int main()
{
    int arr[100],i,N,Sum,flag,ct;
    
    printf("Enter How many Elements you want: ");
    scanf("%d",&N);
    
     for(i=0; i<N; i++)
     {
         printf("Enter Element arr[%d]: ",i);
         scanf("%d",&arr[i]);
     }
     
     for(i=0; i<N; i++)
     {
         for(ct=2,flag=1; ct<arr[i]; ct++)
         {
             if(arr[i]%ct==0)
             {
                 flag=0;
             }
         }
         if(flag==1)
         {
             Sum = Sum + arr[i];
         }
     }
     
     printf("Sum = %d",Sum);
     
    return 0;
}


