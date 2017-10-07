class Student:
	

	def __init__(self, ten, Lop, diemToan, diemLy, diemHoa):
		self.name = ten
		self.Lop = Lop
		self.diemToan = diemToan
		self.diemLy = diemLy
		self.diemHoa = diemHoa

	def Dispaly(self):
		print "%5s%5s%3d%3d%3d" % (self.name,self.Lop,self.diemToan,self.diemLy,self.diemHoa)

	def Average(self):
		ave = (self.diemToan + self.diemLy + self.diemHoa)/3
		return ave
	

def main():

	hovaten = raw_input("Nhap ho van ten :")
	lop = raw_input("Nhap Lop :")
	toan = input("Nhap diem Toan :")
	ly = input("Nhap diem LY :")
	hoa = input("Nhap diem Hoa :")
	a = Student(hovaten,lop,toan,ly,hoa)
	a.Dispaly()
	print "Diem trung binh cac mon hoc la %d" %a.Average()


if __name__ == '__main__':
	main()