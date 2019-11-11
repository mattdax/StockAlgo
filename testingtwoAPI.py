from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import TrendingScraper as TS
from time import sleep
import requests
import lxml.html as lh

class GetData():
	def __init__(self):

		
		self.symbols = TS.RiseScraper().symbols
		self.Wlow = []
		self.Whigh = []
		self.Cprice = []
		self.loopPull()
	def loopPull(self):
		self.ctr = -1
		for i in range(0, len(self.symbols),1):
			self.ctr += 1
			print(i)
			print(self.Wlow)
			sleep(10)
			self.pull()
		print(self.Wlow,self.Whigh,self.symbols)
	
	def pull(self):
		self.ts = TimeSeries(key='IYH3P1ZXYWIFM33F', output_format='pandas')
		Wdata, metadata = self.ts.get_weekly(symbol=str(self.symbols[self.ctr]))

		Cdata, Cmetadata = self.ts.get_intraday(symbol=self.symbols[self.ctr],interval='1min',outputsize='compact')

		Cprice = Cdata.iloc[0]
		self.Cprice.append(Cprice[3])
		Wlow = Wdata.iloc[4]
		self.Wlow.append(Wlow[2])
		Whigh =  Wdata.iloc[4]
		self.Whigh.append(Whigh[1])
GetData()

		

