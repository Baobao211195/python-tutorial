"""bài 17 More file
# viết một đoạn mã để copy một file
 tới một file khác."""
 """ 
 cách đọc một file..
tao 2 file nguồn và đích
b1: mở file nguồn ..
b2: đọc file
b3: nhập và mở file với chế độ 'w' cần ghi vào
B4: ghi file
"""
 
from sys import argv
from os.path import exists


script, from_file, to_file = argv

print(" Copying from %s to %s" % (from_file, to_file))

#we could do these two on one line too, how ?
# mở và đọc file đã có sẵn
inputdata = open(from_file)
data = inputdata.read()
print(data)


print(" The input file is %d bytes long " % len(data)) # kiểm tra độ dài đoạn dữ liệu vừa nhập vào 

print(" Does the output file exist ? %r" %exists(to_file)) # kiểm tra file có tồn tại hay không.nếu không trả
															# về false
print("ready, hit RETURN to continue, CTRL-C to abort. ")

input("> ") # nhập tên file cần ghi

output = open(to_file, 'w') # mở file cần ghi với chế độ write

output.write(data) # ghi file

print("Alright, all done")


output.close()
inputdata.close()


