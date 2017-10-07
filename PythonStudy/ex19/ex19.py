"""
ôn tập về function và variable
note: + biến trong hàm (tham số truyền vào) không liên 
		quan tới biến ở ngoài
		

"""
# create a function cheese_and_crackers with two argument
def cheese_and_crackers(cheese_count, boxes_of_cracker):
	print("You have %d cheese !" % cheese_count)
	print("You have %d boxes of cracker!" % boxes_of_cracker)
	print(" it is enough for our party")
	
print("we can just give the function numbers directly:")
cheese_and_crackers(20,30) #  equal two argument to function

print("OR, we can use variables from our script :")	
# define two variables
amount_of_cheese = 10
amount_of_crackers = 50

# trasmit two argument as  defined variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print("we can even do math inside too:")
cheese_and_crackers(10+20, 5+6) #trasmit directly to function

print("And we can combine the two, variable and math:")
# combine variables and math as argument to function
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
""" Result :
we can just give the function numbers directly:
You have 20 cheese !
You have 30 boxes of cracker!
 it is enough for our party
OR, we can use variables from our script :
You have 10 cheese !
You have 50 boxes of cracker!
 it is enough for our party
we can even do math inside too:
You have 30 cheese !
You have 11 boxes of cracker!
 it is enough for our party
And we can combine the two, variable and math:
You have 110 cheese !
You have 1050 boxes of cracker!
 it is enough for our party
"""

# BÀI TẬP LÀ VIẾT MỘT HÀM CỦA RIÊNG BẠN VÀ CHẠY NÓ THEO 10 CÁCH KHÁC NHAU
