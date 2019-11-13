import json

class JsonTesting():

	def __init__(self):
		self.main()
		self.write()
	def main(self):
		with open('accounts.json','r') as account:	
			words = (json.loads(account.read()))
		#print((words['stocks']))
		#words.close()
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
		with open('accounts.json',"r+") as account:
			words = json.loads(account.read())
			stock = json.loads(stock.read())
			json.dump(stock, words)
			#account.close()
		#print(words)
JsonTesting()