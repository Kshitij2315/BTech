'''Basic DataTypes:
byte
int
float
string
bool
complex
BBI-FCS'''

'''Container DataTypes:
List
Tuple
Set
Dict'''

'''User-Defined DataTypes:
   Class'''

'''Keywords:
if, else, elif, for, while, in, is, break, return, import, def'''

import keyword
import math

print(keyword.kwlist)

n = 2 +3j
print(type(n))
print(n.real)
print(n.imag)

n = complex(2,3)
print(n)
print(n.real)
print(n.imag)

e = True
print(type(e))

e1 = int(bool(False))
print(e1)

b = b'\xa1\xe4\x56'   #10100001-(161) 11100100-(228) 01010110-(86)
print(b)

b2 = b'\101'          # Gives the symbol
print(b2)
print(type(b2), type(b))

b1 = 0o56             # Gives ASCII value (Decimal Value)
print(b1)
print(type(b1), type(b))

b3 = 0x56             # Gives ASCII value (Decimal Value)
print(b3)
print(type(b3), type(b))

a, b, c, d = 3, 4.5, 'Ram', 12+15j
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))

print(d/3)     #Performs Addition & Subtraction on REAL NUM only but Multiplication and Division on both REAL & IMAGINARY part

a = 23; b=45
print(a,b)

e = a^b        # ^ performs XOR Gate (0,0--->0; 1,1--->0)
print(e)

f = a**b       # Performs raise-to-power
print(f)

print(10/3)
print(10//3)       #Floor Division

print(math.floor(-3.99))
print(math.ceil(-3.01))
print(-10//3)
print(10//-3)
print(-10//-3)
print(3//10)
print("3//10:",3//-10)
print(10%3)       # a-(b*(a//b))
print(-10%3)      # -10-(3*(-10//3)) ===> -10-(3*(-4) ===> -10-(-12) ===> -10+12 ===> 2
print(3%10)       # 3-(10*(3//10))
print(3%-10)      # 3-(-10*(3//-10)) ===> 3-(-10*(-1)) ===> 3-(10) ===> -7

print(int(33.3))

print(chr(65))
print(ord('A'))
print("divmod(10,3):",divmod(10,3))

x1 = 10, 3
print(x1)
print(type(x1))

print(bin(9))

print(math.trunc(5.5))

print("All Math Func():",dir(__builtins__))     #Every built-in-func.
print("All Math Func():",dir(math))            #Every func. in Math module

name ='Ram'
print(id(name))   #2927859862096

name += ' Kumar'
print(name ,id(name))   #2460343147840

print(name.replace('yam','Ram'))
print(name)
print(id(name))

lst = [1,2,3,4,5]
print(id(lst))

lst[0] = 30
print(lst)
print(id(lst))

# string = ordered collection, immutable, iterable
# list = ordered collection, mutable, iterable
# tuple = ordered collection, immutable, iterable
# set = unordered collection, mutable, iterable
# dic = unordered collection, mutable, iterable

lst1 = [6,7,8]
lst = [1,2,3,*lst1,4,5]           # List within List    [1, 2, 3, [6, 7, 8], 4, 5]
#print(lst[3][1])

print("lst:",lst)

lst = ['Ram','Shyam','Krishan']
print(lst)

lst[0] += 'esh'
print(lst)

# Tuple within List possible
# List within Tuple possible

x = 5
y = 7.9

print(isinstance(x, float))