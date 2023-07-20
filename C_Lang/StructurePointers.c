/******************************************************************************

To input and output an struct array using pointers

*******************************************************************************/
#include <stdio.h>
struct account
{
    int acno;
    char name[80];
    float bal;
};

int main()
{
    //int arr[10], *ptr;
    int i;
    struct account arr[10],*ptr;
    //struct account *ptr;
    
    for(i=0;i<=1;i++)
    {
        printf("\n");
        
        printf("Enter Account Number: ");
        scanf("%d",&arr[i].acno);
        
        printf("Enter Name: ");
        scanf("%s",&arr[i].name);
        
        printf("Enter Balance: ");
        scanf("%f",&arr[i].bal);
    }
    
    ptr = arr;
    
    for(; ptr<=&arr[1]; ptr++)  //i=0; (ptr+i)<=&arr[1]; i++  //i=0; i<2; i++, ptr++
    {
        printf("\n\nAcc Number: %d\n Acc Name: %s\n Acc Balance: %f",ptr->acno, ptr->name, ptr->bal);
    }

    return 0;
}
