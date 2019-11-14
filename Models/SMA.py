import requests
import lxml.html as lh
import os, inspect, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Scrapers import CurrentPriceScraper as CPS

class SMA():
	def __init__(self):
		self.stocks = ['GE']
		self.period = 50
		self.SMA = [[]]
		self.loopPull()
	
	# Loops which stock data is currently being pulled from 
	def loopPull(self):
		for i in range(0, len(self.stocks),1):
			self.temp = self.stocks[i]
			self.numTemp = i
			self.pullData()

	# Pulls the data from the internet per stock
	def pullData(self):
		url = 'https://finance.yahoo.com/quote/'+ self.temp + '/history?p='+ self.temp +'&.tsrc=fin-srch'
		page = requests.get(url)
		

		doc = lh.fromstring(page.content)
		tr_elements = doc.xpath('//tbody')
		
		for i in range(0, self.period, 1):
			self.tempTwo = []
			for x in range(0, self.period, 1):
				try:
					self.tempTwo.append(tr_elements[0][x+i][4].text_content())
				except IndexError:
					pass
			self.calc()
	# Function that calculates SMA 
	def calc(self):
		sum = 0
		for z in range(0, len(self.tempTwo),1):
			sum += float(self.tempTwo[z])

		self.SMA[self.numTemp].append(int(sum)/int(self.period))
		