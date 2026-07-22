# Charter - 12 Comprehension

# Q(a): Generate coordinates from (1,1) to (5,5)

points = [(x, y) for x in range(1, 6) for y in range(1, 6)]

print(points)

print()

# Q(b): Multiply each element by 10

lst = [1, 2, 3, 4, 5]

new_lst = [i * 10 for i in lst]

print(new_lst)

print()

# Q(c): First 20 Fibonacci numbers

fib = [0, 1]

for i in range(18):
    fib.append(fib[-1] + fib[-2])

ans = [i for i in fib]

print(ans)

print()

# Q(d): First 20 odd and even numbers

odd = [i for i in range(1, 40, 2)]

even = [i for i in range(2, 41, 2)]

print("Odd =", odd)

print("Even =", even)

print()

# Q(e): Separate positive and negative numbers

lst = [-5, 4, -2, 8, -7, 10, 3, -1]

positive = [i for i in lst if i > 0]

negative = [i for i in lst if i < 0]

print("Positive =", positive)

print("Negative =", negative)

print()

# Q(f): Convert strings to uppercase

lst = ["apple", "banana", "mango", "orange", "grapes"]

upper = [i.upper() for i in lst]

print(upper)

print()

# Q(g): Fahrenheit to Celsius

fahrenheit = [32, 68, 86, 104, 122]

celsius = [(f - 32) * 5 / 9 for f in fahrenheit]

print(celsius)

print()

# Q(h): 4x5 matrix of random multiples of 4

import random

matrix = [[random.randrange(40, 161, 4) for j in range(5)] for i in range(4)]

for row in matrix:
    print(row)

print()

