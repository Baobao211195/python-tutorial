print "Let's practice everything"
print 'You\'d need to know \' bout escapes with \\ that do \n newlines and \t tabs. '
poem = '''
\t the lovely word 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\t where there is none.
'''

print "------------------"
print poem
print "------------------"

five = 10-2 +3-6 # khai bao bien five
print "This should be five : %s " % five
'''khoi tao mot ham voi mot tham so 
	gia tri tra ve la cac ket qua thuc hien trong ham
'''

def secret_formula(started):
	jelly_beans = started*500
	jars = jelly_beans/10000
	crates = jars / 100
	return jelly_beans, jars, crates



# khai bao mot tham so mac dinh la 100
start_point = 10000
beans, jars, crates = secret_formula(start_point)
print "With a starting point of : %d" %start_point

print "We'd have %d beans, %d jars, and %d crates." %(beans,jars,crates)

start_point = start_point/10
print"We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates:"%secret_formula(start_point)

