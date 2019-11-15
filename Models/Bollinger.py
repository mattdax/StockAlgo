import SMA
# Import Statements
import SMA
import requests
import lxml.html as lh
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Scrapers import CurrentPriceScraper as CPS


class Bollinger():
	def __init__(self):
		self.stocks =['GE']
		
		# Gives the calculated list from SMA.py
		self.info = SMA.SMA().info
		self.SMA = self.info[0]
		self.typicalPrice = self.info[1]
		self.bollinger = []
		self.deviationNum = [[]]
		self.loopStock()
		
	def loopStock(self):
		
		for i in range(0, len(self.stocks),1):
			#self.temp = self.stocks[i]

			self.temp = i 
			self.newSMA()
			self.deviation()
			self.calc()
		print(self.upper)
		print(self.lower)
		print(self.SMA)
		print(self.bollinger)
		#	print(self.typicalPrice)
		
	def newSMA(self):
		for i in range(0, len(self.SMA),1):
			self.SMA[self.temp][i] = self.SMA[self.temp][i] * self.typicalPrice[self.temp][i]
	def deviation(self):
		
		sum = 0
		
		for x in range(0,len(self.typicalPrice[self.temp]),1):
			sum += self.typicalPrice[self.temp][x]
		sum = (sum/len(self.typicalPrice[self.temp]))
		
		for x in range(0, len(self.typicalPrice[self.temp]),1):
			self.typicalPrice[self.temp][x] = (self.typicalPrice[self.temp][x]) - (sum)
		
		for x in range(0, len(self.typicalPrice[self.temp]),1):
			self.typicalPrice[self.temp][x] = self.typicalPrice[self.temp][x] ** 2
		sum = 0 
		
		for x in range(0, len(self.typicalPrice[self.temp]),1):
			sum += self.typicalPrice[self.temp][x]
		self.deviationNum = ((sum/len(self.typicalPrice[self.temp])) ** 0.5)*2
	

	def calc(self):
		self.upper = []
		self.lower = []
		#print(self.SMA)
		for x in range(0,len(self.typicalPrice[self.temp]),1):
			self.upper.append(((self.SMA[self.temp][x]))+(self.deviationNum))
			self.lower.append(((self.SMA[self.temp][x]))-(self.deviationNum))
		self.filter()


		#for i in range(0,len(self.upper),1):
	
		#	self.bollinger.append(self.upper[i]-self.lower[i])
	def filter(self):
		
		for x in range(0,len(self.upper),1):
				
			temp = []
			
			temp.append(float(self.upper[x])-float(self.SMA[self.temp][x])+float(self.SMA[self.temp][x])-float(self.lower[x]))
			self.bollinger.append(temp)
		
Bollinger()

