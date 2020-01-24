
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

#import handler 
#from Scrapers import TrendingScraper as TS
# Changes back to original folder
sys.path.insert(1, '/StockAlgo/Models')
#################


class Bollinger():
	def __init__(self):
		
		# Loads Gainer list
		self.stocks = ['GOOG', 'GE']
		self.days = 60
		
			# Cuts off top 30 - Due to Alpha Vantage limit
		
		#self.stocks = self.stocks[0:29]
		
		# Loop Call
		self.loopStock()
		
	

	def loopStock(self):
		
		# Define Variables
		self.upper = []
		self.middle = []
		self.lower = []
		self.bollinger = [self.upper, self.lower]
		self.averages = []
		self.streak = []

		# Loop for length of stocks
		for i in range(0, len(self.stocks),1):
			# FIGURE OUT WHAT THIS DOES
			self.temp = i 
			self.pull()
			#self.calc()
			#self.filter() ---------- Removed for now
			

	def pull(self):
		# 	Load Indicator
		ti = TechIndicators(key='XP9KDY0X1E13B4HN',output_format='pandas')
		
	
		# 	Pulls Bollinger Bands  -	symbol = current symbol, interval = Time between data points, time_period = number of data points
		data, meta_data = ti.get_bbands(symbol= self.stocks[self.temp], interval='daily',time_period= 20)
		
		# Not used atm
		#################
		self.middle.append(data['Real Middle Band'].tolist())
		##################

		# Appends data points of current stock to 
		self.upper.append(data['Real Upper Band'].tolist())
		self.lower.append(data['Real Lower Band'].tolist())
	
"""
	def calc(self):
		bollTemp = []
		
		for i in range(0, len(self.upper[self.temp]),1):
			bollTemp.append(round((self.upper[self.temp][i])-(self.lower[self.temp][i]),2))
		bollTemp = bollTemp[:]
		self.bollinger.append(bollTemp)
		"""