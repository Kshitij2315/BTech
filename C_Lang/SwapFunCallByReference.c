/******************************************************************************

 WAF to swap/interchange two values os variables
 
 SwapFun.c

  Call By Refrence

*******************************************************************************/
#include <stdio.h>

void swapFun(int *Num1, int *Num2)
{
    int swap;
    
    swap=*Num2;
    *Num2=*Num1;
    *Num1=swap;
    
    printf("\nFirst Number 'Num1'= %d\n",*Num1);//Shows the Swaped Value
    printf("Second Number 'Num2' = %d",*Num2);//Shows the Swaped Value
}

int main()
{