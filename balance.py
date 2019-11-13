# Import Statements
import os, sys, inspect, json


# Pulls balance from 'balance.txt'
class Balance():
	def __init__(self):
		# Init
		self.balance  = 0
		self.readBalance()
	

	def readBalance(self):
		
		# Sets working directory to models folder
		current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		self.parent_dir = os.path.dirname(current_dir)
		
		
		sys.path.insert(0, self.parent_dir) 
		
		# FROM MODELS FOLDER 
		file = "\\StockAlgo\\Data\\balance.json"
		
		

		paths = self.parent_dir+file

		# Opens file and reads the balance 
		with open(paths,"r") as balance:
			
			self.balance = int((json.loads(balance.read())['balance']))
			balance.close()
Balance()
