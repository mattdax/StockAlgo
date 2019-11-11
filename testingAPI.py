from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import TrendingScraper as TS
import requests
import lxml.html as lh

class StockAPI():
	def __init__(self):
		self.Cprice = []
		self.Whigh = []
		self.Wlow = []
		self.symbols = TS.RiseScraper().symbols
		self.loopPull()
	def loopPull(self):
		self.ctr =0
		for i in range(0,len(self.symbols),1):
			self.ctr += 1
			self.pull()
		print(self.Cprice,self.Whigh,self.Wlow)
	def pull(self):

		#url =  'https://finance.yahoo.com/quote/%5EDJI/history?p=%5EDJI'
		url = 'https://finance.yahoo.com/quote/'+ self.symbols[self.ctr-1]+ '/history?p='+ self.symbols[self.ctr-1] +'&.tsrc=fin-srch'

		#Handle Page? handles contents of website?
		page = requests.get(url)
		#self.spLimit = 100
		# Store contents of website under doc
		doc = lh.fromstring(page.content)
		tr_elements = doc.xpath('//tbody')

		self.Cprice.append(tr_elements[0][0][4].text_content())
		self.Whigh.append(tr_elements[0][7][2].text_content())
		self.Wlow.append(tr_elements[0][7][3].text_content())

StockAPI()
		