# Containership: Do not reinvent the wheel from scratch but reuse existing code.
# Containership and Inheritance support Reuse.
# Containership and Inheritance both are used to enhance the existing classes.
# Containership also called Composition.
# We prefer Containership when there is 'has-a' relationship between two Objects or Classes.
#	Eg: i) University has Teachers and Students.
#	   ii) Car has an Engine.

class Abc:  # Already existing class
    def display(self):
        print('This is the Abc class display method')

class Xyz:
    def __init__(self):
        self.a = Abc()

    def display(self):
        self.a.display()
        print('This is the Xyz class display method')

x = Xyz()
x.display()