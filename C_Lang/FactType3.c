/*******************************************************************

Factorial of a Number

// Modular programming
// Non returning , but  parameters

FactType3.c

*******************************************************************/
#include <stdio.h>

void calFact(int Num) //Recived "num" value in new variable "Num"
{
    
    int fact;
    

    for(fact=1; Num>=1; Num--)
    {
        fact=fact*Num;  
        printf("%d*",Num);
    }
 
 printf("\b=%d",fact);

 
} //end of calFact


int main()
{
   int num;
   
   printf("Input a num = ");
    scanf("%d",&num);
    
   calFact(num); //"num" value passed tom calFact();
   
   return 0;
}
