/******************************************************************************

WAP to Read and Print an Array 

******************************************************************************/
#include <stdio.h>

int main()
{
    int arr[10],i,N;
    
    printf("Enter How many Elements you want: ");
    scanf("%d",&N);
    
     for(i=0; i<N; i++)
     {
         printf("Enter Element arr[%d}: ",i);
         scanf("%d",&arr[i]);
     }
     
     for(i=0; i<N; i++)
     {
         printf("arr[%d] = %d\n",i,arr[i]);
     }

    return 0;
}
