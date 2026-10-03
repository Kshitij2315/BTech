# Recursion ---> Function calling itself
# By default 10^3 (1000) Executions

import sys
sys.setrecursionlimit(10000)

def hello(i):
    print(i,"Hello World")
    i+=1
    if i == 10000:         # Restriction: Atleast 1 if condition after which it stops calling
        return
    hello(i)
hello(1)

print()

print('N Natural Number')
def n_num(n,i):
    print(i)
    if i == n:
        return
    # i+=1
    n_num(n,i+1)

n = 10 # int(input("Number to be printed: "))
n_num(n,1)

print()

print('Reverse of N Natural Number')
def reverse_n(n):
    print(n)
    if n == 1:
        return
    reverse_n(n-1)         # Recursive Case - Place where you call for recursion

n = 10 # int(input("Number to be printed: "))
reverse_n(n)

print()

# Head Recursion or Tail Recursion

print('Tail-Recursion:')
def number(n):
    if n == 0:
        return
    else:
        print(n)
        number(n-1)

number(5)

print()

print('Head-Recursion:')
def number2(n):
    if n == 0:     # 5
        return
    else:
        number2(n-1)
        print(n)

number2(5)

print()

def fact(n):
    if n == 0:   # 5
        return 1
    else:
        a = n * fact(n-1)  # 5 * 24
        return a           # 120

def fact(n):
    if n == 0:   # 4
        return 1
    else:
        a = n * fact(n-1)   # 4 * 6
        return a            # 24

def fact(n):
    if n == 0:   # 3
        return 1
    else:
        a = n * fact(n-1)    # 3 * 2
        return a             # 6

def fact(n):
    if n == 0:   # 2
        return 1
    else:
        a = n * fact(n-1)    # 2 * 1
        return a             # 2

def fact(n):
    if n == 0:   # 1
        return 1
    else:
        a = n * fact(n-1)    # 1 * 1
        return a             # 1

def fact(n):
    if n == 0:   # 0
        return 1
    else:
        a = n * fact(n-1)
        return a

n = 5
ans = fact(n)     # 120
print('Factorial of',n,'is',ans)

print()

# Iterative(for/while) vs Recursive Functions

n = 263  #int(input("Enter a number: "))

n = str(n)
add = 0

for i in n:
    add += int(i)

print('Sum of digits:', add)

def digi_sum(n,i):
    print(n,i)
    if i == len(n):
        return 0
    else:
        a = int(n[i]) + digi_sum(n,i+1)
        return a
n =263
ans = digi_sum(str(n),0)
print('Sum of digits:', ans)

add = 0
while n > 0:
    add += n%10
    n //= 10
print('Sum of digits:', add)