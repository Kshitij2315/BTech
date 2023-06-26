/*******************************************************************

 Power Function 

 modular programming
 non returning but parameters

*******************************************************************/
#include <stdio.h>

void calPower(int m, int n)
{
   int a=1;
    
    int ct=1;
    
       while (ct<=m)
       {
           a = a * n;
           
           ct = ct + 1;
       }
       
    printf("%d ^ %d = %d",n ,m ,a);     
}

int main()
{
     int M=0;
    int N=0;
   
    
    printf("Enter Number: ");
    scanf("%d",&M);
    
    printf("To The Power: ");
    scanf("%d",&N);
    calPower(M, N);

    return 0;
}
