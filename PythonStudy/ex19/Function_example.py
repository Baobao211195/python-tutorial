# khai báo hàm không tham số 
""""ví dụ khai báo một hàm không tham số
"""
def print_lyrics(): # phần header
# các câu lệnh thực hiện trong thân hàm  (phần body)
	print(" i'am oanh, i am a senior !")
	print("i am trying to become a real programmer !")
	
# call defined function
print_lyrics() 
print()
print()
print()
"""" # to repeat print_lyrics() many times
we create a function contain print_lyrics() function 
"""
# create repeat() function
def repeat():
	print_lyrics()
	print_lyrics()
	print_lyrics()
	
# call repeat()
repeat()
"""
print()
print()
print()
print_lyrics()""" #có thể gọi hàm print_lyrics sau hàm repeat()
