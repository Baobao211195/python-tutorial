bob = {'name':'Bob Smint','age':42,'pay':4200,'job':'Sorfware'}
sue = {'name':'Sue John','age':46,'pay':4500,'job':'Hardware'}
print bob['name'].split()[0]
#make a dict
print "the first way to make a dictionary"
oanh = {}
oanh['name'] = 'van oanh'
oanh['age'] = 42
oanh['pay'] = 3000
oanh['job'] = 'Electronic'
print oanh
print
print """	the second way to make a dictionary
			by zipping name and values
			name and value are list"""
name = ['name','age','pay','job']
value = ['Nguyen Van',32,40000,'Accountant']
van = zip(name,value)  #zip retur a list of tuples
print van 
print 'convert to dictionary'
van = dict(zip(name,value))
print van
print
print """	the third way to make a dictionary
			use fromkeys()
			to initiallize a empty value dictionary"""
fields = ('name','age','pay','job')
value = dict.fromkeys(fields,'?')
print value