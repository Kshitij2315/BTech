# Chapter - 14 Recursion

# Q(a): Following program calculates sum of first 5 natural numbers
# using tail recursion and head recursion.

def head_sum(n):
    if n == 0:
        return 0
    return n + head_sum(n - 1)

def tail_sum(n, total):
    if n == 0:
        return total
    return tail_sum(n - 1, total + n)

print("Head Recursion =", head_sum(5))
print("Tail Recursion =", tail_sum(5, 0))

print()

# Q(b): There are three pegs labeled A, B and C. Four disks are placed on
# peg A. The bottom-most disk is largest, and disks go on decreasing in size
# with the topmost disk being smallest. The objective of the game is to move
# the disks from peg A to peg C, using peg B as an auxiliary peg.
# Write a program to print out the sequence in which the disks should be moved.

def tower(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower(n - 1, auxiliary, source, destination)

tower(4, "A", "B", "C")

print()

# Q(c): A string is entered through the keyboard.
# Write a recursive function that counts the number of vowels in this string.

def count_vowels(s):
    if s == "":
        return 0

    if s[0].lower() in "aeiou":
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

text = input("Enter a string: ")

print("Number of vowels =", count_vowels(text))

print()

# Q(d): A string is entered through the keyboard.
# Write a recursive function that removes any tabs present in this string.

def remove_tabs(s):
    if s == "":
        return ""

    if s[0] == "\t":
        return remove_tabs(s[1:])
    else:
        return s[0] + remove_tabs(s[1:])

text = input("Enter a string: ")

print("After removing tabs:")
print(remove_tabs(text))

print()

# Q(e): A string is entered through the keyboard.
# Write a recursive function that checks whether the string is a palindrome or not.

def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])

text = input("Enter a string: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")

print()

# Q(f): Two numbers are received through the keyboard into variables
# a and b. Write a recursive function that calculates the value of a^b.

def power(a, b):
    if b == 0:
        return 1

    return a * power(a, b - 1)

a = int(input("Enter base: "))
b = int(input("Enter exponent: "))

print("Answer =", power(a, b))

print()

# Q(g): Write a recursive function that reverses the list of numbers that
# it receives.

def reverse_list(lst):
    if len(lst) <= 1:
        return lst

    return [lst[-1]] + reverse_list(lst[:-1])

numbers = [10, 20, 30, 40, 50]

print("Original List :", numbers)
print("Reversed List :", reverse_list(numbers))

print()

# Q(h): A list contains some negative and some positive numbers.
# Write a recursive function that sanitizes the list by replacing
# all negative numbers with 0.

def sanitize(lst, index):
    if index == len(lst):
        return

    if lst[index] < 0:
        lst[index] = 0

    sanitize(lst, index + 1)

numbers = [10, -5, 20, -15, 30, -25]

sanitize(numbers, 0)

print(numbers)

print()

# Q(i): Write a recursive function to obtain average of all numbers
# present in a given list.

def total(lst):
    if len(lst) == 0:
        return 0

    return lst[0] + total(lst[1:])

numbers = [10, 20, 30, 40, 50]

avg = total(numbers) / len(numbers)

print("Average =", avg)

print()

# Q(j): Write a recursive function to obtain length of a given string.

def length(s):
    if s == "":
        return 0

    return 1 + length(s[1:])

text = input("Enter a string: ")

print("Length =", length(text))

print()

# Q(k): Write a recursive function that receives a number as input and
# returns the square of the number. Use the mathematical identity
# (n - 1)^2 = n^2 - 2n + 1.

def square(n):
    if n == 0:
        return 0

    return square(n - 1) + 2 * n - 1

num = int(input("Enter a number: "))

print("Square =", square(num))

print()