""""bài này 
làm việc với functions and file 
"""
from sys import argv

script, input_file = argv
# tạo một hàm in data trong file
def print_all(f):
	print(f.read())

# tạo một hàm 
def rewind(f):
	f.seek(0)
	
# tạo một hàm in từng dòng
def print_a_line(line_count , f):
	print(line_count, f.readline())
	
current_file = open(input_file)

print("First let's print the whole file:\n.")

# gọi hàm print_all
print_all(current_file)
#gọi hàm rewind
rewind(current_file)

print("let's print three file:")

for current_line in range(1,4):
	print_a_line(current_line, current_file)

#current_line =+ current_line 
#print_a_line(current_line, current_file)

#current_line += current_line
#print_a_line(current_line, current_file)

