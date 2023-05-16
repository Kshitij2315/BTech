
/* WAP to print percentage of a student in Phy, Che, Maths */
#include <stdio.h>

int main()
{
    float physics=0.0;
    float chemistry=0.0;
    float maths=0.0;
    float total=0.0; 
    float percentage=0.0;

    printf("Enter Physics marks: ");
    scanf("%f", &physics);

    printf("Enter Chemistry marks: ");
    scanf("%f", &chemistry);

    printf("Enter Maths marks: ");
    scanf("%f", &maths);

    total = physics + chemistry + maths;
    percentage = (total / 300) * 100;

    printf("Your Percentage is: %f", percentage);
}
