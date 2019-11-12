"""
TODO

- cur price function added
- finish buy
- finish sell
- comment
"""

import sys 
sys.path.insert(1, '/StockAlgo/Scrapers') 

class Simulator():
	
	def __init__(self):
		self.Ssym = []
		self.Sprice = []
		self.Svolume = []

	def loopPrice(self):
		self.ctr = -1
		for i in range(0, len(self.Sprice),1)
			self
			self.getPrice()

	def getPrice(self):
		url = 'https://finance.yahoo.com/quote/'+ x + '/history?p='+ x +'&.tsrc=fin-srch'
		page = requests.get(url)
		

		doc = lh.fromstring(page.content)
		tr_elements = doc.xpath('//tbody')
		
		return (float(tr_elements[0][0][4].text_content()))
	def buy(self):
		account = open('testfile.txt','w')
		for i in range(0, len(self.Sprice), 1):
			
			account.write(str(self.symbol)+str(self.Sprice*self.Svolume))
		account.close()
