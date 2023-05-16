/******************************************************************************

WAP to Read 1D Array Elements and Copy Values to Another Array in Reverse

******************************************************************************/
#include <stdio.h>

int main()
{
    int arr[100], ARR[100],i,j,N;
    
    printf("Enter How many Elements you want = ");
    scanf("%d",&N);
    
     for(i=0; i<N; i++)
     {
        printf("Enter arr[%d] =",i);
        scanf("%d",&arr[i]);
     }
     
     for(i=0, j=N-1; i<N && j>=0; i++,j--)
     {
        ARR[j]=arr[i]; 
     }
     
     for(j=0; j<N; j++)
     {
         printf("\nARR[%d] = %d",j,ARR[j]);
     }
   
    return 0;
}


