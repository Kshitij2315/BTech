# Classes which cannot be instantiated (cannot create object of class) are called as Abstract Classes.
# They are always inherited by other classes and cannot be used separately.
# Abstract Classes have at-least one abstract method.
# If a class contain at-least one abstract method it becomes mandatory to declare such class as 'Abstract Class'.
# Basic purpose is again reusability of code.
# Abstract Class are made for consistency.
# Abstract Method are denoted with Decorator i.e. '@abstractmethod'.
# Abstract Class always inherited from ABC(Abstract Base Class).
# Abstract Class always acts as parent.
# It is mandatory for child class of abstract class to override Abstract Method of the Parent Class,
#       otherwise this child is also declared as Abstract Class.
# Finally, a concrete (tangible) class should not have any abstract method and can be instantiated.
# Example: Shape: Circle, Square
# If all method of the 'Abstract Class' are 'Abstract Method' then such class is called as interface.
# Ultimate form of Abstract Class is called Interface.
# Interfaces are useful in:
#           Integration of 2 or more systems,
#           Implementing Adaptors,   ---> UPI: reciver_bank_account_number, sender_bank_account_number, amount
#           Runtime Polymorphism.

from abc import abstractmethod, ABC

class MyAbstractClass(ABC):
    def display(self):
        print('This is the MyAbstractClass display method')

    @abstractmethod
    def show(self):
        print('This is the MyAbstractClass show method')

# a = MyAbstractClass()        # Cannot be instantiated
# a.display()

class MyChildCLass(MyAbstractClass):
    def show(self):
        print('This is the MyChildClass show method')

c = MyChildCLass()
c.show()

class Shape(ABC):
	@abstractmethod
	def draw(self):
		pass

class Circle(Shape):
	def draw(self):
		print('This is a circle')

class Square(Shape):
	def draw(self):
		print('This is a square')


c = Circle()
c.draw()

s = Square()
s.draw()