#-*- utf-8
import sys
#kiem tra do dai cua list: = 1 la list rong
# thuc hien in vo han du lieu tu nguoi su dung
if len(sys.argv) ==1:
	while True:
		print (raw_input("Nhap thong tin 1 :"))
#neu khong thi filenam la mot argv[1] 1 tham so dau vao
#doc file 
if len(sys.argv) == 2:
	path = sys.argv[1] # tham so dau tien  trong list
	f = open(path) # ten file truyen vao va mo file
	# in ra man hinh
	print(f.read())
	f.close() #close file
else:
	s = raw_input("Nhap thong tin  2:")
	path2 = sys.argv[2]
	f = open(path, 'w')
	f.write(s)
	f.close()


	