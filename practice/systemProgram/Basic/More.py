# -*- coding: utf8 -*-
""""
phân chia và tuong tac đánh sô môt
chuoi hoăc mot đoan text hoăc fil


"""
def more(text,numberlines):
	lines = text.splitlines()  # giong split('\n') khong co '' kêt thu cuoi cung
	while lines:
		chunk = lines[:numberlines]  # tru 10 dong dau tien 
		lines = lines[numberlines:]  # lây 10 dong dau tien
		for line in chunk:
			print line
		if lines and raw_input('More ? ') not in ['y', 'Y']: # chon y hoac Y thi doc tiep..ko thi break
			break
if __name__ == '__main__':
	import sys
	more(open(sys.argv[1]).read(),10) # đoc 10 dong môt lân, 
"""
ham splitlines() se chia string thanh cac substring va luu vao trong mot list voi dieu kien chuoit co
\n  (eg 
>>> str = "pham van onah ha nam\nisnh ngay 34\n\nnaamfnaf"
>>> print str.splitlines()
['pham van onah ha nam', 'isnh ngay 34', '', 'naamfnaf'])
from package.subpackage import module # Alternative
"""