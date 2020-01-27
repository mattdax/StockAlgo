#from Scrapers import TrendingScraper as TS
import requests
import lxml.html as lh
from Models import Bollinger as Boll

from Data import Config

from Models import change as Change
from alpha_vantage.techindicators import TechIndicators
import time
class DoubleBollingerBacktrack():

	def __init__(self, config):
		self.Config = Config.Config().Config
		self.DoubleBollinger = config

		self.balanceInit = self.Config[2]
		self.balance = self.Config[2]
		self.stocksOwned = 0
		self.trades = 0
		self.stocks = self.Config[0]
		self.days = self.Config[1]
		self.SecondLower = []
		self.SecondUpper = []
		self.position = []
		self.Change = Change.Change().Prices
		
		print("Here 1")
		self.loopBollingerTwo()
		self.loopBacktrack()
		

		print(self.position)
	def __repr__(self):
		return str(self.position[0])
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
			self.balTemp = self.balance * self.DoubleBollinger[0]
			self.SellStrk = 0
			self.BuyStrk = 0
			self.balance = self.Config[2]
			self.stocksOwned = 0

			for i in range(len(self.Change[self.temp])-1,0,-1):

				# Hold 
				if self.Change[self.temp][i] <= self.SecondUpper[self.temp][i] and self.Change[self.temp][i] >= self.SecondLower[self.temp][i]:
					pass

				if self.Change[self.temp][i] > self.SecondUpper[self.temp][i]:
					self.BuyStrk += 1
					#if self.stocksOwn < 4 and self.Change[self.temp][i+1] > self.SecondUpper[self.temp][i+1]:
					if self.sold == True or self.BuyStrk == self.DoubleBollinger[1]:
						self.BuyStrk = 0
						self.sold = False
						self.trades += 1
						

						self.stocksOwned += (self.balTemp//self.Change[self.temp][i])
						
						self.balance -= (self.Change[self.temp][i]) * (self.balTemp//self.Change[self.temp][i])
				else:
					self.SellStrk += 1
					#if self.stocksOwned > 0 and self.SellStrk == 2:
					if self.stocksOwned > 0 and self.SellStrk == self.DoubleBollinger[2]:
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

class DoubleBollingerOptimize():
	def __init__(self):
		self.Config = Config.Config().Config
		self.DoubleBollinger = Config.Config().DoubleBollinger
		self.DoubleBollingerPrecentToInvest = 0.1	
		self.BuyStreak = 2				
		self.SellStreak  = 2
		#self.InitialPosition = float(DoubleBollingerBacktrack())
		self.AllResults = []
		#self.pack = [self.DoubleBollingerPrecentToInvest, self.BuyStreak, self.SellStreak]

		#self.AllResults.append(self.InitialPosition)
		self.Optimize()
	def Optimize(self):
		for i in range(0,5,1):
			for x in range(0,3,1):
				self.SellStreak = 2
				for z in range(0,3,1):
					if self.SellStreak > 5:
						break
					time.sleep(5)
					self.SellStreak += 1
					self.pack = [self.DoubleBollingerPrecentToInvest, self.BuyStreak, self.SellStreak]
					print(self.pack)
					temp = DoubleBollingerBacktrack(self.pack)
					
					self.AllResults.append(temp)
				
				self.BuyStreak += 1
			self.BuyStreak = 2
			self.DoubleBollingerPrecentToInvest += 0.1
		print(self.AllResults)

DoubleBollingerOptimize()	