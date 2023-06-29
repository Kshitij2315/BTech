/******************************************************************************

Recursive function : A function if calls itself
one loop by calling one time 
imp : there must a condition to stop calling
otherwise endless loop >> stack overlflow



*******************************************************************************/
#include <stdio.h>

int calFact(int num)
{
    int fact;
    
    if (num == 0)
        return 1;
    else
        fact= num * calFact(num-1);
  
    
    return fact;
}

int main()
{
    int ans , Num;
    
    printf("Enter the Number: ");
    scanf("%d",&Num);
    
    ans=calFact(Num);
    
    printf("%d",ans);

    return 0;
}
