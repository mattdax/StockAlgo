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
		self.bollinger = [[]]
		self.deviationNum = [[]]
		self.loopStock()
	def loopStock(self):
		for i in range(0, len(self.stocks),1):
			#self.temp = self.stocks[i]
			self.temp = i 
			self.deviation()
			self.calc()

		print(self.bollinger)
	def deviation(self):
		
		sum = 0
		for x in range(0,len(self.typicalPrice[self.temp]),1):
			sum += self.typicalPrice[self.temp][x]
		sum = (sum/len(self.typicalPrice[self.temp]))
		for x in range(0, len(self.typicalPrice[self.temp]),1):
			self.typicalPrice[self.temp][x] = int(self.typicalPrice[self.temp][x]) - int(sum)
		for x in range(0, len(self.typicalPrice[self.temp]),1):
			self.typicalPrice[self.temp][x] = self.typicalPrice[self.temp][x] ** 2
		sum = 0 
		for x in range(0, len(self.typicalPrice[self.temp]),1):
			sum += self.typicalPrice[self.temp][x]
		self.deviationNum = ((sum/len(self.typicalPrice[self.temp][x])) ** 0.5)*2
	def calc(self):
		upper = []
		lower = []
		for x in range(0,len(self.typicalPrice[self.temp]),1):
			upper.append((int(self.SMA[self.temp][x])*int(self.typicalPrice[self.temp][x]))+int(self.deviationNum))
			lower.append((int(self.SMA[self.temp][x])*int(self.typicalPrice[self.temp][x]))-int(self.deviationNum))
		for i in range(0,len(upper),1):
			self.bollinger.append(upper[i]-lower[i])
Bollinger()

