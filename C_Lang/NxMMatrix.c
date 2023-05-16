/******************************************************************************

WAP to Read and Print NxM Matrix

******************************************************************************/
#include <stdio.h>

int main()
{
    int arr[100][100],i,j,N,M;
    
    printf("Enter How many Rows = ");
    scanf("%d",&N);
    
    printf("Enter How many columns = ");
    scanf("%d",&M);
    
     for(i=0; i<N; i++)
     {
        for(j=0; j<M; j++)
        {
             printf("Enter Element arr[%d][%d]: ",i,j);
             scanf("%d",&arr[i][j]);
        }
     }
     for(i=0; i<N; i++)
     {
         for(j=0; j<M; j++)
         {
             printf("\narr[%d][%d] = %d ",i,j,arr[i][j]);
         }
         
     }
     
     printf("\n");
     
     for(i=0; i<N; i++)
     {
         for(j=0; j<M; j++)
         {
             printf("%d ",arr[i][j]);
         }
         
         printf("\n");
     }
   
    return 0;
}



