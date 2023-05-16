/******************************************************************************
WAP to print Whether a Number is Divisible by Another Number or Not

*******************************************************************************/
#include <stdio.h>

int main()
{
   int num1=0;
   int num2=0;
   int remainder=0;
   
   printf("Enter First Number: ");
   scanf("%d",&num1);
   
   printf("Enter Second Number: ");
   scanf("%d",&num2);
   
   remainder=num1%num2;
   
       if (remainder==0)
       {
           printf("The Number is Divisible");
       } 
       else
       {
           printf("The Number is Not Divisible");
       }

    return 0;
}