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

struct node *search(int find)
{
    //int find;
    struct node *temp;
    int found = 0;
    
    /*printf("\nEnter Data to Search for: ");
    scanf("%d",&find);*/
    
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
    
    /*if(found == 1)
    {
        printf("\nData is present in the List.\n\n");
    }
    else
    {
        printf("\nData is not present in the List.\n\n");
    }*/
    
   return temp; 
} 

void insertAfter()
{
    int after, data;
    struct node *temp, *newnode;
    
    printf("Insert After: ");
    scanf("%d",&after);
    
    temp = search(after);
    
    newnode = createNode();
    
    printf("\nEnter data: "); 
    scanf("%d",&data);
    
    newnode -> data = data;
    
    newnode -> next = temp -> next;
    
    temp -> next = newnode;
}

int main()
{
    int ans=1;
    while (ans >0)
    {
        printf("\n 1. To CreateList: ");
        printf("\n 2. To Search: ");
        printf("\n 3. To Display: ");
        printf("\n 4. To Insert After: ");
        printf("\nEnter your choice: ");
        scanf("%d",&ans);
        
        switch(ans)
        {
        case 1: createList(); break;
        //case 2: search(); break;
        case 3: display(); break;
        case 4: insertAfter(); break;
        }
    }
    
    return 0;
}