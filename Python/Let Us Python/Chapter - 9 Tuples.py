# Chapter - 9 Tuples  [C]

# Q(c): Suppose data regarding a date is stored as a tuple
# in the form (dd, mm, yy). Write a program to create two
# date tuples and find the number of days between them.

from datetime import date

d1 = (10, 2, 2024)
d2 = (25, 3, 2024)

date1 = date(d1[2], d1[1], d1[0])
date2 = date(d2[2], d2[1], d2[0])

days = abs((date2 - date1).days)

print("Days =", days)

print()

# Q(c): Suppose a date is represented as a tuple (d, m, y).
# Write a program to create two date tuples and find
# the number of days between the two dates.

from datetime import date

d1 = (10, 2, 2024)
d2 = (25, 3, 2024)

date1 = date(d1[2], d1[1], d1[0])
date2 = date(d2[2], d2[1], d2[0])

days = abs((date2 - date1).days)

print("Days =", days)

print()

# Q(d): Create a list of tuples, each tuple containing
# item name and price. Sort it in increasing order of price.

# Q(d): Create a list of tuples, each tuple containing
# item name and price. Sort it in increasing order of price.

items = [
    ("Pen", 20),
    ("Book", 150),
    ("Scale", 30),
    ("Pencil", 10)
]

n = len(items)

for i in range(n):
    for j in range(n - i - 1):
        if items[j][1] > items[j + 1][1]:
            temp = items[j]
            items[j] = items[j + 1]
            items[j + 1] = temp

print(items)

print()

# Q(e): Store share information in a list of tuples.
# Determine total cost, total profit/loss and
# percentage profit/loss.

shares = [
    ("ABC", 100, 50, 120),
    ("XYZ", 200, 20, 180),
    ("PQR", 150, 30, 170)
]

total_cost = 0
total_sell = 0

for name, cp, qty, sp in shares:
    total_cost += cp * qty
    total_sell += sp * qty

profit = total_sell - total_cost
percent = (profit / total_cost) * 100

print("Total Cost =", total_cost)
print("Profit/Loss =", profit)
print("Percentage =", percent)

print()

# Q(f): Write a program to remove empty tuples
# from a list of tuples.

lst = [(), (10, 20), (), (30, 40), (), (50,)]

new = []

for i in lst:
    if len(i) != 0:
        new.append(i)

print(new)

print()

# Q(g): Create three lists: names, roll numbers and marks.
# Generate a list of tuples from them.
# From this list generate three tuples containing
# names, roll numbers and marks.

names = ["Ram", "Shyam", "Ajay"]
roll = [101, 102, 103]
marks = [85, 90, 88]

students = list(zip(names, roll, marks))

print("List of Tuples:", students)

name_tuple = ()
roll_tuple = ()
marks_tuple = ()

for n, r, m in students:
    name_tuple += (n,)
    roll_tuple += (r,)
    marks_tuple += (m,)

print("Names:", name_tuple)
print("Roll Numbers:", roll_tuple)
print("Marks:", marks_tuple)