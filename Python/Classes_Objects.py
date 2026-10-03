# Programming Paradigms ---> Types:
#                       i) Structured
#                      ii) Functional
#                     iii) Object Oriented Programming
# Object Oriented Programming ---> Why needed ----> More related to Real World Object like Table, Bed, Mirror.
# Objects are related to each other in some or other manner, so related/similar types of Object forms a Class.
# For example: Bed and Table are related/similar to each other which forms a Class called Furniture.
# Classes are intangible/Logical/Imaginary/Generic in Nature. But Objects are Physical or Tangible.
# Generic in Nature vs Specific in Nature
# They are logical Group of Objects. Eg: Sparrow, Crow, Pigeon are Objects and they form a class called 'Bird'.
# Similarly Virat, Sachin, Dhoni are Objects of Class 'Players'.
# Classes are just like template(Stencil/Tracing paper).
# Paradigms ---> Model/Principle/Prototype/Way of doing programming.
# Objects contain two things:
#                  i) Features/Attribute/Traits
#                 ii) Funtions/Behavior
# Class should contain:
#              i) Attributes/Form/Member-Data/Attribute-Data/Properties/Instance-Data/Field/Variable
#             ii) Functions ---> Member-Methods/Member-Functions/Behavior/Functionality which can access Class Attributes
# Technical Definition of Objects ---> Instance/Example of a Class is called an Object.
# Basic purpose of Contructor is to initialize attributes of an object.
# We need not to call the constructors.
# Constructor is automatically called at the time of object creation.
# Constructors are called once in their lifetime at the time of object creation.
# Constructor do not return anything.
# Constructer overloading is not possible in python.
# But can be depicted using Variable Lenght Parameters/Keyword or by Assigning Default Values.
# Constructors are named as '__init__():'
# Destructor are also called automatically when object is about to be deleted from the memory,
#                                              when it no longer needed in the program.
# Destructors are named as '__del__():'

class MyClass:
    def set_data(self):
        self.attr1 = 0

    def display_data(n):
        print('Display Data')

    def show(n):
        print('Show Data:',n.attr1)

obj1 = MyClass()
obj1.display_data()
# MyClass.display_data(obj1)
# print(type(obj1))
obj1.set_data()
obj1.show()

# Constructors

