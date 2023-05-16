/******************************************************************************

WAP to print the Sum of Digits of a Number

*******************************************************************************/
#include <stdio.h>

int main()
{
    int number, digit, sum = 0;

    printf("Enter a number: ");
    scanf("%d", &number);
    
        if (number < 0)
        {
           number = number * -1;
        }
     
            while (number > 0) 
            {
               digit = number % 10;
               sum = sum + digit;
               number = number / 10;
            }

    printf("Sum of digits = %d\n", sum);

    return 0;
}


