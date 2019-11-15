import requests
import lxml.html as lh
import os, inspect, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Scrapers import CurrentPriceScraper as CPS

class SMA():
	def __init__(self):
		self.stocks = ['NVDA']
		self.period = 5
		self.tpyicalP = [[]]
		self.SMA = []
		self.info = [self.SMA,self.tpyicalP]
		self.loopPull()
	
	# Loops which stock data is currently being pulled from 
	def loopPull(self):
		for i in range(0, len(self.stocks),1):
			self.temp = self.stocks[i]
			self.numTemp = i
			self.pullData()
			self.tPrice()

	# Pulls the data from the internet per stock
	def pullData(self):
		url = 'https://finance.yahoo.com/quote/'+ self.temp + '/history?p='+ self.temp +'&.tsrc=fin-srch'
		page = requests.get(url)
		

		doc = lh.fromstring(page.content)
		self.tr_elements = doc.xpath('//tbody')
		
		
		self.tempTwo = [[]]
		self.i = 0
		for i in range(0, self.period, 1):
			sum = 0

			for x in range(self.i, (self.period+self.i), 1):
				self.tempthree = []
				try:
					self.tempthree.append(self.tr_elements[0][x][4].text_content())
					self.tempTwo.append(self.tempthree)
				except IndexError:
					self.tempTwo.append[i](self.tr_elements[0][x+1][4].text_content())
					self.i += 1 
				self.i += 1

				
		self.calc()
	# Function that calculates SMA 
	def calc(self):
		
		SMAt = []
		print(self.tempTwo)
		print()
		for i in range(0, (self.period),1):
			sum = 0
		
			for z in range(0, len(self.tempTwo),1):
				sum+= float(self.tempTwo[i][z])
			SMAt.append(float(sum)/(float(self.period)))
		self.SMA.append(SMAt)
		
	def tPrice(self):
		self.i = 0
		for i in range(0, self.period,1):
			try:
				high = float(self.tr_elements[0][i][1].text_content())
				low = float(self.tr_elements[0][i][2].text_content())
			except ValueError:
				high = float(self.tr_elements[0][i+1][1].text_content())
				low = float(self.tr_elements[0][i+1][2].text_content())
				self.i += 1 
			except IndexError:
				print(self.i+1)
				high = float(self.tr_elements[0][self.i+1][1].text_content())
				low = float(self.tr_elements[0][self.i+1][2].text_content())
				self.i += 1 
			cprice = float(CPS.getprice(self.stocks[self.numTemp]))
			self.tpyicalP[self.numTemp].append((float(high+low+cprice)/float(3)))
			