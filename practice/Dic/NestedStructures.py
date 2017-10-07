bob = {'name' :{'first':'Bob','last':'Smith'},
        'age':42,
         'job':['sorfware','writting'],
         'pay':(4000,5000)}
print bob['name']
print
print bob['name']['last']
print
print bob['pay'][1]
print "Find job of bob"
for job in bob['job']:
	if job.startswith('sorfware'):
		print job
print "Add job in job of bob"
bob['job'].append('engeneer')
print "Jobs of bob after append are ",bob['job']