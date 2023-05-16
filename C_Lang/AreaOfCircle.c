/******************************************************************************

WAP to print Area of a Circle

******************************************************************************/
#include <stdio.h>

int main()
{
    float radius=0.0;
    float area=0.0;
    float PIE=3.14;

    printf("Enter radius of circle: ");
    scanf("%f", &radius);

    area = PIE * radius * radius;

    
    printf("Area of circle:%f",area);
    
    return 0;
}