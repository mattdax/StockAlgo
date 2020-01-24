#from Scrapers import TrendingScraper as TS
import requests
import lxml.html as lh
from Models import Bollinger as Boll
#from Models import WilliamsInd as Will
from Models import change as Change
from alpha_vantage.techindicators import TechIndicators
import time
class Handler():

	def __init__(self):
		

		self.stocks = ['GOOG', 'GE']
		self.days = 60
		self.Bollinger  = Boll.Bollinger().bollinger
		self.BollUpper = self.Bollinger[0]
		self.BollLower = self.Bollinger[1]
		self.SecondLower = []
		self.SecondUpper = []
		self.Change = Change.Change().Prices
		
		self.loopBollingerTwo()
		print(self.BollUpper[0][0], self.Change[0][0])
		self.testFunc()
	def loopBollingerTwo(self):
		
		for i in range(0, len(self.stocks),1):
			self.temp = i
			self.pull()
	def pull(self):
		ti = TechIndicators(key='XP9KDY0X1E13B4HN',output_format='pandas')	
	
		# 	Pulls Bollinger Bands  -	symbol = current symbol, interval = Time between data points, time_period = number of data points
		data, meta_data = ti.get_bbands(symbol= self.stocks[self.temp], interval='daily',time_period= 20, nbdevup = 1, nbdevdn = 1)
		

		# Appends data points of current stock to 
		self.SecondUpper.append(data['Real Upper Band'].tolist())
		self.SecondLower.append(data['Real Lower Band'].tolist())
	def testFunc(self):
		for i in range(0, len(self.Change[0]),1):
			if self.Change[0][i] <= self.SecondUpper[1][i] and self.Change[1][i] >= self.SecondLower[1][i]:
				print("Hold/Nothing")
			if self.Change[1][i] > self.SecondUpper[1][i]:
				print("Buy")
			else:
				print("Sell")
Handler()