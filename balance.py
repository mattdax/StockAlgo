# Import Statements
import os, sys, inspect


# Pulls balance from 'balance.txt'
class Balance():
	def __init__(self):
		# Init
		self.balance  = 0
		self.readBalance()
	

	def readBalance(self):
		
		# Sets working directory to models folder
		current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		sys.path.insert(0, current_dir) 
		file = "\\models\\balance.txt"
		

		path = os.getcwd()+file
		# Opens file and reads the balance 
		with open(path,"r+") as balance:
			self.balance = int(balance.readline())
			balance.close()
Balance()
