# def create_hoan_vi(list1):
# 	import itertools
# 	return list(itertools.permutations(list1))
# # print create_hoan_vi([1,2])

# def printValues():
# 	l = list()
# 	for i in range(1,21):
# 		l.append(i**2)
# 	print(l[5:])

# printValues()

 # l = ['*' for col in range(6)]
 # print l
def creat_a():
	result_str_a="";      
	for row in range(0,7):      
	    for column in range(0,7):       
	        if (((column == 1 or column == 5) and row != 0) 
	    									or ((row == 0 or row == 3) 
	    									and (column > 1 and column < 5))):      
	           	result_str_a=result_str_a+"*"      
	        else:        
	            result_str_a=result_str_a+" "      
	    result_str_a=result_str_a+"\n"      
	print(result_str_a);  

def create_e():
	result_str_e="";      
	for row in range(0,7):      
	    for column in range(0,7):       
	        if (column == 1 or 
	        				((row == 0 or row == 6) and (column > 1 and column < 6))
	        				or (row == 3 and column > 1 and column < 5)):    
	            result_str_e=result_str_e+"*"      
	        else:        
	            result_str_e=result_str_e+""      
	    result_str_e=result_str_e+"\n"      
	print(result_str_e);  

print creat_a()
print create_e()

COUNTRIES, DEPARTMENTS, EMPLOYEES, GROUPS, JOB_HISTORY, JOBS, LOCATION, REGIONS, STUDENT









