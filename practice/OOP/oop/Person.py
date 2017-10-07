class Person (object):
	'''
	adding behavior 
	'''
	def __init__(self, name, age, pay = 0, job = None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job

	def lastName(self):
		return self.name.split()[-1]

	def giveRaise(self,percent):
		self.pay *= (1.0 + percent)



if __name__ == '__main__':
	oanh = Person('van oanh',42,30000,'sorfware')
	van = Person('Van Kem',48,40000,'hardware')
	huy = Person('Dinh Huy',41,50000,'student')

	# print oanh.lastName(),'and', oanh.pay
	# oanh.giveRaise(10)
	# print "After raise Salary is :",oanh.pay
	db = [oanh,van,huy]
	print type(db)
	for per in db:
		print per.lastName(),'and', per.pay