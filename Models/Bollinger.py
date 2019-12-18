
# Import Statements

import requests
import lxml.html as lh
import sys, os, inspect
from alpha_vantage.techindicators import TechIndicators
import pandas

# Changes path to parent directory

######################
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
par_dir = os.path.dirname(current_dir)
sys.path.insert(0, par_dir)
#########################

import handler 
from Scrapers import TrendingScraper as TS
# Changes back to original folder
sys.path.insert(1, '/StockAlgo/Models')
#################


class Bollinger():
	def __init__(self):
		self.stocks = TS.RiseScraper().symbols
		self.deviationNum = [[]]
		self.loopStock()
		
	

	def loopStock(self):
		self.upper = []
		self.middle = []
		self.lower = []
		self.bollinger = []
		self.averages = []
		self.streak = []
		for i in range(0, len(self.stocks),1):
	
			self.temp = i 
			self.pull()
			self.calc()
			self.filter()
		print(self.streak)
	def pull(self):
		
		ti = TechIndicators(key='IYH3P1ZXYWIFM33F',output_format='pandas')
		data, meta_data = ti.get_bbands(symbol=self.stocks[self.temp], interval='60min',time_period=5)

		self.upper.append(data['Real Upper Band'].tolist())
		self.middle.append(data['Real Middle Band'].tolist())
		self.lower.append(data['Real Lower Band'].tolist())
	

	def calc(self):
		bollTemp = []
		for i in range(0, len(self.upper[self.temp]),1):
			bollTemp.append((self.upper[self.temp][i])-(self.lower[self.temp][i]))
		self.bollinger.append(bollTemp)
	
	def filter(self):
		self.sum = 0
		strk = 0
		end = 0
		print('here')
		for i in range(0, len(self.bollinger[self.temp])-1,1):
			if end == 3:
				break

			if self.bollinger[self.temp][i] <= self.bollinger[self.temp][i+1]:
				strk += 1 
			else: 
				try:
					if self.bollinger[self.temp][i] > self.bollinger[self.temp][i-1]:
						end += 1
				except IndexError:
					pass
		self.streak.append(strk)

Bollinger()