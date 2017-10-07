from Person import Person
class Manager (Person):
	""""inherite form class Person
	"""
	# def __init__(self):
	# 	super(Manager,self).__init__


	def giveRaise(self, percent, bonus = 0.1):
		self.pay = self.pay * (1.0 +percent + bonus) #khong nen dung self.pay
		return self.pay


if __name__ == '__main__':
	tom = Manager('My Tom',46,5000)
	print tom.lastName()
	print
	print tom.giveRaise(20)
	print 
	print tom.pay

	
	# print " All Information Person "
	# db = [oanh,van,huy, tom]
	