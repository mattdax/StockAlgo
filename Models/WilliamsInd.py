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
		self.sell = []
		self.buy = []
		print(len(self.Symbol))
		print(len(self.Whigh))
		print(len(self.Cprice))
		self.calcInd()
	
	def calcInd(self):
		for i in range(0,len(self.Symbol)-1,1):
			print(i)
			try:
				r = ((self.Whigh[i]-self.Cprice[i])/(self.Whigh[i]-self.Wlow[i])*-100)
				self.williams.append(r)
			except ZeroDivisionError:
				 self.williams.append(float(0))
		self.FilterInd()
	
	def FilterInd(self):
		for i in range(0, len(self.williams),1):
			if self.williams[i] > -20:
				self.sell.append(self.Symbol[i])
			if self.williams[i] < -80:
				self.buy.append(self.Symbol[i])
		print(self.sell, self.buy)



Williams()