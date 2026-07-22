# Chapter - 11 Dictionaries

# Q(a): Read a string and create a dictionary containing
# frequency of each character. Also print the occurrences.

s = input("Enter a string: ")

d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)

print("Histogram:")

for key in d:
    print(key, "*" * d[key])

print()

# Q(b): Create a dictionary containing names of students
# and marks in three subjects. Replace marks with total
# and average. Report the topper.

students = {
    "Ram": [80, 70, 90],
    "Shyam": [85, 90, 88],
    "Ajay": [75, 80, 82]
}

topper = ""
highest = 0

for name in students:
    total = sum(students[name])
    avg = total / 3
    students[name] = [total, avg]

    if total > highest:
        highest = total
        topper = name

print(students)
print("Topper:", topper)

print()

# Q(c): Perform operations on the given portfolio dictionary.

portfolio = {
    "accounts": ["SBI", "IOB"],
    "shares": ["HDFC", "ICICI", "TM", "TCS"],
    "ornaments": ["10 gm gold", "1 kg silver"]
}

portfolio["MF"] = ["Reliance", "ABSL"]

portfolio["accounts"] = ["Axis", "BOB"]

portfolio["shares"].sort()

del portfolio["ornaments"]

print(portfolio)

print()

# Q(c): Perform operations on the given portfolio dictionary.

portfolio = { "accounts": ["SBI", "IOB"],
              "shares": ["HDFC", "ICICI", "TM", "TCS"],
              "ornaments": ["10 gm gold", "1 kg silver"]}

portfolio["MF"] = ["Reliance", "ABSL"]

portfolio["accounts"] = ["Axis", "BOB"]

portfolio["shares"].sort()

del portfolio["ornaments"]

print(portfolio)

print()

# Q(d): Create two dictionaries containing grocery items
# and quantity purchased. Compute the total bill.

price = {
    "Rice": 50,
    "Sugar": 40,
    "Milk": 30
}

qty = {
    "Rice": 2,
    "Sugar": 3,
    "Milk": 5
}

bill = 0

for item in price:
    bill += price[item] * qty[item]

print("Total Bill =", bill)

print()

# Q(f): Create a dictionary of 10 usernames and passwords.
# Receive the username and password from the keyboard
# and search for them in the dictionary.

users = {}

for i in range(10):
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = password

u = input("Enter username to search: ")
p = input("Enter password: ")

if u in users and users[u] == p:
    print("Login Successful")
else:
    print("Invalid Username or Password")

print()

# Q(g): Perform the given operations on the marks dictionary.

marks = {
    "Subu": {"Maths": 88, "Eng": 60, "SSt": 95},
    "Amol": {"Maths": 78, "Eng": 68, "SSt": 89},
    "Raka": {"Maths": 56, "Eng": 66, "SSt": 77}
}

print("Amol's English Marks =", marks["Amol"]["Eng"])

marks["Raka"]["Maths"] = 77

print()

print("Sorted Dictionary")

for name in sorted(marks):
    print(name, marks[name])

print()

# Q(h): Store interface, IP address and status in a dictionary.
# Perform the required operations.

network = {
    "eth0": ["1.1.1.1", "up"],
    "eth1": ["2.2.2.2", "up"],
    "wlan0": ["3.3.3.3", "down"],
    "wlan1": ["4.4.4.4", "up"]
}

name = input("Enter interface: ")

if name in network:
    print("Status =", network[name][1])

print()

print("Interfaces which are up")

for key in network:
    if network[key][1] == "up":
        print(key, network[key][0])

print()

print("Total Interfaces =", len(network))

network["eth2"] = ["5.5.5.5", "up"]
network["wlan2"] = ["6.6.6.6", "down"]

print()

print(network)

print()

# Q(i): Print the dictionary from last pair to first pair.
# Delete every pair after printing so that the dictionary
# becomes empty.

