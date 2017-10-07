# records
bob  = {'name':'Bob Smint','age':42,'pay':4200,'job':'Sorfware'}
sue  = {'name':'Sue John','age':46,'pay':4500,'job':'Hardware'}
huy =  {'name':'Dinh Huy','age':32,'pay':5200,'job':'Chef'}
Minh = {'name':'Minh Ha','age':18,'pay':6200,'job':'firmware'}
Hai = {'name':'Hai Tran','age':27,'pay':7800,'job':'OpenStack'}
Tung = {'name':'Tung Van','age':45,'pay':4900,'job':'assitant'}
Tha = {'name':'Cong Thanh','age':23,'pay':6700,'job':'Supervisor'}
Duc = {'name':'Tran Duc','age':62,'pay':8900,'job':'Director'}
Kha = {'name':'Khanh Nguyen','age':22,'pay':1300,'job':'Engineer'}

#database 
db ={}
db['bob'] = bob
db['sue'] = sue
db['huy'] = huy
db['Minh'] = Minh
db['Hai'] = Hai
db['Tung'] = Tung
db['Tha'] = Tha
db['Duc'] = Duc
db['Kha'] = Kha
if __name__ == '__main__':
	for key in db:
		print key,'=>\n',db[key] 
