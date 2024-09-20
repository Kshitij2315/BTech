/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *prev, *next;
};

struct node *start = NULL;

struct node *createNode()
{
    struct node *newnode;
    newnode = (struct node *) malloc(sizeof(struct node));
    newnode -> next = NULL;
    newnode -> prev = NULL;
    
    return newnode;
}

void createList()
{
    int data;
    struct node *newnode, *temp;
    
    printf("Enter Data: ");
    scanf("%d",&data);
    
    newnode = createNode();
    
    newnode -> data = data;
    
    if(start == NULL)
    {
        start = newnode;
    }
    else
    {
        temp = start;
        
        while(temp-> next != NULL)
        {
            temp = temp -> next;
        }
        
        temp -> next = newnode;
        newnode -> prev = temp;
    }
}

void display()
{
    struct node *temp;
    
    temp = start;
    
    while(temp != NULL)
    {
        printf("%d -> ", temp -> data);
        
        temp = temp -> next;
    }
}

void displayRev()
{
    struct node *temp;
    
    temp = start;
    
    while(temp -> next != NULL)
    {
        temp = temp -> next;
    }
    
    while(temp != NULL)
    {
        printf("%d <-",temp -> data);
        
        temp = temp -> prev;
    }
}

void search()
{
    int find, found = 0;
    struct node *temp;
    
    printf("Enter Element to search for: ");
    scanf("%d",&find);
    
    temp = start;
     
    while(temp != NULL)
    {
        if( temp -> data == find)
        {
            found = 1;
            break;
        }
        else
        {
            temp =temp -> next;
        }
    }
    
    if( found == 1)
    {
        printf("\nThe element %d is found in the given Linked List.",find);
    }
    else
    {
        printf("\nThe element %d is not found in the given Linked List. ",find);
    }
}

void insertAfter()
{
    int after, data;
    struct node *temp, *prev, *newnode;
    
    printf("Enter element to insert after: ");
    scanf("%d",&after);
    
    prev = NULL;
    temp = start;
    
    while(temp != NULL)
    {
        if(temp -> data == after)
        {
            prev = temp;
            temp = temp -> next;
            
            break; 
        }
        else
        {
            prev = temp;
            temp = temp -> next;
        }
    }
    
    
    newnode = createNode();
    
    printf("\nEnter data to insert after %d: ",after);
    scanf("%d",&data);
    
    newnode -> data = data;
    
    if(temp == NULL)
    {
        prev -> next = newnode;
        newnode -> prev = prev;
    }
    else
    {
        newnode -> prev = prev;
        prev -> next = newnode;
        
        newnode -> next = temp;
        temp -> prev = newnode; 
    }
}

void insertBefore()
{
    int before, data;
    struct node *temp, *prev, *newnode;
    
    printf("\nEnter element to insert before: ");
    scanf("%d",&before);
    
    prev = NULL;
    temp = start;
    
    while(temp != NULL)
    {
        if(temp -> data == before)
        {
            break;
        }
        else
        {
            temp = temp -> next;
        }
        
    }
    
    newnode = createNode();
    
    printf("\nEnter data to insert before %d: ",before);
    scanf("%d",&data);
    
    newnode -> data = data;
    
    if(prev == NULL)
    {
        newnode -> next = temp;
        temp -> prev = newnode;
    }
    else
    {
        newnode -> next = temp;
        temp -> prev = newnode;
    
        newnode -> prev = prev;
        prev -> next = newnode;  
    }
}

int main()
{
    int ans=1;
    while (ans > 0)
    {
        printf("\n--------------------------------");
        printf("\n 1. To CreateList: ");
        printf("\n 2. To Search: ");
        printf("\n 3. To Display: ");
        printf("\n 4. To Insert After: ");
        printf("\n 5. To Insert Before: ");
        printf("\n 6. To Delete: ");
        printf("\n 7. To DisplayReverse: ");
        printf("\n\nEnter your choice: ");
        scanf("%d",&ans);
        printf("--------------------------------\n\n");
        
        switch(ans)
        {
        case 1: createList(); 
                break;
        case 2: search(); 
                break;
        case 3: display(); 
                break;
        case 4: insertAfter(); 
                break; 
        case 5: insertBefore(); 
                break;
        /*case 6: delete(); 
                break;*/
        case 7: displayRev();
                break;
        }
    }


    return 0;
}

