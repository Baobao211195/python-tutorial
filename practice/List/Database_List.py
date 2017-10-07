# -*- coding: utf -8 -*-
import math

#trong example1 có những thứ sau 
bob = ['Bob Smith',42,3000,'sorfware']
sue = ['Sue Jones',45,4000,'hardware']

people = [bob,sue] #list of list
			# duyet list
# for person in people:
# 	print person # in từng list

# 	print person[1] # in index 1 của các list

			# duyet cua thể từng phần tử của list con trong list people
# for person in people:

# 	print person[0].split()[0] #in ra su va bod
			# một vài câu lệnh hay sử dụng 
pay = map((lambda x:x[2]),people)  #  map trả về một list
print pay  # map là một generator in 3.x
print
print sum(pay) # tinh tong  
          # add a list in people
people.append(['van oanh',50, 5000,'electronic'])
print people