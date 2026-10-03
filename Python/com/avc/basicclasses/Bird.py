class Bird:

    wings = 0  # Common to all Objects called as Class Variable

    def __init__(self, w = 0, c = ' '):
        Bird.wings += 2
        self.weight = w
        self.colour = c

    def __del__(self):
        print()
        print()
        print()
        print('Deleting Bird Object: \n Weight:',self.weight,'\n Colour:',self.colour)
        print("Address:",self)

    def set_data(self):
        self.weight = 50
        self.colour = 'Black'

    def disp_data(self):
        print('Colour:', self.colour)
        print('Weight:', self.weight)

    def cls_method():                    # Class Methods. Common to all object.
        print('I am class method')       # Called using Class Name, and do not contain 'self'

    def compare(self, other):  # self = b1
        if self.weight == other.weight and self.colour == other.colour:
            return True
        else:
            return False

b1 = Bird(0,' ')
b1.set_data()
b1.disp_data()

print()

b2 = Bird(32,'Brown')
b2.disp_data()

print()

b3 = Bird()
b3.disp_data()

print()

b4 = Bird(40)
b4.disp_data()

print()

Bird.cls_method()     # Class Method are called using class reference not object.

print()

print('vars():',vars())   # Prints dictionary of attributes in current module.
print('dir():',dir())    # Prints list of attributes in current module (only keys of dictionaries)

print('vars(b1):',vars(b1))

print('dir(Bird):',dir(Bird))

print()

print('Total Number of wings altogether:', Bird.wings)

print()

print('b1.compare(b2):',b1.compare(b2))