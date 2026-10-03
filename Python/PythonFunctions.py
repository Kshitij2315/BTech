# Function is a group of statements placed together to perform a specific task
# Purpose: i) To reuse
#          ii) To avoid repetition
# Process of writing func() is  Modular Approach
# For understandability purpose in real life we use 'Divide and Conquer'
# Func() are based on 'Divide and Conquer' analogy/mechanism
# Types of func(): i) Built-In
#                  ii) User-Defined
# func() naming conventions are same as variable naming conventions
# A func() can be redefined in Python but calling will be done for latest func()
# func() can be nested - We can declare one func() within another
# Nested func() is called 'inner func()' and it can access all outer func() variables but reverse isn't true
# Use of InnerFunc(): To create Decorators

def f1():
    print("This is f1")

# f1()

def f1():
    print("This is latest f1")
f1()
print(f1())


print()

# func() can be nested - We can declare one func() within another
# Nested func() is called 'inner func()' and it can access all outer func() variables but reverse isn't true

def f2():
    v = 30
    print('This is Outer func()')
    def f3():
        v = 2
        print('This is Inner func()')
        print("v:",v)
    f3()
    print('v',v)

f2()

print()

# Use of InnerFunc(): To create Decorators

def my_decorator(func):           # func ---> f4
    def wrapper():
        print("Before Calling:",func)
        func()                    # func() ---> f4()
        print("After Calling:",func)
        print()
    return wrapper

@my_decorator
def f4():
    print("This is f4")

@my_decorator
def f5():
    print("This is f5")

f4()
f5()

# No Parameter,No Return Type           # Returns None

def isprime1():
    print("No Parameter,No Return Type:")
    n = int(input("Enter a number: "))
    for i in range(2,n):
        if n % i == 0:
            print(n,"Is Not a Prime Number")
            break
    else:
        print(n,"is a Prime Number")
# isprime1()

print()

# No Parameter, Return Type

def isprime2():
    print("No Parameter,Return Type:")
    n = int(input("Enter a number: "))
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True

# ans = isprime2()
# if ans == True:
#     print("Is Prime Number")
# else:
#     print("Is Not Prime Number")
#
# print()

# With Parameter, No Return Type        # Returns None

def isprime3(n):
    print("With Parameter,No Return Type:")
    for i in range(2,n):
        if n % i == 0:
            print(n,"Is Not a Prime Number")
            break
    else:
        print(n,"is a Prime Number")

# n = int(input("Enter a number: "))
# isprime3(n)

print()

# With Parameter, Return Type

def isprime4(n):
    print("With Parameter,Return Type:")
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True

# n = int(input("Enter a number: "))
# ans = isprime4(n)
# if ans == True:
#     print("Is Prime Number")
# else:
#     print("Is Not Prime Number")
#
# print()

# 4 ways to manage Arguments in Python
#              i) Positional Arguments
#             ii) Keyword Arguments
#            iii) Variable length Positional Arguments - No Certainty of Positional Arguments
#             iv) Variable length Keyword Argument - No certainty of Keyword Arguments

# i) Positional Arguments

print("Positional Arguments:")

def myfun1(i,j,k):
    print(i+j,k.upper())

myfun1(1,2,'ram')

print()

# ii) Keyword Arguments

print("Keyword Arguments:")

def myfun2(i, j, k):
    print(i + j, k.upper())

myfun2(i = 1,j = 2, k = 'ram')
myfun2(i = 1, k = 'ram',j = 2)
myfun2(1, k = 'ram',j = 2)
myfun2(1, 2, k = 'ram')
# myfun2(1, k = 'ram', 2)       # Positional Arguments should be followed by Keyword Arguments
# myfun2(a = 1,j = 2, k = 'ram')  # Keyword should be same during passing an Argument

print()

# iii) Variable length Positional Arguments - No Certainty of Positional Arguments
# Zero or Many arguments can be passed
def myfun3(*args):
    print('Variable length Positional Arguments:')
    print(type(args))
    print(args)

    for arg in args:
        if isinstance(arg, str):
            print(arg.upper())
        else:
            print(arg)

myfun3()
myfun3(1,2,'ram')
myfun3(1,2)
myfun3(1,'ram',2)
# myfun3(1,'ram',j = 2)
# myfun3(args = (1,2,'ram'))

print()

def myfun4(i,j,*args):
    print("Combination of Positional and Variable length Positional Arguments:")
    print(type(args))
    print(args)

    for arg in args:
        if isinstance(arg, str):
            print(arg.upper())
        else:
            print(arg)
    print()

myfun4(1,2,4,5.6,'ram',2+1j)
myfun4(i = 1,j = 2)
myfun4(1,2)

print()

# iv) Variable length Keyword Argument - No certainty of Keyword Arguments
# Zero or Many arguments can be passed
def myfun5(**kwargs):
    print('Variable length Keyword Argument:')
    print(type(kwargs))
    print(kwargs)

    for k,v in kwargs.items():
        if isinstance(v, str):
            print(k,':',v.upper())
        else:
            print(k,':',v)
    print()

myfun5(i = 1, j = 'Ram', x = 5.5, y = 2+5j)
# myfun5(5,4,45)

# Combination of Positional, Keyword, Variable Length Positional and Keyword Argument
print('Combination of Positional, Keyword, Variable Length Positional and Keyword Argument:')
def myfun6(i,j,*args,**kwargs):
    print(i,j,args,kwargs)

# myfun6(10)
myfun6(10,20)
myfun6(10,j = 20)
# myfun6(10,j = 20, 5, 7)
myfun6(5.5,"Good",2+5j,a = 1, b = 'Ram')

print()

# Combination of Positional, Variable Length Positional, Keyword and Keyword Argument
print('Combination of Positional, Variable Length Positional, Keyword and Keyword Argument:')
def myfun7(i,*args,j,**kwargs):
    print(i,j,args,kwargs)

# myfun7(10)              # Not Possible
myfun7(10,j = 5)
myfun7(i =10, j = 3)
# myfun7(10, 7, 9)        # Not Possible

lst = [10,20,30,'Ram']
myfun7(*lst, j = 5)

d = {'1': 10,
     '2': 100,
     '3':200,
     '4': 300}
myfun7(7,j = 15, **d)
myfun7(7,*lst,j = 15, **d)