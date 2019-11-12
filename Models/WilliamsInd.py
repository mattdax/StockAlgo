"""
TODO

- Comment
- figure out why all symbols are not being taken
"""

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import API

class Williams():
	
	def __init__(self):
		self.info = API.StockAPI().info
		self.Cprice = self.info[0]
		self.Whigh = self.info[1]
		self.Wlow = self.info[2]
		self.Symbol = self.info[3]
		self.williams = []
		self.calc()
	def calc(self):
		for i in range(0,len(self.Symbol)-1,1):
			try:
				r = ((self.Whigh[i]-self.Cprice[i])/(self.Whigh[i]-self.Wlow[i])*-100)
				self.williams.append(r)
			except ZeroDivisionError:
				 self.williams.append(float(0))
		print(self.williams)

Williams()