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
		#self.parent_dir = os.path.dirname(current_dir)
		#print(self.parent_dir)
		
		
		sys.path.insert(0, current_dir) 
		
		# FROM MODELS FOLDER 
		file = "\\balance.txt"
		
		

		paths = os.getcwd()+file
		print(paths)
		# Opens file and reads the balance 
		with open(paths,"r+") as balance:
			self.balance = int(balance.readline())
			balance.close()
Balance()
