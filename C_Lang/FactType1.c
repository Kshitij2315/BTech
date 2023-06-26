/*******************************************************************

Factorial Function 

// Simplest way
// Modular programming
// non returning , no parameters

FactType1.c

*******************************************************************/
#include <stdio.h>

void calFact(){
    
    int num, fact;
    printf("Input a num = ");
    scanf("%d",&Num);

    for(fact=1; Num>=1; Num--)
    {
        fact=fact*Num;  
        printf("%d*",Num);
    }
 
 printf("=%d",fact);
} //end of calFact


int main()
{
   calFact(); 
   return 0;
}
