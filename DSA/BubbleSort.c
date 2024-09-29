/******************************************************************************

Bubble Sort

*******************************************************************************/
#include <stdio.h>

#include <stdio.h>

#define MAX 5
int arr[MAX];

void getArrElements()
{
    int i; 
    
    for(i=0; i < MAX; i++)
    {
        printf("Enter data: ");
        scanf("%d",&arr[i]);
    }
}

void display()
{
    int i; 
    
    for(i=0; i < MAX; i++)
    {
        printf("%d, ",arr[i]);
    }
}

void bubbleSort()
{
    int i, r, temp;
    
    for(r = 0; r < MAX-1; r++)
    {
        for(i = 0; i < MAX-1; i++)
        {
            if(arr[i] > arr[i+1])        // For decending '<'  
            {
               temp = arr[i];
               arr[i]=arr[i+1];
               arr[i+1]=temp;
            }
        }
    }
    
    printf("Sorted");
}

int main()
{
    int a;
   
    do
    {
        printf("\n\n--------------------\n");
        printf("0. Exit\n");
        printf("1. Enter Data\n");
        printf("2. Sort\n");
        printf("3. Display\n");
        printf("--------------------\n\n");
        
        printf("Enter your choice: ");
        scanf("%d",&a);
        printf("\n--------------------\n\n");
        
        switch(a)
        {
            case 1: getArrElements();
                    break;
        
            case 2: bubbleSort();
                    break;
                
            case 3:display();
                    break;
        }
        
    }while( a != 0);
    
    return 0;
}
