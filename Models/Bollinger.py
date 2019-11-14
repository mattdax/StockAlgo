import SMA
# Import Statements
import SMA
import requests
import lxml.html as lh
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Scrapers import CurrentPriceScraper as CPS


class Bollinger():
	def __init__(self):
		self.stocks =['GE']
		
		# Gives the calculated list from SMA.py
		self.SMA = SMA.SMA().SMA

		self.bollinger = [[]]
		self.loopStock()
	def loopStock(self):
		for i in range(0, len(self.stocks),1):
			self.temp = self.stocks[i]
			self.typicalPrice()
			self.

	def typicalPrice(self):
		url = 'https://finance.yahoo.com/quote/'+ self.temp+ '/history?p='+ self.temp +'&.tsrc=fin-srch'
		#Handle Page? handles contents of website?
		page = requests.get(url)
		#self.spLimit = 100
		# Store contents of website under doc
		doc = lh.fromstring(page.content)
		self.tr_elements = doc.xpath('//tbody')

		high = float(self.tr_elements[0][0][1].text_content())
		low = float(self.tr_elements[0][0][2].text_content())
		cprice = float(CPS.getprice(self.temp))
		self.typicalP = int((high+low+cprice)/3)



Bollinger()