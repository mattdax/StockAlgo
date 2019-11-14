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
		# Calls data needed from Stock API class 
		self.info = API.StockAPI().info
		
		# Stores data that was loaded in lists
		self.Cprice = self.info[0]
		self.Whigh = self.info[1]
		self.Wlow = self.info[2]
		self.Symbol = self.info[3]
		
		# Empty lists
		self.williams = []
		self.sell = []
		self.buy = []
	
		# Call the calculation function
		self.calcInd()
	
	# This function calculates the williams indicator 
	def calcInd(self):
		
		# Calculates indicator for each stock in the list 
		for i in range(0,len(self.Symbol)-1,1):
			try:
				
				# Indicator calculation
				r = ((self.Whigh[i]-self.Cprice[i])/(self.Whigh[i]-self.Wlow[i])*-100)
				
				# Adds it to the list 
				self.williams.append(r)
			except ZeroDivisionError:
				 self.williams.append(float(0))
		
		# Calls the filter indicator function
		self.FilterInd()
	
	# Filter indicators that are within the threshold of selling and buying

	def FilterInd(self):
		
		# Goes through the list
		for i in range(0, len(self.williams),1):
			
			# Greater than -20 is within the threshold to sell 
			if self.williams[i] > -20:
				self.sell.append(self.Symbol[i])
			
			# Les than -80 is within the threshold to buy 
			if self.williams[i] < -80:
				self.buy.append(self.Symbol[i])
		# Prints the list
		print(self.sell, self.buy)



Williams()