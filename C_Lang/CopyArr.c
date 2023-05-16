/******************************************************************************

WAP to Read 1D Array Elements and Copy Values to Another 1D Array

******************************************************************************/
#include <stdio.h>

int main()
{
    int arr[100], ARR[100],i,N;
    
    printf("Enter How many Elements you want = ");
    scanf("%d",&N);
    
     for(i=0; i<N; i++)
     {
        printf("Enter arr[%d] =",i);
        scanf("%d",&arr[i]);
     }
     
     for(i=0; i<N; i++)
     {
         ARR[i]=arr[i];
     }
     
     for(i=0; i<N; i++)
     {
         printf("\nARR[%d] = %d",i,ARR[i]);
     }
   
    return 0;
}


