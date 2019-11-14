"""
 TODO
- figure out how to call functions from different folders
-  comment
"""
import requests
import lxml.html as lh
def getprice(x):
	url = 'https://finance.yahoo.com/quote/'+ x + '/history?p='+ x +'&.tsrc=fin-srch'
	page = requests.get(url)
	#self.spLimit = 100
	# Store contents of website under doc
	doc = lh.fromstring(page.content)
	tr_elements = doc.xpath('//tbody')
	#print(tr_elements.text_content())
	return (float(tr_elements[0][0][4].text_content()))