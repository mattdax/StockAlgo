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
		self.balanceInit = 10000
		self.balance = 10000
		self.stocksOwned = 0
		self.trades = 0
		self.stocks = ['GE', 'SLF']
		self.days = 60
		self.SecondLower = []
		self.SecondUpper = []
		self.position = []
		self.Change = Change.Change().Prices
		

		self.loopBollingerTwo()
		self.loopBacktrack()
		

		print(self.balance)

		print(self.trades)
		print(self.position)

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


	def loopBacktrack(self):
		for i in range(0, len(self.stocks),1):
			self.temp = i
			self.Analyze()
	
	def Analyze(self):
			self.sold = True
			self.balTemp = self.balance * 0.20
			self.SellStrk = 0
			self.BuyStrk = 0
			self.balance = 10000
			self.stocksOwned = 0

			for i in range(len(self.Change[self.temp])-1,0,-1):

				# Hold 
				if self.Change[self.temp][i] <= self.SecondUpper[self.temp][i] and self.Change[self.temp][i] >= self.SecondLower[self.temp][i]:
					pass

				if self.Change[self.temp][i] > self.SecondUpper[self.temp][i]:
					self.BuyStrk += 1
					#if self.stocksOwn < 4 and self.Change[self.temp][i+1] > self.SecondUpper[self.temp][i+1]:
					if self.sold == True or self.BuyStrk == 2:
						self.BuyStrk = 0
						self.sold = False
						self.trades += 1
						

						self.stocksOwned += (self.balTemp//self.Change[self.temp][i])
						
						self.balance -= (self.Change[self.temp][i]) * (self.balTemp//self.Change[self.temp][i])
				else:
					if SellStrk == 1:
						self.SellStrk += 1
					if self.stocksOwned > 0 and self.SellStrk == 2:
						self.SellStrk = 0
						self.trades += 1
						self.stocksOwned -= self.stocksOwned
						self.balance += (self.Change[self.temp][i]) * (self.balTemp//self.Change[self.temp][i])
						self.sold = True

			self.balanceNew = self.balance + self.stocksOwned * self.Change[self.temp][0]
			print("Final Balance: "+ str(self.balanceNew))
			print("Trades Made: " + str(self.trades))

			if self.balanceNew > self.balanceInit:
				self.position.append(round(self.balanceNew/self.balanceInit,3))
			else:
				self.position.append(0)
			
Handler()	