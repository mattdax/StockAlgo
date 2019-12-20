 
"""
 - Finish comments
 - Clean up
 - add redundency
 - Create new list with different stock names
"""

# Imports
import requests
import lxml.html as lh # What is this
import pandas as pd
import os, sys, inspect
from alpha_vantage.techindicators import TechIndicators
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import balance



"""
CLASS PURPOSE:

Pulls stock symbols from Yahoo and filters out stock by price of funds available. 
"""
class RiseScraper():
	
	def __init__(self):

		# Store URL
		url =' https://finance.yahoo.com/gainers'

		#Handle Page? handles contents of website?
		page = requests.get(url)
		self.spLimit = balance.Balance().balance

		
		# Store contents of website under doc
		doc = lh.fromstring(page.content)
		self.tr_elements = doc.xpath('//tr')
		self.toList()
		
	# This function converts needed information from html file to 3 lists
	def toList(self):

		# Empty
		self.price = []
		self.symbols = []

		#Create empty list
		col=[]
		i=0	
		# Loop that stores symbols in a list
		for i in range(1, len(self.tr_elements),1):
			for	t in self.tr_elements[i]:
				name=t.text_content()
				col.append((name))
			self.symbols.append(col[0])
			col=[]


		# Loop that stores price in a list
		for i in range(1, len(self.tr_elements),1):
			for	t in self.tr_elements[i]:
				name=t.text_content()
				col.append((name))
								# '2' = price
			self.price.append(col[2])
			col=[]

		self.ctr = 2
		# Converts dats in lists to float
		self.toFloat()
		self.price = self.nPrice
		self.symbols = self.nSymbol
		
		# Filter's out the set price of funds available
		self.filterPrice()
		self.price = self.nPrice
		self.symbols = self.nSymbol
		self.filterPriceTwo()
		self.filterPriceThree()

	"""
	
	Fucntion: toFloat

	Purpose:

		- removes stocks that cannot be converted from flaot 
		- converts prices from string to float that have been pulled from online

	Editing:

		- no real editing shoud occur here

	"""

	
	def toFloat(self):
		self.nPrice = []
		self.nSymbol = []
		for i in range(0, len(self.price)-(self.ctr),1):
			try:
				float(self.price[i])
			except (ValueError):
				self.price.remove(self.price[i])
				self.ctr += 1

			self.nPrice.append(float(self.price[i]))
			self.nSymbol.append(self.symbols[i])
	"""
	Function: Filter Price 

	Purpose:
	- Removes stocks that I cannot buy at least 10 of
		- No point in buying any stocks that I can only buy a few of, will not be very profitable 

	Editing:
	
	- Can be changed in float(self.spLimit/x) --- Change x
	"""
	def filterPrice(self):
		self.nPrice = []
		self.nSymbol = []
		for i in range(0,len(self.price),1):
			if self.price[i] <= float(self.spLimit/10):
				self.nPrice.append(self.price[i])
				self.nSymbol.append(self.symbols[i])

	"""
	Function: Filter Price Two

	Purpose:
			- Removes penny stocks from the initial list

				- Sometimes cheaper stocks are not supported by alpha vantage
	Editing:

			- Change float(x) --- in the if statement to change the least price
	"""

	def filterPriceTwo(self):
		self.ctrtwo = 1
		for i in range(0, len(self.price)-(self.ctrtwo),1):
			

			if float(self.price[i]) < float(1):
				
				self.price.pop(i)
				self.symbols.pop(i)
				self.ctrtwo += 1

	"""
	Function: Filter Price Three

	Purpose:
		- Removes stocks that give errors when used in Alpha Vantage
			- Most likely means they are not supported
	Editing:

		- No real editing should occur here

	"""


	def filterPriceThree(self):
		ti = TechIndicators(key='XP9KDY0X1E13B4HN',output_format='pandas')
		self.ctrtwo = 2
		
		for i in range(0, len(self.symbols)-(self.ctrtwo),1):
			
			if i >= len(self.symbols):
				break
			try:
				data, meta_data = ti.get_bbands(symbol= self.symbols[i], interval='60min',time_period= 5)
			except ValueError:
				self.symbols.pop(i)
				self.price.pop(i)
				self.ctrtwo += 1
		print(self.symbols)
