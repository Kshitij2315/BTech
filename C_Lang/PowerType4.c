/*******************************************************************

 Power Function 

 modular programming
 Returning and Parameters

*******************************************************************/
#include <stdio.h>

int calPower(int m, int n)
{
   int a=1;
    
    int ct=1;
    
       while (ct<=m)
       {
           a = a * n;
           
           ct = ct + 1;
       }
       
    printf("%d ^ %d = ",m ,n); 
    
    return a;
}

int main()
{
    int M=0;
    int N=0;
    int ans;
    
    printf("Enter Number: ");
    scanf("%d",&M);
    
    printf("To The Power: ");
    scanf("%d",&N);
    ans=calPower(M, N);
    
    printf("%d",ans);

    return 0;
}
