""" Functions can return something
bai 21
"""
def add(a,b):
	print "Adding %d +%d" %(a,b)
	return a+b
def subtract(a,b):
	print "Subtracting %d - %d" %(a,b)
	return a-b
def Multiply(a,b):
	print "Multipling %d * %d" %(a,b)
	return a*b
def Divide(a,b):
	print "Dividing %d / %d" %(a,b)
	return a/b
print "Let's do some math with just functions !"

age = add(40,5)
height = subtract(78,4)
weight = Multiply(90,2)
iq = Divide(100,2)

print "Age : %d, Height : %d, Weight: %d, IQ : %d" %(age, height, weight, iq)

print "Here is a puzzle."

what = add(age, subtract(height, Multiply(weight,Divide(iq,2))))
print " That becomes : ", what, "Can you do it by hand ?"
