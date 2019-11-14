"""
 TODO
- figure out how to call functions from different folders
-  comment
"""
# Import Statements
import requests
import lxml.html as lh
import os, sys, inspect
import csv
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import balance


# Function gets the price of any stock 
def getprice(x):
	
	# Calculates the url and pulls its data
	url = 'https://finance.yahoo.com/quote/'+ x + '/history?p='+ x +'&.tsrc=fin-srch'
	page = requests.get(url)
	
	# Store contents of website under doc
	doc = lh.fromstring(page.content)
	tr_elements = doc.xpath('//tbody')
	
	# Returns the current price
	return (float(tr_elements[0][0][4].text_content()))


# Function that writes the new current balance in balancs.csv
def writeBalance(x):
	
	# Change path directory
	current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	parent_dir = os.path.dirname(current_dir)
	sys.path.insert(0, parent_dir) 
	
	# Opens and reads current balance
	with open(parent_dir+'\\Data\\balance.csv', 'r') as ebalance:
		z = csv.reader(ebalance, delimiter=',')
		nbalance = (next(z))[0]
	
	# Adds balance to new balalnce
	newbalance = int(nbalance) + int(x)
	
	print(newbalance)
	
	# Deletes the file 
	open(parent_dir+'\\Data\\balance.csv', 'w')


	# Recreates the file with the new data
	with open(parent_dir+'\\Data\\balance.csv','a+') as mbalance:
		writer = csv.writer(mbalance, delimiter = ',')
		writer.writerow([newbalance,])
