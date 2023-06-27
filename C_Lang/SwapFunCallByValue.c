/******************************************************************************

 WAF to swap/interchange two values os variables
 
 SwapFun.c

*******************************************************************************/
#include <stdio.h>

void swapFun(int Num1, int Num2)
{
    int swap;
    
    swap=Num2;
    Num2=Num1;
    Num1=swap;
    
    printf("\nFirst Number 'Num1'= %d\n",Num1);//Shows the Swaped Value
    printf("Second Number 'Num2' = %d",Num2);//Shows the Swaped Value
}

int main()
{
    int Num1, Num2;
    
    printf("Enter First Number = ");
    scanf("%d",&Num1);
    
    printf("Enter Second Number = ");
    scanf("%d",&Num2);
    
    swapFun(Num1, Num2);

    printf("\n*First Number 'Num1'= %d\n",Num1);//Shows the Orginal Value Of Variable
    printf("*Second Number 'Num2' = %d",Num2);//Shows the Orginal Value Of Variable

    return 0;
}
