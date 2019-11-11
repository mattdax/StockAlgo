from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import TrendingScraper as TS
import requests
import lxml.html as lh

class StockAPI():
	def __init__(self):
		
		# Empty Variables
		self.Cprice = []
		self.WLT = []
		self.WHT = []
		self.Whigh = []
		self.Wlow = []
		self.daysBack = 14
		self.symbols = TS.RiseScraper().symbols
		
		self.loopPull()
		self.info = [self.Cprice, self.WHT, self.WLT, self.symbols]
	
	def loopPull(self):
		# 
		self.ctr =0
		for i in range(0,len(self.symbols),1):
			self.ctr += 1
			self.pull()
		self.removeExtra()
		

		return
		
	def pull(self):

		# URL used to search
		url = 'https://finance.yahoo.com/quote/'+ self.symbols[self.ctr-1]+ '/history?p='+ self.symbols[self.ctr-1] +'&.tsrc=fin-srch'

		#Handle Page? handles contents of website?
		page = requests.get(url)
		#self.spLimit = 100
		# Store contents of website under doc
		doc = lh.fromstring(page.content)
		self.tr_elements = doc.xpath('//tbody')

		# Adds Wlow, Whigh, Cprice from web data to list and converts to float
		try:
			self.Cprice.append(float(self.tr_elements[0][0][4].text_content()))
		except ValueError:
			self.Cprice.append(float((str(self.tr_elements[0][0][4].text_content()).replace(',', ''))))
		#self.Whigh.append(float(tr_elements[0][14][2].text_content()))
		#self.Wlow.append(float(tr_elements[0][14][3].text_content()))
		self.gethl()
	


	def gethl(self):

		

		#self.checkIndex()

		self.tempH = (0)
		self.tempL =float(str(self.tr_elements[0][0][3].text_content()).replace(',', ''))
		
		for i in range(0, self.daysBack, 1):
			try:
				if float(str(self.tr_elements[0][i][2].text_content()).replace(',', '')) >= float(self.tempH):
					self.tempH = str(self.tr_elements[0][i][2].text_content()).replace(',', '')
				if float(str(self.tr_elements[0][i][3].text_content()).replace(',', '')) <= float(self.tempL):
					self.tempL = str(self.tr_elements[0][i][3].text_content()).replace(',', '')
			except IndexError:
				self.daysBack += 1
				pass

			
			self.tempL = float(str(self.tempL))
			self.tempH = float(self.tempH)
			self.Whigh.append(self.tempH)
			self.Wlow.append(self.tempL)

	def removeExtra(self):
		self.WLT = []
		self.WHT = []
		for z in range(0, len(self.Whigh)-self.daysBack, int(self.daysBack)):
			self.WLT.append(self.Wlow[0+z])
			self.WHT.append(self.Whigh[0+z])
		print(self.WLT)
		self.Whigh = self.WHT
		self.Wlow = self.WLT

	def checkIndex(self):
		pass