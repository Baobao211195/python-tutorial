print """Chuong trinh quan ly hoc sinh"
	"Bam 1 de nhap thong tin"
	"Bam 2 de in thong tin"
	"Bam 3 de sap xep thong in"
	"Bam 4 de quit chuong trinh"""
List_Truong = []
Dic_HocSinh = {}
i = 0
while  True:
	s = input("Nhap yeu cau :")	
	if s == 1 :   
		i = i + 1
		ho_ten = raw_input("Ho va ten :")
		Tuoi = input("Nhap tuoi :")
		Dic_HocSinh["ID "] = i
		Dic_HocSinh["Hovaten"] = ho_ten
		Dic_HocSinh["Tuoi"] = Tuoi
		
		# Ngay_sinh = raw_input("Nhap ngay sinh :")
		# Dic_HocSinh["Ngay sinh"] = Ngay_sinh
		# Dia_chi = raw_input("Nhap dia chi :")
		# Dic_HocSinh["Dia chi"] = Dia_chi
		#print Dic_HocSinh
		List_Truong.append(Dic_HocSinh)
		print List_Truong



