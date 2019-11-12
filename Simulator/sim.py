"""
TODO

- cur price function added
- finish buy
- finish sell
- comment
"""

import sys 
sys.path.insert(1, '/StockAlgo/Scrapers') 

class Simulator():
	
	def __init__(self):
		self.Ssym = []
		self.Sprice = []
		self.Svolume = []

	def buy(self):
		account = open('testfile.txt','w')
		for i in range(0, len(self.Sprice), 1):
			
			account.write(str(self.symbol)+str(self.Sprice*self.Svolume))
		account.close()
