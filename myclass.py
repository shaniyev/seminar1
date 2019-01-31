class my_point:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def print_ab(self):
		print('a = ', self.a)
		print('b = ', self.b)

	def sum_ab(self):
		return self.a + self.b

	def mult_ab(self):
		return self.a * self.b

class my_point_child(my_point):
	pass