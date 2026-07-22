# Chapter-10   Sets    [B]

# Q(a): A set contains names beginning with A or B.
# Write a program to separate the names into two sets,
# one containing names beginning with A and another
# containing names beginning with B.

names = {"Amit", "Ajay", "Anil", "Bharat", "Bobby", "Bhavesh"}

A = set()
B = set()

for name in names:
    if name[0] == "A":
        A.add(name)
    elif name[0] == "B":
        B.add(name)

print("Names beginning with A:", A)
print("Names beginning with B:", B)

print()

# Q(b): Create an empty set. Write a program that adds
# five new names to this set, modifies one existing name
# and deletes two existing names.

names = set()

for i in range(5):
    name = input("Enter name: ")
    names.add(name)

print("Original Set:", names)

old = input("Enter name to modify: ")
new = input("Enter new name: ")

if old in names:
    names.remove(old)
    names.add(new)

for i in range(2):
    name = input("Enter name to delete: ")
    if name in names:
        names.remove(name)

print("Updated Set:", names)

print()

# Q(d): Create a set containing 10 randomly generated
# numbers in the range 15 to 45. Count how many numbers
# are less than 30. Delete all numbers greater than 35.

import random

nums = set()

while len(nums) < 10:
    nums.add(random.randint(15, 45))

print("Original Set:", nums)

count = 0

for i in nums:
    if i < 30:
        count += 1

print("Numbers less than 30:", count)

temp = set()

for i in nums:
    if i > 35:
        temp.add(i)

for i in temp:
    nums.remove(i)

print("Updated Set:", nums)

print()