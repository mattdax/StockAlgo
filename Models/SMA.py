import requests
import lxml.html as lh
import csv
from alpha_vantage.timeseries import TimeSeries
import os, inspect, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Scrapers import CurrentPriceScraper as CPS

class SMA():
	

	def __init__(self):
		self.stocks = ['NVDA']
		self.period = 20
		self.tpyicalP = []
		self.SMA = []
		self.info = [self.SMA,self.tpyicalP]
		self.loopLength = self.period * 24
		self.loopPull()

	
	# Loops which stock data is currently being pulled from 

	def loopPull(self):
		for i in range(0, len(self.stocks),1):
			self.temp = self.stocks[i]
			self.numTemp = i
			self.getInfo()
			self.pullData()
			self.tPrice()


	def getInfo(self):
		self.loopLength = self.period * 24
		ts = TimeSeries(key='IYH3P1ZXYWIFM33F',output_format='csv')
		# Get json object with the intraday data and another with  the call's metadata
		self.data, self.meta_data = ts.get_intraday(self.temp,interval = '60min',outputsize='full')
		self.reader = csv.reader(self.data,delimiter = ',')

	# Pulls the data from the internet per stock
	def pullData(self):
		
		self.tempTwo = []
		self.SMActr  = 0
		for row in self.data:
			self.tempthree = []
			if self.SMActr == self.loopLength:
				return
			try:
				self.tempthree.append(float(row[4]))
			except ValueError:
				pass
			self.SMActr += 1
			

		self.tempTwo.append(self.tempthree)
			

				
		self.calc()
	# Function that calculates SMA 
	def calc(self):
		
		SMAt = []
		print(len(self.tempTwo[0]))

		for i in range(0, self.loopLength,1):
			sum = 0
			for z in range(0, len(self.tempTwo[i]),1):
				sum+= float(self.tempTwo[z])
			
			SMAt.append(float(sum)/(float(self.period)))
		self.SMA.append(SMAt)
	
	def tPrice(self):
		
		self.typicalPriceLoopCounter = 0
		a = []
		for row in self.data:
			if self.typicalPriceLoopCounter == self.loopLength:
				return
			else:

				try:
					b = float(row[2]) + float(row[3]) + float(row[4])
					a.append(b/3)
					self.typicalPriceLoopCounter+= 1
				except ValueError:
					pass
		self.tpyicalP.append(a)
		print(self.tpyicalP)
				#print(self.tpyicalP)
				