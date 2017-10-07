# -*- coding: utf-8 -*-
oanh = [["name","van oanh"],["age",42],["pay",42000],["job","student"]]
huy = [["name","huy"],["age",34],["pay",52000],["job","fucker"]]
people = [oanh,huy]
def field(record,lable):
	"""tìm kiếm giá trị dựa vào value và lable trong một list
	"""
	for (fname,fvalue) in record:
		if fname == lable:
			return fvalue

if __name__ == '__main__':
	for rec in people:
		print field(oanh,'name')