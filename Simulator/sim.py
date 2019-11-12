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
import os, sys, inspect

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

		current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		parent_dir = os.path.dirname(current_dir)
		sys.path.insert(0, parent_dir) 
		
		file = "\\Data\\accounts.txt"
		self.path = parent_dir+file

		account = open(self.path,'w')
		for i in range(0, len(self.Sprice), 1):
			
			account.write(str(self.Ssym[i]+str(self.Sprice[i])+":"+str(self.Svolume[i])))
		account.close()


	def sell(self):
		self.load = []
		self.toSell = ['GE']
		
		with open(self.path, 'r') as account:
			line = account.readline()
			self.load.append(line)
			while line:
				line = account.readline()
				self.load.append(line)
			account.close()
		with open(self.path ,'r+') as delete:
			d = delete.readlines()
			delete.seek(0)
			for i in d:
				if i[0:2] != (self.toSell[0])[0:2]:
					delete.write(i)
			delete.truncate()

		print(self.load)
		account.close()
Simulator().buy()