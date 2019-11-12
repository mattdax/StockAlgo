"""
TODO

- Comment
- figure out why all symbols are not being taken
"""
import API

class Williams():
	
	def __init__(self):
		self.info = API.StockAPI().info
		self.Cprice = self.info[0]
		self.Whigh = self.info[1]
		self.Wlow = self.info[2]
		self.Symbol = self.info[3]
		print(self.Symbol)
		print(self.Cprice)
		print(len(self.Whigh))
		print(self.Wlow)
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