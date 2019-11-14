"""
 TODO
- figure out how to call functions from different folders
-  comment
"""
import requests
import lxml.html as lh
import os, sys, inspect
import csv
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import balance

def getprice(x):
	url = 'https://finance.yahoo.com/quote/'+ x + '/history?p='+ x +'&.tsrc=fin-srch'
	page = requests.get(url)
	#self.spLimit = 100
	# Store contents of website under doc
	doc = lh.fromstring(page.content)
	tr_elements = doc.xpath('//tbody')
	#print(tr_elements.text_content())
	return (float(tr_elements[0][0][4].text_content()))

def writeBalance(x):
	
	current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	parent_dir = os.path.dirname(current_dir)
	sys.path.insert(0, parent_dir) 
	
	with open(parent_dir+'\\Data\\balance.csv', 'r') as ebalance:
		z = csv.reader(ebalance, delimiter=',')
		for row in ebalance:
			nbalance = row
			print(nbalance)
	
	newbalance = int(nbalance) + int(x)
	
	print(newbalance)
	# Deletes the file 
	open(parent_dir+'\\Data\\balance.csv', 'w')


	# Recreates the file with the new data
	with open(parent_dir+'\\Data\\balance.csv','a+') as mbalance:
		writer = csv.writer(mbalance, delimiter = ',')
		writer.writerow([newbalance])
