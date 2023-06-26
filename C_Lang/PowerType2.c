/*******************************************************************

 Power Function 

 Modular programming
 Returning , No Parameters

*******************************************************************/
#include <stdio.h>

int calPower()
{
   int n=0;
    int m=0;
    int a=1;
    
    printf("Enter Number: ");
    scanf("%d",&n);
    
    printf("To The Power: ");
    scanf("%d",&m);
    
    int ct=1;
    
       while (ct<=m)
       {
           a = a * n;
           
           ct = ct + 1;
       }
       
    printf("%d ^ %d = ",n ,m);   
    
    return a;
}

int main()
{
    int ans;
    ans=calPower();
    
    printf("%d",ans);

    return 0;
}