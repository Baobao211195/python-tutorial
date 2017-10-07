# class Point:
# 	"A Class implementation of a 2-dimensinal point"
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
# 	def __str__(self):
# 		return "(%d,%d)"%(self.x,self.y)

# def main():
# 	P1 = Point(2,4)
# 	print P1.__doc__
# 	print P1.__str__
# if __name__ == '__main__':
# 	main()
def buildConnectionString(params):
"""Build a connection string from a dictionary of parameters.Returns string."""
	return ";".join(["%s=%s" % (k, v) for k, v in params.items()])
if __name__ == "__main__":
	myParams = {"server":"mpilgrim", \
				"database":"master", \
				"uid":"sa", \
				"pwd":"secret" \}
									
print buildConnectionString(myParams)