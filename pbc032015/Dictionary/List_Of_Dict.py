# -*- coding: utf -8 -*-
import math

oanh = {'name':'oanh','age':42,'pay':3000,'job':'student'}
huy = {'name':'huy','age':45,'pay':5000,'job':'mặt Dày'}
people = [oanh, huy]
for person in people:
# 	print person['name'],',',person['pay'],"\n"
	if person['name'] == "oanh":  #fetch oanh'pay
		print person['pay']

for person in people: # collect names 
	print person['name']

print
print list(map((lambda x:x['name']),people)) # return list of name

print
# caculate sum of pay
for person in people:
	print sum(person['pay']) 
"""
một vài câu lệnh sử dụng để truy cập trong SQL
sử dụng để truy cập cấu trúc dữ liệu 

"""