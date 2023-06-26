/*******************************************************************

Factorial Of a Number

// Modular programming
// returning , no parameters

FactType2.c

*******************************************************************/
#include <stdio.h>

int calFact(){
    
    int Num, fact;
    printf("Input a num = ");
    scanf("%d",&Num);

    for(fact=1; Num>=1; Num--)
    {
        fact=fact*Num;  
        printf("%d*",Num);
    }
 
 return fact;
 
} //end of calFact


int main()
{
   int ans;
   ans = calFact();
   printf("\b=%d",ans);
   return 0;
}
