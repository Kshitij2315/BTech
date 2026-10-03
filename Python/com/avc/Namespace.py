# Namespace ---> func(), class, variable names are called as Identifiers.
# Python keeps these Identifier in a table (called symbol table).
# Table contains:
#            Identifier Name
#            Type
#            Scope ---> local/global
#            Memory Location(Address)
# Table is in the form of Dictionary.
# Namespace is a Space where all the Identifiers are present in a Tabular Form (Dictionary) implementation.
# Local variable shadows Global if names are same.

x = 500
def myfunc():
    a = 100
    x = 200          # Local variable shadows Global if names are same.
    print('a and x are local variable:',a,x)
    print('x is a global variable:', x)
def myfunc2():
    print('x can be used here too:',x)
    # print('y:',y)
    def myfunc3():
        z = 5
        print('x can be used in nested func() too:',x)
        # print('y can also be used in nested func():',y)
        print('locals():',locals())
        print('globals():',globals())
    myfunc3()
myfunc()
# myfunc2(6)
myfunc2()

print()

# Uses of locals() and globals()
a = 10
b = 20
c = 30
lst = ['a','b','c']
for i in lst:
    print(globals()[i])

print()

print('globals() in func():')
lst = ['myfunc','myfunc2']
for i in lst:
    globals()[i]()

# Converting local to global
print('Converting local to global:')

# LEGB ----> scoping
# L--->Local
# E--->Enclosed/Parameters
# G--->Global
# B--->Built-in

x = 500
def myfunc():
    a = 100
    x = 200
    print(globals()['x'])
    print(locals()['x'])
myfunc()