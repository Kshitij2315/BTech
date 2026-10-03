class MyDate:
	def __init__(self, d, m, y):
		self.dd = d
		self._mm = m
		self.__yyyy = y

	def set_data(self,d,m,y):
		self.dd = d
		self._mm = m             # '_' means protected attribute
		self.__yyyy = y          # '__' means private attribute

	def disp_data(self):
		print(self.dd,'/',self._mm,'/',self.__yyyy)
d1 = MyDate()
d1.set_data('05','08','2026')
d1.disp_data()
print(d1.dd)
print(d1._mm)    # Protected can be accessed directy outside of class
# print(d1.__yyyy)   # Private attributes cannot be accessed directy outside of class
print(d1._MyDate__yyyy)  # Private attributes are renamed by python in this format
# print(d1._MyDate__mm)