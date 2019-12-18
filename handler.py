from Scrapers import TrendingScraper as TS
import requests
import lxml.html as lh
from Models import Bollinger as Boll
from Models import WilliamsInd as Will
class Handler():

	def __init__(self):
		print('1')
		#self.symbols = TS.RiseScraper().symbols

		self.prices = []
		print(self.symbols)
		print('2')
		self.loopPrice()
		print(self.prices)

# Check Stocks amongst indicators
	
	# 
	def check(self):
		self.boll = Boll.Bollinger().Bollinger
		self.Will = Will.Williams().williams
		print(self.boll, self.Will)

Handler()