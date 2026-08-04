# Chapter - 15 Functional Programming

# Q(a): Suppose a dictionary contains type of pet (cat, dog, etc.),
# name of pet and age of pet. Write a program that obtains the
# sum of all dog's ages.

pets = [
    {"type": "dog", "name": "Tommy", "age": 5},
    {"type": "cat", "name": "Kitty", "age": 2},
    {"type": "dog", "name": "Bruno", "age": 7},
    {"type": "dog", "name": "Rocky", "age": 4}
]

dog_ages = map(lambda x: x["age"],
               filter(lambda x: x["type"] == "dog", pets))

print("Sum of dog's ages =", sum(dog_ages))

print()

# Q(b): Consider the following list:
# lst = [1.25, 3.22, 4.68, 10.95, 32.55, 12.54]
# The numbers in the list represent radii of circles.
# Write a program to obtain a list of areas of these circles
# rounded off to two decimal places.

import math

lst = [1.25, 3.22, 4.68, 10.95, 32.55, 12.54]

areas = list(
    map(lambda r: round(math.pi * r * r, 2), lst)
)

print(areas)

print()

# Q(c): Consider the following lists:
# nums = [10, 20, 30, 40, 50, 60, 70, 80]
# strs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# Write a program to obtain a list of tuples,
# where each tuple contains a number from one list
# and a string from another, in the same order.

nums = [10, 20, 30, 40, 50, 60, 70, 80]
strs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

result = list(map(lambda x, y: (x, y), nums, strs))

print(result)

print()

# Q(d): Suppose a dictionary contains names of students
# and marks obtained by them in an examination.
# Write a program to obtain a list of students
# who obtained more than 40 marks in the examination.

marks = {
    "Ram": 45,
    "Shyam": 32,
    "Krishan": 78,
    "Mohan": 40,
    "Lucy": 55
}

result = list(
    map(lambda x: x[0],
        filter(lambda x: x[1] > 40, marks.items()))
)

print(result)

print()

# Q(e): Consider the following list:
# lst = ['Malayalam', 'Drawing', 'madamImadam', '1234321']
# Write a program to print those strings which are palindromes.

lst = ['Malayalam', 'Drawing', 'madamImadam', '1234321']

result = list(
    filter(lambda x: x.lower() == x.lower()[::-1], lst)
)

print(result)

print()

# Q(f): A list contains names of employees.
# Write a program to filter out those names whose
# length is more than 8 characters.

employees = [
    "Ram",
    "Purushotam",
    "Amit",
    "Shubham",
    "Prachurya",
    "Vijay"
]

result = list(
    filter(lambda x: len(x) > 8, employees)
)

print(result)

print()

# Q(g): A dictionary contains following information about
# 5 employees:
# First name
# Last name
# Age
# Grade (Skilled, Semi-skilled, Highly-skilled)
# Write a program to obtain a list of employees
# (first name + last name) who are Highly-skilled.

employees = [
    {
        "First name": "Ram",
        "Last name": "Kumar",
        "Age": 25,
        "Grade": "Highly-skilled"
    },
    {
        "First name": "Kshitij",
        "Last name": "Bhardwaj",
        "Age": 21,
        "Grade": "Skilled"
    },
    {
        "First name": "Shreya",
        "Last name": "Verma",
        "Age": 28,
        "Grade": "Highly-skilled"
    }
]

result = list(
    map(
        lambda x: x["First name"] + " " + x["Last name"],
        filter(lambda x: x["Grade"] == "Highly-skilled", employees)
    )
)

print(result)

print()

# Q(h): Consider the following list:
# lst = ['Benevolent', 'Dictator', 'For', 'Life']
# Write a program to obtain a string
# 'Benevolent Dictator For Life'.

from functools import reduce

lst = ['Benevolent', 'Dictator', 'For', 'Life']

result = reduce(
    lambda x, y: x + " " + y,
    lst
)

print(result)

print()

# Q(i): Consider the following list:
# lst = ['Rahul', 'Priya', 'Chaya', 'Narendra', 'Prashant']
# Write a program to obtain a list in which all the names
# are converted to uppercase.

lst = ['Rahul', 'Priya', 'Chaya', 'Narendra', 'Prashant']

result = list(
    map(lambda x: x.upper(), lst)
)

print(result)

print()