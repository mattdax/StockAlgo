import json
import csv
class JsonTesting():

	def __init__(self):
		self.main()
		#self.write()
	def main(self):
		"""
		with open('accounts.csv','a') as account:	
			# How to write 
			writer = csv.writer(account, delimiter= ',',quotechar = '"')
			s = ["TD",23,54,9]
			writer.writerow(s)
			
			"""
			"""
		with open('accounts.csv','r') as account:
			reader = csv.reader(account,delimiter = ',')
			for row in reader:
				print(row[0])
		
"""


	def write(self):
		sym = 'GE'
		Cprice = 33.3
		Bprice= 32.6
		volume= 8
		stock = {

		"Sym" : sym,
		
		"Bprice" : Bprice,
		
		"Vol" : volume,
		
		"Cprice" : Cprice
		}

		with open('accounts.json',"a+") as account:
			words = json.loads(account)
			entry = {}

			json.dump(stock, words)
			#account.close()
JsonTesting()