 
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

	def toFloat(self):
		self.nPrice = []
		self.nSymbol = []
		for i in range(0, len(self.price)-(self.ctr),1):
			try:
				float(self.price[i])
			except (ValueError):
				self.price.remove(self.price[i])
				self.ctr += 1
				#self.toFloat()

			self.nPrice.append(float(self.price[i]))
			self.nSymbol.append(self.symbols[i])


	def filterPrice(self):	
		self.nPrice = []
		self.nSymbol = []
		for i in range(0,len(self.price),1):
			
			if self.price[i] <= float(self.spLimit/10):
				self.nPrice.append(self.price[i])
				self.nSymbol.append(self.symbols[i])
