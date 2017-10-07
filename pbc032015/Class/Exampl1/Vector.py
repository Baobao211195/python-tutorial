# -*- coding: utf-8 -*-
class Vector:
	"""docstring for"""
	def __init__(self, tungdo, hoanhdo):
		self.tungdo = tungdo
		self.hoanhdo = hoanhdo
	def __str__(self): # hàm chuyển đối tượng thành chuỗi
		return "Vector (%d,%d)" %(self.tungdo,self.hoanhdo)
 

	def __add__(self, other): #hàm cộng các đối tượng
		return Vector(self.tungdo + other.tungdo,self.hoanhdo + other.hoanhdo)


def main():
	v1 = Vector(2,2)
	v3 = Vector(-9,7)
	print v1.__str__()
	print
	print v3.__str__()
	print
	print v1 + v3
	print
	print v1.__add__(4)
	print 
	print v3.__add__(5)


if __name__ == '__main__':
	main()


		