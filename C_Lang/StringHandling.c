/******************************************************************************

//WAP Recurcive function to Print a String in Reverse Order

//WAP Recurcive function to Search a Character in a String. 0==not found, 1== found

//to do: making this function case insensitive

//WAF to Return Upper Case String

*******************************************************************************/
#include <stdio.h>

char* conCase(char *str)
{
    int i;
    char result[100];
    
    for(i=0;str[i]!='\0';i++)
    {
        if(*str[i]>=97 && *str[i]<=122)
        {
            result[i] = str[i] - 32;
        }
        else
        {
            result[i] = str[i];
        }
    }
    
    result[i]='\0';
    
    return result;
}

int printRev(char* str) 
{
    if (*str == '\0') 
    {
        return 1 ;  
    } 
    else 
    {
        printRev(str + 1);
        
        printf("\n\n");
        printf(" %c", *str);
    }
}


int searchChar(char* str, char ch) 
{
    if (*str == ch)
    {
        return 1;  
    }
    else if (*str == '\0')
    {
        return 0;  
    }
    else
    {
        return searchChar(str + 1, ch);  
    }
}


int main() 
{
    char str[100], ch, result;
    int ans;

    printf("\n\n Enter a string: ");
    gets(str);
    
    result=conCase(str);
    
    printf("%s",result);
    
    /*****printf(" Enter a character to search: ");
    scanf(" %c", &ch);

    ans = searchChar(str, ch);
    
     if (ans == 1)
     {
        printf("\n\nCharacter '%c' found in the string.\n", ch);
     }
     else 
     {
         printf("\n\nCharacter '%c' not found in the string.\n", ch);
     }*********************/

   /* printRev(str);

    printf("Reversed string\n");*/
    
    return 0;
}
