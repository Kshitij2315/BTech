/******************************************************************************

Array implimentation of Queue.

*******************************************************************************/
#include <stdio.h>

#define MAX 100

int arr[MAX];
int top = -1;

void enqueue()
{
    int num;
    
    if(top != MAX - 1)
    {
        top++;
        
        printf("Enter a number to insert: ");
        scanf("%d",&num);
        
        printf("\n\n");
        
        arr[top] = num;
    }
    else 
    {
        printf("Queue Overflow \n");
    }
}

int dequeue()
{
    int i = 0, temp;
    
    if(top == -1)
    {
        printf("Queue Underflow");
        
        return 0;
    }
    else
    {
        temp = arr[i];
        
        for(i = 0; i < top; i++)
        {
            arr[i] = arr[i+1];
        }
        
        top--;
    }
    
    return temp;
}

void display()
{
    int i;
     printf("The array elements: \n");
    
    for(i=0; i <= top; i++)
    {
        printf("%d, ", arr[i]);
    }

}


void main()
{
    int n, i, c, del;
    
    do
    {
        printf("1. Enqueue\n");
        printf("2. Dequeue\n");
        printf("3. Display\n");
        printf("---------------------------\n\n");
    
        printf("Enter your choice: ");
        scanf("%d",&c);
    
        if(c == 1)
        {
            printf("\n\n");
            
            enqueue();
            
        }
        else if(c == 2)
        {
            del = dequeue();
        
            printf("\nDeleted Number: %d \n",del);
        }
        else if(c == 3)
        {
            display();
        
            printf("\n----------------\n");
        }
        else
        {
            printf("Wrong choice.\n Please try again.\n -------------------\n\n");
        }
        
    } while(c != 0);
}