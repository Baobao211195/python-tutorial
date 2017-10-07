class People (object):
	pcount = 0 
# self.name la mot instance variable ko duoc dung chung

	def __init__(self, name = "Van oanh"):
		self.name = name # dinh nghia bien cho instance variable
						# la mot thuoc tinh name cho a..doi tuong truyeen vao
		People.pcount = People.pcount + 1
		print "%s da duoc sinh ra" % self.name
		print "So nhan vien da duoc sinh ra %d" % People.pcount

	def getpop(self):
		print "Dan so hien co la :",People.pcount
	def __getpop(self): # đóng gói 
		print "Dan so hien co la :",People.pcount	

class VietnamPeople(People):

	def __init__(self):
		Super(VietnamPeople,self).__init__ # class cha phai co class object

	quocgia = "vietNam"
	quocca = "Tien quan ca"

	def getpop1(self):
		print "I will calculate Vietnam pop only"




def main():
	a = People("ha nam")
	a.getpop()
	b = People("Minh")
	b.getpop()

	v = VietnamPeople("viet nam")
	v.getpop()
	v.getpop1()



if __name__ == '__main__':
	main()