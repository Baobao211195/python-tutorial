sr = open("oanh.txt",'r')
dic = open("oanh2.txt",'w')
dic.truncate(len("oanh2.txt"))

for line in sr.readlines():
	dic.writelines(line)
dic.close()

dic2 = open("oanh2.txt",'r')
print (dic2.read())
dic2.close()






