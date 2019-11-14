import requests
import lxml.html as lh
import os, inspect, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Scrapers import CurrentPriceScraper as CPS

class SMA():
	def __init__(self):
		self.stock = "GE"
		self.period = 50
		self.SMA = []
		self.pullData()
	def pullData(self):
		url = 'https://finance.yahoo.com/quote/'+ self.stock + '/history?p='+ self.stock +'&.tsrc=fin-srch'
		page = requests.get(url)
		

		doc = lh.fromstring(page.content)
		tr_elements = doc.xpath('//tbody')
		self.ctr = 0
		for i in range(0, self.period, 1):
			self.temp = []
			for x in range(0, self.period+self.ctr, 1):
				print(x+i)
				try:
					self.temp.append(tr_elements[0][x+i][4].text_content())
				except IndexError:
					#self.ctr += 1 
					pass
			self.calc()
	def calc(self):
		sum = 0
		for z in range(0, len(self.temp),1):
			sum += float(self.temp[z])
		self.SMA.append(int(sum)/int(self.period))

SMA()