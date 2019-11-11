from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import TrendingScraper as TS
import requests
import lxml.html as lh

class StockAPI():
	def __init__(self):
		
		# Empty Variables
		self.Cprice = []
		self.Whigh = []
		self.Wlow = []
		self.symbols = TS.RiseScraper().symbols
		self.loopPull()
	
	def loopPull(self):
		# 
		self.ctr =0
		for i in range(0,len(self.symbols),1):
			self.ctr += 1
			self.pull()

	def pull(self):

		# URL used to search
		url = 'https://finance.yahoo.com/quote/'+ self.symbols[self.ctr-1]+ '/history?p='+ self.symbols[self.ctr-1] +'&.tsrc=fin-srch'

		#Handle Page? handles contents of website?
		page = requests.get(url)
		#self.spLimit = 100
		# Store contents of website under doc
		doc = lh.fromstring(page.content)
		tr_elements = doc.xpath('//tbody')

		# Adds Wlow, Whigh, Cprice from web data to list and converts to float
		self.Cprice.append(float(tr_elements[0][0][4].text_content()))
		self.Whigh.append(float(tr_elements[0][7][2].text_content()))
		self.Wlow.append(float(tr_elements[0][7][3].text_content()))
StockAPI()
		