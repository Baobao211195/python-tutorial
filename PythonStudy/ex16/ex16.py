# reading and writting files
""" nhập và mở file cần ghi dữ liệu
kiểm tra file có rống không = hàm truncate()
nhâp theo từng dòng bằng input()
ghi bằng lệnh write()
"""
from sys import argv
script, filename = argv # hai tham số đầu vào 
 
print("We're going to erase %r." % filename)
print("if you don't want that, hit CTRL -C ")
print("If you do want that, hit RETURN.")

input("? ") # đầu vào là filename (oanh.txt đã lưu trong thư mục làm việc)

print("Opening the file...")
target = open(filename, 'w') # mở file và chế độ là write
							# 'a' là append : thêm nội dung vào file

print("Truncating the file. Goodbye !")
target.truncate() # đây là rỗng file..nó sẽ xóa nội dung trong file trước khi ghi vào

print("Now I'm going to ask you for three lines.")
#nhập các chuối đầu vào 
lines1 = input("line 1: ")
lines2 = input("line 2: ")
lines3 = input("line 3: ")


print("I'm going to write these to the file.")

target.write(lines1)
target.write("\n")
target.write(lines2)
target.write("\n")
target.write(lines3)
target.write("\n")

#target.write('%3b''%2b''%2b'%(lines1,lines2,lines3))

print(" And finally, we close it.")
target.close()
# đọc file đã tạo

txt = open(filename,'r')
print(txt.read())
txt.close()