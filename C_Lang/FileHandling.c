/******************************************************************************

File Handling in C

*******************************************************************************/
#include <stdio.h>

int main()
{
    int i;
    char buff[255];
    FILE *fp;
    
    fp = fopen("/tmp/test.txt", "w+");
    
    fprintf(fp, "This is testing for fprintf...\n");
    
    fputs("This is testing for fputs...\n", fp);
    
    fclose(fp);

    fp = fopen("/tmp/test.txt", "r");
    
   /* fscanf(fp, "%s", buff);
    
    printf("1.1 : %s\n", buff );
    
    fgets(buff, 255, (FILE*)fp);

    printf("1.2 : %s\n", buff );
    
    fgets(buff, 255, (FILE*)fp);
    
    printf("2 : %s\n", buff ); */
    
    for(i=1 ; !(feof(fp)); i++)
    {
        fgets(buff, 255, (FILE*)fp);

        printf("%d : %s\n", i, buff );
    }
    
    fclose(fp); 
    
    return 0;
}