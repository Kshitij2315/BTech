class DateUtility:
    def __init__(self, d=0, m=0, y=0):
        self.dd = d
        self.mm = m
        self.yyyy = y

    def disp_data(self):
        print(self.dd, '/', self.mm, '/', self.yyyy)

    def greater(self, other):
        if self.yyyy > other.yyyy:
            return True
        elif self.yyyy < other.yyyy:
            return False
        elif self.mm > other.mm:
            return True
        elif self.mm < other.mm:
            return False
        elif self.dd > other.dd:
            return True
        else:
            return False

    def __gt__(self, other):        # Operator Overloading: Eg: 'greater()' is called by '>'
        if self.yyyy > other.yyyy:
            return True
        elif self.yyyy < other.yyyy:
            return False
        elif self.mm > other.mm:
            return True
        elif self.mm < other.mm:
            return False
        elif self.dd > other.dd:
            return True
        else:
            return False

    def __add__(self, other):
        d = self.dd + other.dd
        m = self.mm + other.mm
        y = self.yyyy + other.yyyy
        if d > 30:
            d = d - 30
            m = m + 1
        if m > 12:
            m = m - 12
            y = y + 1

        return d, m, y

d1 = DateUtility(13,8, 2026)
d1.disp_data()
d2= DateUtility(8,1, 2027)
d2.disp_data()

print()

print('d1.greater(d2):',d1.greater(d2))

print()

print('d2.greater(d1):',d2.greater(d1))

print()

print('d2>d1 :',d2>d1)

print()

print(d1+d2)
