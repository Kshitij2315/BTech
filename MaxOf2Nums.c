/******************************************************************************

WAP to print Maximum of Two Numbers 

*******************************************************************************/
#include <stdio.h>

int main()
{
    int Num1=0.0;
    int Num2=0.0;
    
    printf("Enter First Number: ");
    scanf("%d",&Num1);
    
    printf("Enter Second Number: ");
    scanf("%d",&Num2);
    
      if (Num1>Num2)
      {
          printf("The Maximum Number is: %d",Num1);
      }
      else
      {
          printf("The Maximum Number is: %d",Num2);
      }

    return 0;
}