"""
TODO

- cur price function added
- finish buy
- finish sell
- comment
"""

# Import Statements
import sys 
import requests
import lxml.html as lh
import os, sys, inspect, csv
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import balance
from Scrapers import CurrentPriceScraper as CPS
# Change Path
sys.path.insert(1, '/StockAlgo/Scrapers') 


class Simulator():
	
	def __init__(self):
		# Stores stocks to be sold
		self.Ssym = ['GE']
		# Price of the strocks
		self.Sprice = []
		# Number of stocks to be sold/bought
		self.Svolume = [6]
		self.Cprice = []
		current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		self.parent_dir = os.path.dirname(current_dir)
		self.file = "\\Data\\accounts.csv"
		self.path = self.parent_dir+self.file
		self.loopPrice()

	def loopPrice(self):
		self.ctr = -1
		for i in range(0, len(self.Ssym),1):
			self.ctr += 1
			self.getPrice()
		self.getCprice()
		self.buy()
		self.sell()

	def getPrice(self):
		

		url = 'https://finance.yahoo.com/quote/'+ self.Ssym[self.ctr] + '/history?p='+ self.Ssym[self.ctr] +'&.tsrc=fin-srch'
		page = requests.get(url)
		

		doc = lh.fromstring(page.content)
		tr_elements = doc.xpath('//tbody')
		
		self.Sprice.append(float(tr_elements[0][0][4].text_content())) 

	# Function that adds current price of stock to a list. 
	def getCprice(self):
			for i in range(0, len(self.Ssym),1):
				self.Cprice.append(CPS.getprice(self.Ssym[i]))
	
	def buy(self):

		
		sys.path.insert(0, self.parent_dir) 
		
		

		for i in range(0, len(self.Sprice), 1):
			with  open(self.path,'a') as account:
				writer = csv.writer(account, delimiter= ',',quotechar = '"')
				s = [str(self.Ssym[i]),str(self.Sprice[i]),str(self.Cprice[i]),str(self.Svolume[i])]
				writer.writerow(s)
				balanceNew  = balance.Balance().balance
				d = int(self.Svolume[i])
				e = int(CPS.getprice(self.Ssym[i]))
				price  = int(balanceNew)-d-e
				(CPS.writeBalance((price)))



	def sell(self):
		# Stock to sell
		self.load = ['GE']
		self.SellSym = []
		self.SellVol = []


		# Removes stock that is being sold from csv
		#self.ctrTwo = -1
		if len(self.load) > 1:
			for i in range(0,len(self.load),1):
				with open(self.path, 'r') as inp, open(self.parent_dir+'\\Data\\accountsTmp.csv','a+') as out:
					#i = i -self.ctrTwo
					print(i)
					#i = i + 1
					writer = csv.writer(out)
					try:
						for row in csv.reader(inp, delimiter=','):
							if row[0] != str(self.load[0]):
								writer.writerow(row)
							else:
								self.SellVol.append(int(row[3]))
								self.SellSym.append(row[0])
				
					except IndexError:
						pass
					self.ctr -= 1
		else:
			with open(self.path, 'r') as inp, open(self.parent_dir+'\\Data\\accountsTmp.csv','a+') as out:
					#print(i)
					writer = csv.writer(out)
					try:
						for row in csv.reader(inp, delimiter=','):
							if row[0] != str(self.load[0]):
								
								writer.writerow(row)
							else:
								self.SellVol.append(int(row[3]))
								self.SellSym.append(row[0])
				
					except IndexError:
						pass


		# Eeases main CSV file 
		erase = open(self.path, 'a')
		erase.close()
		for i in range(0, len(self.SellVol),1):
			
			balanceNew  = balance.Balance().balance
			d = int(self.SellVol[i])
			e = int(CPS.getprice(self.SellSym[i]))
			price  = d + e + int(balanceNew)
			(CPS.writeBalance((price)))


			# Re writes to main from temp accounts pages
		data = self.parent_dir +'\\Data\\accountsTmp.csv'
		# Replaces csv file from temp
		with open(self.path, 'w') as account:
			writer = csv.writer(account, delimiter = ',',quotechar = '"')
			with open(data, 'r') as write:
				reader = csv.reader(write,delimiter = ',')
				for row in reader:
					writer.writerow(row)
Simulator()
