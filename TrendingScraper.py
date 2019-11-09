
"""" 
Todo:

- git REPO
- update channel



"""
# Imports
import requests
import lxml.html as lh # What is this
import pandas as pd



class RiseScraper():
	
	def __init__(self):

		# Store URL
		url =' https://finance.yahoo.com/gainers'

		#Handle Page? handles contents of website?
		page = requests.get(url)

		# Store contents of website under doc
		doc = lh.fromstring(page.content)
		self.tr_elements = doc.xpath('//tr')
		self.toList()
	

	# This function converts needed information from html file to 3 lists
	def toList(self):

		self.change = []
		self.price = []
		self.symbols = []

		for t in self.tr_elements:
			break


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
		print(self.symbols)


		# Loop that stores price in a list
		for i in range(1, len(self.tr_elements),1):
			for	t in self.tr_elements[i]:
				name=t.text_content()
				col.append((name))
								# '2' = price
			self.price.append(col[2])
			col=[]
		print(self.price)

		# Loop for saving % change in a list
		for i in range(1, len(self.tr_elements),1):
			for	t in self.tr_elements[i]:
				name=t.text_content()
				col.append((name))
									#'4' = %change
			self.change.append(col[4])
			col=[]
		print(self.change)



RiseScraper()