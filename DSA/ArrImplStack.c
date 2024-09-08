/******************************************************************************

Array Implimentation of Stack.

*******************************************************************************/
#include <stdio.h>

#define MAX 100
int stack[MAX];
int top = -1;

void push(int x)
{
    if(top != MAX - 1)
    {
        top++;
        stack[top] = x;
    }
    else 
    {
        printf("Stack Overflow \n");
    }
}

int pop()
{
    if(top != -1)
    {
        return stack[top--];
    }
    else
    {
        printf("Stack Underflow \n");
        
        return 0;
    }
}

int main()
{
    int num, x;
    
    printf("Enter a Number to Push: ");
    scanf("%d",&num);
    
    push(num);
    
    /*push(7);
    push(12);*/
    
    x = pop();
    
    printf("%d \n",x); //12
    
    x = pop();
    
    printf("%d \n",x); //7*/
    
    return 0;
}
