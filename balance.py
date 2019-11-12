import os, sys, inspect

class Balance():
	def __init__(self):
		self.balance  = 0
		self.readBalance()
	def readBalance(self):
		current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		sys.path.insert(0, current_dir) 
		with open("balance.txt","r") as balance:
			self.balance = (balance.readline())
			balance.close()
