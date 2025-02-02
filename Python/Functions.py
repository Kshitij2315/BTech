''' In C language
int/void fun_name(parameters1, parameter2....)
{
   ....
}'''

''' In Python
def fun_name(parameteres1, parameter2...):
    statements...
    
    return var_name
    
statement(out of func.)'''

def factorial(n = 5):                       # n = 5 default parameter
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

num = int(input("Enter any num: "))

ans = factorial(num)

#ans = factorial()

print("Factorial: ",ans)