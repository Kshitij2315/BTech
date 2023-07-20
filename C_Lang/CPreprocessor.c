/******************************************************************************

C preprocessor

*******************************************************************************/
#include <stdio.h>

#define MAX 100
#define PIE 3.14

#ifdef MAX 
    #undef MAX
    #define MAX 10
#endif

#define  message_for(a, b)  \
    printf("\n" #a " and " #b ": We love you!\n")
   
#define MAX2(x, y)  (x > y) ? x : y //Ternary Operator

#ifndef MIN 
    #define MIN 0
#endif
   
int main()
{
    
    printf("\n%d \n%f\n", MAX, PIE);
    
    message_for(Ram, Shyam);
    
    printf ("\nMaximum of 5 and 7 is : %d\n",MAX2(5 , 7));
    
    printf ("\n %d \n",MIN);
    
    printf("\nDate :%s\n", __DATE__ );
    
    printf("\nTime :%s\n", __TIME__ );
    
    printf("\nLine Num: :%d\n", __LINE__ );
    
    printf("\nStandard Compiler Command :%d\n", __STDC__ );

    return 0;
}
