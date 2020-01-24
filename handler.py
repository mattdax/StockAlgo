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
		
		self.balance = 0
		self.stocksOwn = 0
		self.trades = 0
		self.stocks = ['GOOG', 'TEAM']
		self.recommend = []
		self.days = 60
		self.Bollinger  = Boll.Bollinger().bollinger
		self.BollUpper = self.Bollinger[0]
		self.BollLower = self.Bollinger[1]
		self.SecondLower = []
		self.SecondUpper = []
		self.Change = Change.Change().Prices
		self.loopBollingerTwo()
		self.testFunc()
		print(self.balance)
		print(self.stocksOwn)
		print(self.trades)

		#self.Analyze()
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
		#for i in range(0, len(self.stocks),1):
			self.temp = 1
			self.Analyze()
			print(len(self.Change[self.temp]),len(self.SecondUpper[self.temp]))
	def Analyze(self):
			print(len(self.Change[self.temp]),len(self.SecondUpper[self.temp]))
			for i in range(len(self.SecondUpper[self.temp])-1,0,-1):
				
				if self.Change[self.temp][i] <= self.SecondUpper[self.temp][i] and self.Change[self.temp][i] >= self.SecondLower[self.temp][i]:
					pass
				if self.Change[self.temp][i] > self.SecondUpper[self.temp][i]:
					if self.stocksOwn < 4:
						self.trades += 1
						self.stocksOwn += 1
						self.balance -= self.Change[self.temp][i]
				else:
					if self.stocksOwn > 0:
						self.trades += 1
						self.stocksOwn -= 1
						self.balance += self.Change[self.temp][i]



Handler()