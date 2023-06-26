/*******************************************************************

Factorial of a Num

// Modular programming
// returning  and  parameters

FactType4.c

*******************************************************************/
#include <stdio.h>

// Modular programming
// returning , and  parameters

int calFact(int Num) //Recived "num" value in new variable "Num"
{
    
    int fact;
    

    for(fact=1; Num>=1; Num--)
    {
        fact=fact*Num;  
        printf("%d*",Num);
    }
 
 return fact;

 
} //end of calFact


int main()
{
   int num, ans;
   
   printf("Input a num = ");
    scanf("%d",&num);
    
   ans=calFact(num); //"num" value passed tom calFact();
   
   printf("\b=%d",ans);
   
   return 0;
}
