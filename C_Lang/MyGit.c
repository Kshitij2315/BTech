/******************************************************************************

MyGit.c

Command Line Arguments 
c = count
v = values

*******************************************************************************/
#include <stdio.h>


int main(int argc, char *argv[])
{
    int i;
    
   printf("Total arguments count : "+argc);
   
   for(i=0; i<argc; i++){
      printf("%d = %sn", i, *argv[i]);
   }
   
    return 0;
}

