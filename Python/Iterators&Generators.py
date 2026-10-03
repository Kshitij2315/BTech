# Iterator ---> means repeatedly.
# Iterable ---> those objects which are capable of returning its elements one by one (one at a time).
# Iterable have only one method:
#                   1. __iter__()
# We Iterate the Iterable Object using Iterator.
# Iterator have 2 methods:
#                   1. __iter__() / iter()
#                   2. __next__() / next() ---> generates StopIteration exception, when last element reached
# Iterators are Implemented in:
#                       1. for loops,
#                       2. comprehensions,
#                       3. generators
#

lst = [ 1, 2, 3, 4, 5 ]

print('lst:',lst)

iterator = lst.__iter__()

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

iterator = iter(reversed(lst))
print(next(iterator))

# List is Iterable: Proof
print(hasattr(lst, '__iter__'))
print(hasattr(lst, 'iter'))              # False because it is an inbuilt func()
print(hasattr(lst, '__next__'))
print(hasattr(lst, 'next'))              # False because iterable has no '__next__' method

print(dir(lst))

for i in range(len(lst)):
    print(lst[i])

for i in lst:
    print(i)

# Iterator Methods: Proof
print(hasattr(iterator, '__iter__'))
print(hasattr(iterator, '__next__'))

lst2 = [10, 20, 30]

zipped = zip(lst, lst2)


for i in zip(lst):
    print(i[0])

print()

for i in zip(lst, lst2):
    print(i[0], i[1])  # i = (1,10), i = (2,20), i = (3,30)

print()

for i in zip(lst, lst2):
    print(*i)

print()

for i,j in zip(lst, lst2):
    print(i,j)

# User-Defined Iterators

lst = [30, 40, 50, 60, 70]

print()

class MyLst:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        # print('This is MyLst --> __next__')

        if self.i == len(self.lst):
            raise StopIteration
        else:
            self.i += 1

        return self.lst[self.i - 1]

for i in MyLst(lst):
    print(i)

print()


class CustAVG:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
        self.j = 1

    def __iter__(self):
        return self

    def __next__(self):
        # print('This is MyLst --> __next__')

        if self.j == len(self.lst):
            raise StopIteration
        else:
            avg = (self.lst[self.i] + self.lst[self.j]) / 2
            self.i += 1
            self.j += 1

            return avg

tar = []
for i in CustAVG(lst):
    tar.append(int(i))

print(tar)

print()

# ------------------------------------------------------------------------
# Generators ---> memory efficient
#            ---> instead of using return they use yield
#            ---> remembers the state(executed last statement)

def numbers():
    yield 10
    yield 20
    yield 30

x = numbers()

print(next(x))
print(next(x))
print(next(x))

print()

lst = [30, 40, 50, 60, 70]

def avgadj(lst):
    for i in range(len(lst)-1):
        yield int(lst[i]+lst[i+1])/2

for i in avgadj(lst):
    print(int(i))

print()

# ------------------------------------------------------------------------
# Generator Expression ---> Do not require yield
#                      ---> Better memory management  (Memory Efficient)

import random

def maxrandlst():
    lst = []
    for i in range(20):
        lst.append(random.randint(1, 100))

    print('maxrandlst:', max(lst))

maxrandlst()

print()

def maxrand():
    n = 0
    m = random.randint(1, 100)
    for i in range(19):
        n = max(m, random.randint(1, 100))

    print('maxrand:',n)

maxrand()

print()

def maxcomp():
    # m = random.randint(1, 100)
    print('maxcomp:',max(random.randint(1,100) for i in range(20)))  # Generator Expression

maxcomp()

print()

print(max([random.randint(1, 100) for i in range(20)]))    # List Comprehension

print()

words = ['A', 'coddle', 'called', 'Molly', 'Ram', 'Krishna']
numbers = [10, 20, 30, 40]
it = zip(words, numbers)
lst= list(it)
w, n = zip(*lst)
print(w) 
print(n)