# bài 18
"""
names, varible, code, Function
cách định nghĩa một hàm và truyền tham số cho hàm đó
hàm có tham số và hàm không tham số
"""
# create print_two function 
def print_two(* args):
	arg1, arg2 = args ## khai báo như một list (học sau)
	print("arg1: %r, arg2: %r" %(arg1, arg2))
# create print_two_again function
def print_two_again(arg1, arg2):
	print("arg1: %r, arg2: %r" %(arg1, arg2))
# create function with one argument
def print_one(arg1):
	print("arg1: %r " % arg1)
# create function without argument
def print_none():
	print("I got nothings")

	# call function with argument 
print_two("oanh","duc")
print_two_again("nam","anh")
print_one("First !")
print_none()