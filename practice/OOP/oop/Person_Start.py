class Person:
	def __init__(self, name, age, pay = 0, job = None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job
if __name__ == '__main__':
	oanh = Person('van oanh',42,30000,'sorfware')
	van = Person('Van Kem',48,40000,'hardware')
	huy = Person('Dinh Huy',41,50000,'student')


	print oanh.name.split()[-1]
	print van.pay
	print oanh.job,huy.pay