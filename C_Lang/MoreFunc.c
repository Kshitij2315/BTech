/******************************************************************************

WAP to print 1>length of a String
             2>Absolute Value of a Number
             3>Table of a Number

*******************************************************************************/
#include <stdio.h>

int calTABLE(int num)
{
    int multi,i;
    
    for(i=0;i<=10;i++)
    {
        multi = num * i;
        
        printf("%d * %d = %d\n",num,i,multi);
    }
    
}

int calSTR(char *str)
{
    int i;
    
    for (i = 0; str[i] != '\0'; i++);
    
    return i;
}

int calABS(int num)
{
    if(num<0)
    {
        num=num * -1;
    }
    
    return num;
}

int main()
{
    
    //Length of a String.
    
    char str[100],ans1;
    
    printf("\n\nEnter String: ");
    gets(str);
    
    ans1=calSTR(str);
    
    printf("The length os String is: %d\n\n",ans1);
    
    
    
    //Absolute Value of a Number.
    
    int num1,ans2;
    
    printf("Enter a Number: ");
    scanf("%d",&num1);
    
    ans2=calABS(num1);
    
    printf("The absolute value: %d\n\n",ans2);
    
    
    
    //Table of a Number.
    
    int num2;
    
    printf("Enter a Number: ");
    scanf("%d",&num2);
    
    calTABLE(num2);
    
    return 0;
}
