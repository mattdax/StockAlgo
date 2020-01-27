from alpha_vantage.timeseries import TimeSeries
import sys, inspect, os
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
par_dir = os.path.dirname(current_dir)
sys.path.insert(0, par_dir)

from Data import Config


class Change():
		
	def __init__(self):
		self.Config = Config.Config().Config
		self.stocks = self.Config[0]
		#self.days = 60 
		self.Prices = []
		self.loopStocks()
		
	def loopStocks(self):

		
		
		for i in range(0,len(self.stocks),1):

			self.temp = i
			self.pull()
	def pull (self):
		#ts = TimeSeries(key='XP9KDY0X1E13B4HN',output_format='pandas')
		#data , metadata = ts.get_daily(self.stocks[self.temp])
		
		ts = TimeSeries(key='XP9KDY0X1E13B4HN', output_format='pandas')
		data, meta_data = ts.get_daily(symbol=self.stocks[self.temp],  outputsize='compact')
		data = data['4. close'].tolist()
		data = data
		self.Prices.append(data)
