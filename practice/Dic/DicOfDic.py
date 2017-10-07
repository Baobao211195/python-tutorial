bob = {'name':'Bob Smint','age':42,'pay':4200,'job':'Sorfware'}
sue = {'name':'Sue John','age':46,'pay':4500,'job':'Hardware'}
database = {} 
database['bob'] = bob # key is 'bob' and value is dict of bob
database['sue'] = sue
print """
		make of empty dict cover two children dict"""
print database['bob']['name']
print "fetch sue's pay"
database['sue']['pay'] = 50000
print "Now sue's pay is",database['sue']['pay']
print"All information about database"
print database
print "import a module help pretty - print infomation in database"
import pprint # module help in thong tin mot cach dep hon
print pprint.pprint(database)
print
print "manipulation with key"
for key in database: # key are bob and sue
	print key,"=>",database[key]['name'] ,"is a",database[key]['job']
sue = {'name':'Sue John','age':46,'pay':4500,'job':'Hardware'}
huy = {'name':'Dinh Huy','age':32,'pay':5200,'job':'Chef'}
Kha = {'name':'Khanh Nguyen','age':22,'pay':1300,'job':'Engineer'}
Duc = {'name':'Tran Duc','age':62,'pay':8900,'job':'Director'}
Tha = {'name':'Cong Thanh','age':23,'pay':6700,'job':'Supervisor'}
Tung = {'name':'Tung Van','age':45,'pay':4900,'job':'assitant'}
Nam = {'name':'Nam Hoang','age':36,'pay':8500,'job':'Cloud'}
Hai = {'name':'Hai Tran','age':27,'pay':7800,'job':'OpenStack'}
Minh = {'name':'Minh Ha','age':18,'pay':6200,'job':'firmware'}
