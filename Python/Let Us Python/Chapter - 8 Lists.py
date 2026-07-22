# Chapter - 8   Lists   [C]

# Q(a): Create a list of 5 odd integers. Replace the third element
# with a list of 4 even integers. Flatten, sort and print the list.

lst = [1, 3, 5, 7, 9]

lst[2] = [2, 4, 6, 8]

flat = []

for item in lst:
    if isinstance(item, list):
        flat.extend(item)
    else:
        flat.append(item)

flat.sort()

print(flat)

print()

# Q(b): Suppose a list contains 20 integers generated randomly.
# Receive a number from the keyboard and report the position
# of all occurrences of this number in the list.

import random

lst = []

for i in range(20):
    lst.append(random.randint(1, 20))

print("List =", lst)

num = int(input("Enter number to search: "))

found = False

for i in range(len(lst)):
    if lst[i] == num:
        print("Found at position", i)
        found = True

if found == False:
    print("Number not found")

print()

# Q(c): Remove all duplicate elements from a list.

lst = [10, 20, 10, 30, 20, 40, 50, 40]

new = []

for i in lst:
    if i not in new:
        new.append(i)

print("Original List:", lst)
print("Without Duplicates:", new)

print()

# Q(d): Separate positive and negative numbers into two lists.

lst = [10, -5, 20, -15, 30, -8, 0, 12]

positive = []
negative = []

for i in lst:
    if i >= 0:
        positive.append(i)
    else:
        negative.append(i)

print("Positive:", positive)
print("Negative:", negative)

print()

# Q(e): Convert all strings in a list to uppercase.

lst = ["python", "java", "c", "html", "css"]

for i in range(len(lst)):
    lst[i] = lst[i].upper()

print(lst)

print()

# Q(f): Convert temperatures from Fahrenheit to Celsius.

fahrenheit = [32, 68, 98.6, 104, 212]

celsius = []

for f in fahrenheit:
    c = (f - 32) * 5 / 9
    celsius.append(c)

print("Fahrenheit:", fahrenheit)
print("Celsius:", celsius)

print()

# Q(g): Find the median without disturbing the original list.

lst = [30, 10, 50, 20, 40]

copy = lst.copy()
copy.sort()

n = len(copy)

if n % 2 == 1:
    median = copy[n // 2]
else:
    median = (copy[n // 2 - 1] + copy[n // 2]) / 2

print("Original List:", lst)
print("Median:", median)

print()

# Q(h): Create a list containing only negative integers.

lst = [10, -5, 30, -12, 45, -8, -100, 25]

negative = []

for i in lst:
    if i < 0:
        negative.append(i)

print("Negative Numbers:", negative)

print()

# Q(i): Suppose a list contains several words.
# Create another list that contains the first character of each word.

words = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

first = []

for word in words:
    first.append(word[0])

print("Original List:", words)
print("New List:", first)

print()

# Q(j): A list contains 10 integers.
# Write a program to eliminate all duplicates from the list.

lst = []

for i in range(10):
    num = int(input("Enter number: "))
    lst.append(num)

new = []

for i in lst:
    if i not in new:
        new.append(i)

print("Original List:", lst)
print("After Removing Duplicates:", new)

print()

# Q(k): Write a program to find the mean,
# median and mode of a list of 10 numbers.

from statistics import mean, median, mode

lst = []

for i in range(10):
    num = int(input("Enter number: "))
    lst.append(num)

print("Mean =", mean(lst))
print("Median =", median(lst))

try:
    print("Mode =", mode(lst))
except:
    print("No unique mode found.")