/******************************************************************************

 Link List create and display

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
}node;

struct node *start = NULL;

struct node *createNode(){
    struct node *newnode;
    newnode = (struct node *) malloc(sizeof(struct node));
    newnode -> next = ' ';
} 

void createList(){
    int data=0;
    struct node *newnode;
    
        printf("nEnter data: n"); 
        scanf("%d",&data);
        
        newnode=createNode();
        newnode -> data = data;
        
        if(start == NULL ){ // only for first time
           start = newnode; 
        }else{
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

int main()
{
    int ans=1;
    while (ans >0){
        printf ("n 1. for createList: ");
        printf("n 2. for display: ");
        printf("nEnter your choice");
        scanf("%d",&ans);
        
        switch(ans){
        case 1: createList(); break;
        case 2: display(); break;


        
        }
    }
    return 0;
}