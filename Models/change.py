from alpha_vantage.timeseries import TimeSeries

class Change():
		
	def __init__(self):

		self.stocks = ['GOOG','GE'] 
		self.months= 2
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
		data, meta_data = ts.get_daily(symbol=self.stocks[self.temp], outputsize=self.months)
		print(data)
		self.Prices.append(data['4. close'].tolist())
Change()