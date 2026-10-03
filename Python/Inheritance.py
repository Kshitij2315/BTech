# Inheritance: Transmission of traits from parents (base/ super) class to child (derived/ off-spring/ sub) class,
#       where there is-a relationship between classes.
# Features:
#       i)Code reuse,
#       ii)Suppressing any feature/base-class (Method-OverRiding),
#       iii)Extending existing feature
class Base:
    def __init__(self):
        self.count = 0
        print('Base Class Default Constructor')

    def display(self):
        print('Count:', self.count)

    def incr(self):
        self.count += 1

class Derived(Base):                     # Inherited Class
    def __init__(self):
        super().__init__()               # Calling Constructor of Base Class.
        print("Derived Class Default Constructor")
        
    def decr(self):
        self.count -= 1

d = Derived()
d.display()
d.incr()
d.display()
d.decr()
d.display()

print()
print()
print()

# Code reuse

print('Code reuse:')
class Parent:
    def __init__(self):
        self.a = 3
        self._b = 6  # Protected
        self.__c = 9  # Private

    def display_c(self):
        print('self.__c:', self.__c)


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.x = 0
        self._y = 5  # Protected
        self.__z = 10  # Private

    def display(self):
        print('self.x:', self.x)
        print('self._y:', self._y)
        print('self.__z:', self.__z)
        print('self.a:', self.a)
        print('self._b:', self._b)
        # print(self.__c)     # Because __c is private attribute of parent
        super().display_c()  # Calling display_c() from Parent Class

c = Child()
c.display()
print()
c._b = 7
c.x = 100
c.__z = 700            # Creates new attribute
c._Child__z = 700
c.display()
print()
print('isinstance(c, Parent):',isinstance(c, Parent))
print('isinstance(c, Child):',isinstance(c, Child))
print('isinstance(c, Derived):',isinstance(c, Derived))
print('issubclass(Parent, Child):',issubclass(Parent, Child))
print('issubclass(Child, Parent):',issubclass(Child, Parent))
print('issubclass(Child, Base):',issubclass(Child, Base))
print('issubclass(Child, object):',issubclass(Child, object))   #Important --> object is Parent/Base class of every class.
print()
print('dir(object):',dir(object))
print('dir(c):',dir(c))

print()
print()
print()

# Suppressing any feature/base-class (Method-OverRiding)

print('Suppressing any feature/base-class (Method-OverRiding):')
class Abc:
    def fact(self,n):
        i = 1
        fact = 1
        while i <= n:
            fact = fact * i
            i+=1
        print('Factorial of',n,'is:',fact)

class Xyz(Abc):
    def fact(self, n):
        s = str(n)
        add = 0
        for i in range(len(s)):
            add = add + int(s[i])
        print('Sum of digits:',add)

a = Abc()
a.fact(5)

print()

x = Xyz()
x.fact(521)

print()
print()
print()

# Extending existing feature

print("Extending existing feature:")

class Abc:
    def fact(self,n):
        i = 1
        fact = 1
        while i <= n:
            fact = fact * i
            i+=1
        print('Factorial of',n,'is:',fact)

class Xyz(Abc):
    def add(self, n):              # Overriding can be used for extending and suppressing
        super().fact(n)
        s = str(n)
        add = 0
        for i in range(len(s)):
            add = add + int(s[i])
        print('Sum of digits:',add)

x = Xyz()
x.add(11)

print()
print()
print()

# Type of Inheritance:
#       i)Simple Inheritance ---> Single Parent,
#       ii) Multi-Level Inheritance ---> Grand(base), Parent(child), Child(sub-child),
#               Eg: HOD ---> Professor/Teacher ---> Person
#       iii) Multiple Inheritance ---> More than One Parent

print('Multi-Level Inheritance ---> Grand(base), Parent(child), Child(sub-child): '
      ' Eg: HOD ---> Professor/Teacher ---> Person')

class Person:
    def __init__(self):
        self.aadharNum = 165465

    def display(self):
        print('I am a Person with Aadhar Number:', self.aadharNum)

class Profesor(Person):
    def __init__(self):
        super().__init__()
        # print('Inside Proffesor ___init__()')
        self.empID = 46546531

    def display(self):
        super().display()
        print('I am a Profesor with Employee ID:', self.empID)

class HoD(Profesor):
    def __init__(self):
        super().__init__()
        self.accessKey = 8845578

    def display(self):
        # super().__init__()            # Can be called in a method too.
        super().display()
        print('I am HoD with Access Key:', self.accessKey)

h = HoD()
h.display()

print()
print()
print()

# Multiple Inheritance ---> More than One Base

print('Multiple Inheritance ---> More than One Base:')

class Abc:
    def __init__(self):
        self.a = 16

    def display(self):
        print('self.a:', self.a)

class Xyz:
    def __init__(self):
        self.x = 48

    def display(self):
        print('self.x', self.x)

class Pqr(Abc, Xyz):
    def __init__(self):
        Abc.__init__(self)
        Xyz.__init__(self)
        self.p = 36

    def display(self):
        Abc.display(self)
        Xyz.display(self)
        print('self.p:', self.p)
        sum = self.p + self.x + self.a
        print('sum:', sum)

p = Pqr()
p.display()