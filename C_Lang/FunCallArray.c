/******************************************************************************

Callings Functions with array 

FuncCallArray.c

*******************************************************************************/
#include <stdio.h>
//WAF to calculate sum of array elements

int anotherSumFun(int ptr[], int n){
    
    int i=0, sum=0;
    
    for(i=0; i<n; i++){
        sum=sum + *(ptr+i); //sum=sum+ptr[i]; // both works
    }
    
     return sum;
    
}

void calSum(int *ptr, int n){
    
    int i=0, sum=0;
    
    for(i=0; i<n; i++){
        sum=sum + *(ptr+i);
    }
    
     printf("sum= %d",sum);  
    }//end of calFun

int main()
{
    int arr[100],n,i,ans;
    
    printf("How many elements you want ");
    scanf("%d",&n);

    for(i=0; i<n; i++){
        printf(" Enter element ");
        scanf ("%d",&arr[i]);
    }
    // array name itself is the base address of array. 
    // arrays always call by refernece
    calSum(arr,n); 
    ans=anotherSumFun(arr,n);
    
    printf("n ans: %d",ans);
    return 0;
}

