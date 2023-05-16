/******************************************************************************

WAP to Read an Array and Print ONLY Even Numbers

******************************************************************************/
#include <stdio.h>

int main()
{
    int arr[100],i,N,Sum;
    
    printf("Enter How many Elements you want: ");
    scanf("%d",&N);
    
     for(i=0; i<N; i++)
     {
         printf("Enter Element arr[%d]: ",i);
         scanf("%d",&arr[i]);
     }
     
     for(i=0,Sum=0; i<N; i++)
     {
        if(arr[i]%2==0)
        {
            printf ("\narr[%d]= %d",i,arr[i]);
        }
     }

    return 0;
}

