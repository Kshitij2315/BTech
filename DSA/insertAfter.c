/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

void display(int n, int arr[])
{
    int i;
     printf("The array elements: \n");
    
    for(i=0; i < n; i++)
    {
        printf("%d, ", arr[i]);
    }

}

void input(int n, int arr[])
{
    int i;
    
    printf("Enter elements: \n");
    
    for(i=0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    
}

int search(int n, int arr[], int s)
{
    int i, c = 0;
    //int s
    
    //printf("\nEnter an element to search for: ");
    //scanf("%d",&s);
    
    for(i = 0; i < n; i++)
    {
        if(arr[i] == s)
        {
            printf("Element %d found at position %d. \n", s, i+1);
            c = 1;
            break;
        }
    }
    
        if(c == 0)
        {
            printf("Element %d not found in the given array. \n", s);
        }
        
        return i;
}

int insertPosition(int n, int arr[])
{
    int i, a, temp;
    
    printf("\n\nEnter at position: ");
    scanf("%d",&a);
    
    for(i = n - 1; i >= a - 1 ; i--)
    {
        arr[i + 1] = arr[i];
    }
    
    printf("Enter element to input at position %d: ",a);
    scanf("%d",&arr[a - 1]);
    
    return n + 1;
}

int insertAfter(int n, int arr[])
{
    int i, j, e;
    
    printf("\nInsert element after: ");
    scanf("%d",&e);
    
    i = search(n, arr, e);
    
    for(j = n - 1; j > i - 1; j--)
    {
        arr[j + 1] = arr[j];
    }
    
    printf("Enter element to insert: ");
    scanf("%d",&arr[i + 1]);
    
    return n + 1;
}

int main()
{
    int n, i, arr[100];
    
    printf("Enter size of array: ");
    scanf("%d",&n);
    
    input(n, arr);
    display(n, arr);
    
    /*printf("\n_______________");
    
    search(n, arr);*/
    
   
    /*printf("\n_______________");
   
    n = insertPosition(n, arr);*/
    
   
    printf("\n_______________");
    
    n = insertAfter(n, arr);
    
   
    display(n , arr);
   
    return 0;
}
