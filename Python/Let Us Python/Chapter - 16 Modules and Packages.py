# Chapter - 16 Modules and Packages

# Q(a): Suppose there are three modules m1.py, m2.py, m3.py,
# containing functions f1(), f2() and f3() respectively.
# How will you use those functions in your program?

import m1
import m2
import m3

m1.f1()
m2.f2()
m3.f3()

print()

# Q(b): Write a program containing functions fun1(), fun2(), fun3()
# and some statements. Add suitable code to the program such that
# you can use it as a module or a normal program.

def fun1():
    print("Function 1")

def fun2():
    print("Function 2")

def fun3():
    print("Function 3")


if __name__ == "__main__":
    print("Running as a program")
    fun1()
    fun2()
    fun3()

print()

# Q(c): Suppose a module mod.py contains functions f1(), f2() and f3().
# Write 4 forms of import statements to use these functions in your program.

# Method 1
import mod
mod.f1()

# Method 2
from mod import f1
f1()

# Method 3
from mod import f1, f2, f3
f2()

# Method 4
from mod import *
f3()

print()