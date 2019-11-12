"""
TODO

- cur price function added
- finish buy
- finish sell
- comment
"""

import sys 
import requests
import lxml.html as lh

sys.path.insert(1, '/StockAlgo/Scrapers') 

class Simulator():
	
	def __init__(self):
		self.Ssym = ['GE']
		self.Sprice = []
		self.Svolume = [6]
		self.loopPrice()

	def loopPrice(self):
		self.ctr = -1
		for i in range(0, len(self.Ssym),1):
			self.ctr += 1
			self.getPrice()
		self.buy()
		self.sell()

	def getPrice(self):
		

		url = 'https://finance.yahoo.com/quote/'+ self.Ssym[self.ctr] + '/history?p='+ self.Ssym[self.ctr] +'&.tsrc=fin-srch'
		page = requests.get(url)
		

		doc = lh.fromstring(page.content)
		tr_elements = doc.xpath('//tbody')
		
		self.Sprice.append(float(tr_elements[0][0][4].text_content())) 
	
	def buy(self):

		account = open('testfile.txt','w')
		for i in range(0, len(self.Sprice), 1):
			
			account.write(str(self.Ssym[i]+str(self.Sprice[i]*self.Svolume[i])))
		account.close()


	def sell(self):
		self.load = []
		with open('testfile.txt', 'r') as account:
			line = account.readline()
			self.load.append(line)
			while line:
				line = account.readline()
				self.load.append(line)


		print(self.load)
		account.close()
Simulator()