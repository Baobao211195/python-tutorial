# -*- coding: utf-8 -*-
class BankAcount:
	"""docstring for BankAcount"""
	def __init__(self, holder, numberCard, balance):
		self.Holder =  holder
		self.NumberCard = numberCard
		if(Balance >= 0):
		 	self.Balance = balance
		 else:
		 	print "The Acount is not exits"

	def Deposit(self,amount):
		pass
	def Withdraw(self, amount):
		pass
	def getBalance(self):

		pass
	def Transfer(self, amount, target):
		pass