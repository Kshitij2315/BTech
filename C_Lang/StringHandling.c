/******************************************************************************

//WAP Recurcive function to Print a String in Reverse Order

//WAP Recurcive function to Search a Character in a String. 0==not found, 1== found

//to do: making this function case insensitive

//WAF to Return Upper Case String

//WAF to Return a Copy of String

//WAF to Return Concatenation of Two Strings

*******************************************************************************/
#include <stdio.h>

char* ConcatenationStr(char *str1, char *str2)
{
    char result[100];
    int i,j,length;
    
    for(i=0; str1[i]!='\0'; i++)
    {
        result[i] = str1[i];
    }
    
    result[i] = 32;
    
    i = i + 1;
    
    /*for(j=0; str2[j]!='\0'; j++)
    {
        result[i + j] = str2[j];
    }*/
    
    for(j=0; str2[j]!='\0'; j++, i++)
    {
        result[i] = str2[j];
    }
    
    result[i + j] = '\0';
    
    return result;
}

char* copyStr(char* str)
{
    char copied[100];
    int i;
    
    for(i=0;*(str+i)!='\0';i++)
    {
        copied[i]=str[i];
    }
    
    copied[i]='\0';
    
    return copied;
}

char* conCase(char *str)
{
    int i;
    char result[100];
    
    for(i=0;str[i]!='\0';i++) //*(str+i)!='\0';
    {
        if(str[i]>=97 && str[i]<=122)//*(str+i)>=97 && *(str+i)<=122;
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
    char str[100], ch, *result, *copied, str1[100], str2[100];
    int ans;

    printf("Enter First String: ");
    gets(str1);
    
    printf("Enter Second String: ");
    gets(str2);

    result = ConcatenationStr(str1, str2); 
    
    printf("Concatenation: %s",result);

    //printf("\n\n Enter a string: ");
    //gets(str);
    
   /*** copied = copyStr(str);
    
    printf("Copied String: %s", copied);***/
    
    /**result=conCase(str);
    
    printf("%s",result)**/
    
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
     }*****/

   /* printRev(str);

    printf("Reversed string\n");*/
    
    return 0;
}
