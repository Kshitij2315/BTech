/******************************************************************************

WAP to Read an Array and Print in Reverse Order

******************************************************************************/
#include <stdio.h>

int main()
{
    int arr[100],i,N;
    
    printf("Enter How many Elements you want: ");
    scanf("%d",&N);
    
     for(i=0; i<N; i++)
     {
         printf("Enter Element arr[%d]: ",i);
         scanf("%d",&arr[i]);
     }
     
     for(i=N-1; i>=0; i--)
     {
         printf("arr[%d] = %d\n",i,arr[i]);
     }

    return 0;
}
