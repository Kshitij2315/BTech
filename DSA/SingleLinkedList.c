/******************************************************************************

 Link List create and display

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>

struct node *u;

struct node {
    int data;
    struct node *next;
}node;

struct node *start = NULL;

struct node *createNode(){
    struct node *newnode;
    newnode = (struct node *) malloc(sizeof(struct node));
    newnode -> next = '\0';
} 

void createList(){
    int data=0;
    struct node *newnode;
    
        printf("\nEnter data: "); 
        scanf("%d",&data);
        
        newnode=createNode();
        newnode -> data = data;
        
        if(start == NULL ){ // only for first time
           start = newnode; 
        }else
        {
            struct node *temp;
            temp = start;
            while(temp -> next != NULL) 
            temp = temp->next;
            
           
            temp -> next = newnode; //linking
        }
}

void display(){
    
    struct node *temp;
    temp = start;
    while(temp  != NULL)
    {
        printf("%d -> ",temp-> data);
        temp = temp->next;
    }
    
}

void search()
{
    int find;
    struct node *temp;
    int found = 0;
    
    printf("\nEnter Data to Search for: ");
    scanf("%d",&find);
    
    temp = start;
    
    while( temp != NULL)
    {
        if(temp -> data == find)
        {
            found = 1;
            break;
        }
        else
        {
            temp = temp -> next;
        }   
    }
    
    if(found == 1)
    {
        printf("\nData is present in the List.\n\n");
    }
    else
    {
        printf("\nData is not present in the List.\n\n");
    }
} 

void insertAfter()
{
    int after, data;
    struct node *temp, *newnode;
    
    printf("Insert After: ");
    scanf("%d",&after);
    
    temp = start;
    
    while( temp != NULL)
    {
        if(temp -> data == after)
        {
            break;
        }
        else
        {
            temp = temp -> next;
        }   
    }
    
    newnode = createNode();
    
    printf("\nEnter data to insertAfter %d: ",after); 
    scanf("%d",&data);
    
    newnode -> data = data;
    
    newnode -> next = temp -> next;
    
    temp -> next = newnode;
}

void insertBefore()
{
    int before, data;
    struct node *temp, *newnode,*prev;
    
    printf("Insert Before: ");
    scanf("%d",&before);
    
    printf("\nEnter data to insertBefore %d: ",before);
    scanf("%d", &data);
    
    newnode = createNode();
    
    newnode->data = data;
    
    prev = NULL;
    temp = start;
    
    if(before != start -> data)
    {
        while( temp != NULL)
        {
            if(temp -> data == before)
            {
                break;
            }
            else
            {
                prev = temp;
                temp = temp -> next;
            }   
        } 
        
        prev->next = newnode;
    }
    else
    {
        newnode -> next = start;
        start = newnode;
    }
    
    newnode->next = temp;
    
   
}

void delete()
{
    int data;
    struct node *temp, *newnode,*prev;
    
    printf("Enter data to be deleted: ");
    scanf("%d",&data);
    
    prev = NULL;
    temp = start;
    
    if(data != start -> data)
    {
        while( temp != NULL)
        {
            if(temp -> data == data)
            {
                break;
            }
            else
            {
                prev = temp;
                temp = temp -> next;
            }
        }
        
        prev->next = temp->next;
    }
    else
    {
        start = start -> next;
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
        case 6: delete(); 
                break;
        }
    }
    
    return 0;
}