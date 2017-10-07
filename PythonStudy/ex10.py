
# có hai cách để in ra một chuỗi trong python
#CÁCH 1:
# sử dụng dấu "\"(ngăn cách- escade) để python biết được chuỗi nào là chuỗi thật
# tức là chuỗi cần in ra , trong trường hợp có nhiều chuỗi được lồng 
# vào với nhau 
# Eg1 : "i "understand" joe."
print("I am 6'2\"tall") # ngăn cách nháy kép bên trong chuỗi
print()
print('I am 6\'2"tall') # ngăn các dấu nháy đơn bên trong chuỗi
#CÁCH 2
# sử dụng 3 dấu ngoặc kép """  và nó làm việc giống như một chuỗi 
# nhưng có thể đặt ở nhiều dòng trong một đoạn text cho đến khi gặp """ lại 
#Eg2 :
tabby_cat = "\tI'm tabbed in." # chen a tap vào trước chuỗi cần in 
persian_cat = "I'am split\non a line."  #\n xuống dòng tiếp thep 
blacdslash_cat = " I'm \\ a \\ cat" # \\ để in một dấu \
fat_cat= """
I 'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass """ # xuống dòng rồi tap 
 # có thể sử dụng dấu '''
print()
print(tabby_cat)
print()
print(persian_cat)
print()
print(blacdslash_cat)
print()
print(fat_cat)
print()
while True:
	for i in ["/","-","|","\\","|"]:
		print("%s\r" %i)  # %r in ra định dạng dữ liệu mà ta sử dụng 
							# nó còn được gọi là raw data
							# luôn luôn nhớ rằng
							# %r để debugg còn %s để hiện thị 


