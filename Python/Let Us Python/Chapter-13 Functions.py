# Chapter - 12 Functions

# Q(a): Write a program that defines a function count_lower_upper() that
# accepts a string and calculates the number of uppercase and lowercase
# alphabets in it. It should return these values as a dictionary.
# Call this function for some sample strings.

def count_lower_upper(s):
    d = {"Uppercase": 0, "Lowercase": 0}

    for ch in s:
        if ch.isupper():
            d["Uppercase"] += 1
        elif ch.islower():
            d["Lowercase"] += 1

    return d

print(count_lower_upper("Hello World"))
print(count_lower_upper("Python Programming"))
print(count_lower_upper("ABCdef"))

print()

# Q(b): Write a program that defines a function compute() that calculates
# the value of n + nn + nnn + nnnn, where n is a digit received by the
# function. Test the function for digits 4 and 7.

def compute(n):
    ans = n + n * 11 + n * 111 + n * 1111
    return ans

print("For 4 =", compute(4))
print("For 7 =", compute(7))

print()

# Q(c): Write a program that defines a function create_array() to create
# and return a 3D array whose dimensions are passed to the function.
# Also initialize each element of this array to a value passed to the
# function.

def create_array(x, y, z, value):
    arr = [[[value for k in range(z)] for j in range(y)] for i in range(x)]
    return arr

a = create_array(2, 3, 4, 5)

print(a)

print()

# Q(d): Write a program that defines a function create_list() to create
# and return a list which is an intersection of two lists passed to it.

def create_list(lst1, lst2):
    result = []

    for i in lst1:
        if i in lst2 and i not in result:
            result.append(i)

    return result

a = [10, 20, 30, 40, 50]
b = [30, 40, 50, 60, 70]

print(create_list(a, b))

print()

# Q(e): Write a program that defines a function sanitize_list() to remove
# all duplicate entries from the list that it receives.

def sanitize_list(lst):
    new_list = []

    for i in lst:
        if i not in new_list:
            new_list.append(i)

    return new_list

lst = [10, 20, 30, 20, 40, 10, 50, 30]

print(sanitize_list(lst))

print()

