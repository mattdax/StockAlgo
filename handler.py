#from Scrapers import TrendingScraper as TS
import requests
import lxml.html as lh
from Models import Bollinger as Boll
#from Models import WilliamsInd as Will
from Models import change as Change
import time
class Handler():

	def __init__(self):
		
		self.Boll = Boll.Bollinger().streak
		self.Change = Change.Change().Prices
		print(self.boll, self.Change)

Handler()