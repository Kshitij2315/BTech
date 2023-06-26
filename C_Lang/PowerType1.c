/*******************************************************************

Power Function 

// Simplest way
// Modular programming
// non returning , no parameters

*******************************************************************/
#include <stdio.h>

void calPower()
{
   int n=0;
    int m=0;
    int a=1;
    
    printf("Enter Number: ");
    scanf("%d",&n);
    
    printf("To The Power: ");
    scanf("%d",&m);
    
    int ct=1;
    
       while (ct<=m)
       {
           a = a * n;
           
           ct = ct + 1;
       }
       
    printf("%d ^ %d = %d",n ,m ,a);     
}

int main()
{
    calPower();

    return 0;
}