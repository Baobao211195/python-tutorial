class Person(object):
	"""a general person : data + logic
	"""
	def __init__(self,name, age, pay = 0, job= None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job
	def lastName(self):
		return self.name.split()[-1]

	def giveRaise(self,percent):
		self.pay *=(1.0 + percent)

	def __str__(self):
		return ('<%s => %s: %s, %s>' %
			(self.__class__.__name__,self.name,self.job,self.pay))
class Manager(Person):

	""" a person with custom giveRaise
	inherrit general lastname,str
	"""
	def __init__(self,name,age,pay):
		Person.__init__(self,name,age,pay,'Manager')

	def giveRaise(self,percent,bonus = 0.1):
		Person.giveRaise(self,percent +bonus)

def main():
	oanh = Person('Pham oanh',44)
	van	= Person('Nguyen van', 34,4000,'kinh te')
	Nam = Manager('Nguyen Nam',45, 50000)

	print van,van.pay,van.lastName()
	print

	for x in (oanh,van,Nam):
		x.giveRaise(.10)
		print x

if __name__ == '__main__':
	main()

 