from Scrapers import TrendingScraper as TS
import requests
import lxml.html as lh
from Models import Bollinger as Boll
from Models import WilliamsInd as Will
import time
class Handler():

	def __init__(self):
		self.timec = time.time()
		#self.symbols = TS.RiseScraper().symbols

		self.prices = []
		#print(self.symbols)
		print('2')
		#self.loopPrice()
		print(self.prices)
		self.check(  )
# Check Stocks amongst indicators
	
	# 
	def check(self):
		self.boll = Boll.Bollinger().streak
		
		print(self.timec - time.time())


		self.Will = Will.Williams().williams
		print(self.boll, self.Will)

Handler()