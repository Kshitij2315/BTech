class MyTime:
	def __init__(self, h =0, m =0, s =0):
		self.hh = h
		self.mm = m
		self.ss = s

	def set_data(self,h,m,s):
		self.hh = h
		self.mm = m
		self.ss = s

	def disp_data(self):
		print(self.hh,':',self.mm,':',self.ss)

	def add(self,other):
		t4 = MyTime()
		t4.ss = self.ss + other.ss
		t4.mm = self.mm + int(other.mm)
		t4.hh = self.hh + other.hh
		if t4.ss >= 60:
			t4.ss -= 60
			t4.mm += 1
		if t4.mm >= 60:
			t4.mm -= 60
			t4.hh += 1
		return t4         #t4.disp_dat()

	def __add__(self,other):     # Operator Overloading
		t4 = MyTime()
		t4.ss = self.ss + other.ss
		t4.mm = self.mm + int(other.mm)
		t4.hh = self.hh + other.hh
		if t4.ss >= 60:
			t4.ss -= 60
			t4.mm += 1
		if t4.mm >= 60:
			t4.mm -= 60
			t4.hh += 1
		return t4  # t4.disp_dat()
t1 = MyTime()
t1.set_data(5,17,39)
t1.disp_data()
t2 = MyTime()
t2.set_data(6,58,45)
t2.disp_data()
print(t1.hh)
print(t2.hh)

print()

t4 = t1.add(t2)
t4.disp_data()      # t1.add(t2).disp_data()

t5 = t1+t2
t5.disp_data()