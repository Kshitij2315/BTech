# WAF to find the factorial of n. (Using recursion)


def factorial(n):
    if n == 0:
        return 1
    #else:
    return n * factorial(n - 1)

#5 * factorial(5-1)  ---> 5 * 4
#4 * factorial(4-1)  ---> 4 * 3
#3 * factorial(3-1)  ---> 3 * 2
#2 * factorial(2-1)  ---> 2 * 1
#1 * factorial(1-1)  ---> 1 * 1

n = int(input("Enter a number to find its factorial: "))

fact = factorial(n)

print(fact)

