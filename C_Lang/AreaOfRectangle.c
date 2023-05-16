/******************************************************************************

WAP to print area of rectangle

*******************************************************************************/
#include <stdio.h>

int main()
{
    float len=0.0;
    float breadth=0.0;
    float area=0.0;
    
    printf("Enter lenght of rectangle");
    scanf("%f",&len);
    
    printf("Enter breadth of rectangle");
    scanf("%f",&breadth);
    
    area=len*breadth;
    
    printf("Area of rectangle:%f",area);

    return 0;
}

