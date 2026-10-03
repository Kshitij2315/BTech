class Abc:
    def display(self):
        print('This is the Abc class display method')

    class Def:
        def display(self):
            print('This is the Nested Def class display method')

class Xyz:
    def display(self):
        print('This is the Xyz class display method')

a = Abc()
a.display()
x = Xyz()
x.display()
d = Abc.Def()
d.display()