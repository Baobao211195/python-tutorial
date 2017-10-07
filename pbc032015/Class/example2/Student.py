class Student(object):
	def __init__(self):
		self.ten = raw_input("Nhap Ten :")
		self.tuoi = input("Nhap Tuoi :")
		self.namsinh = input("Nhap Nam Sinh :")
		self.gioitinh = raw_input("Nhap Gioi Tinh :")	
	def PrintInf(self):
		print (self.ten,self.tuoi,self.namsinh,self.gioitinh)
	#hovaten=raw_input("Nhap Ten :"),tuoi = input("Nhap Tuoi :"),namsinh = input("Nhap Nam Sinh :"),gioitinh = raw_input("Nhap Gioi Tinh :")
	

if __name__ == '__main__':

	nam = Student()
	nam.PrintInf()
		
