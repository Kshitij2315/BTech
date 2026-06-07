import copy
from re import search

num = [10, 20, 30]
num1 = [10]*5
names = ["Ram","Shayam","Krishna","Mohan"]
mix = [ 10, 25.567, "Ram"]
empty = []

print(mix)
print(names)
print(num)
print(num1)
print()

for i in range(len(names)):
    print(names[i])

i = 0

print()

while i < len(names):
    print(names[i])
    i+=1

names1 = ["Ram","Shayam","Krishna","Mohan"]

print()
print("Through Enumerate:")

for i, nam in enumerate(names1):
    print(nam,"  ", i)

print()
print(names1[1:])
print()
print(names1[1:2])
print()

s=[1,2,3,4,5]
y = [10, 20, 30, 40, 50]
z = s + y
num2 = [num, num1]
num3 = num + num1
num4 = [num] + [num2]

print("num3: ",num3)
print("num4: ",num4)
print()
print("num2: ",num2)
print()
print("z: ",z)
print()

strng = "Kshitij"
lst = list(strng)

print("lst: ", lst)
print()

x = s                        #Alias

print("x:", x)
print()

x1 = copy.deepcopy(s)        #Clone

print("x1: ",x1)
print()

s[2] = 7

print("s: ",s," x1: ",x1," x: ",x)
print()

#s =[]

for iii in range(len(s)):
    if s[iii] == 7:
        print("7 found in s on index ",iii)
        break

#if s[iii] != 17:
else:
    print("7 not found in s and iii: ",iii)

if 7 in s:
    print("7 is found in s ")
else:
    print("7 not found in s ")

print()

if x is s:
    print("x is pointing/alias/shallow_copy to list s ")
else:
    print("x is not pointing/alias/shallow_copy to list s ")

print()

if x1 is s:
    print("x1 is pointing/alias/shallow_copy to list s ")
else:
    print("x1 is not pointing/alias/shallow_copy to list s ")

print()

number1 = 10
number2 = 10

print("number1 is number2: ",number1 is number2)
print()

strng1 = "Ram"
strng2 = "Ram"

print("strng1 is strng2: ",strng1 is strng2)
print()

aa = [1,2,3,4,5]
bb = [1,2,3,4,5]

print("aa < bb: ",aa < bb)
print()
print("aa is bb: ",aa is bb)
print()

emppty = []
print("not empty: ",bool(None))      #Emptiness
print()

