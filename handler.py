#from Scrapers import TrendingScraper as TS
import requests
import lxml.html as lh
from Models import Bollinger as Boll
#from Models import WilliamsInd as Will
from Models import change as Change
import time
class Handler():

	def __init__(self):
		
		self.BollChange = []
		self.PChange = []

		self.Boll = Boll.Bollinger().bollinger
		
		self.Change = Change.Change().Prices
		
		self.loopConvert()
		print(self.BollChange,self.PChange)
	
	def loopConvert(self):
		
		
		if len(self.Boll) != len(self.Change):
			raise TypeError

		for i in range(0, len(self.Boll), 1):
			self.temp = i
			self.ConvertBollinger()


	def ConvertBollinger(self):
		BollChange = []
		PChange = []


		for i in range(1, len(self.Boll[self.temp]),1):
			
			BollChange.append(round(((self.Boll[self.temp][i]-self.Boll[self.temp][i-1])/abs(self.Boll[self.temp][i-1])*-100),2))
			PChange.append(round(((self.Change[self.temp][i]-self.Change[self.temp][i-1])/abs(self.Change[self.temp][i-1])*-100),2))
		self.BollChange.append(BollChange)
		self.PChange.append(PChange)

		c = 0
		for i in range(0, 3, 1):
			c += PChange[i]
		print(c/3)
"""

	- Average Pchange <---- recent and past

		- all 60 days
		- 30
		- 7 
		- 3 

	- If Boll change is pos 

	- Average Boll change <-----


"""


Handler()