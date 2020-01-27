class Config():
	def __init__(self):


		# General Backtrack Config
		self.StockstoBacktrack = ['GE']			#	 0
		self.BacktrackDays = 60							# 	 1
		self.BacktrackBalance = 10000					# 	 2


		# Double Bollinger Config
		self.DoubleBollingerPrecentToInvest = 0.2		#	 0
		self.BuyStreak = 3								#    1 
		self.SellStreak  = 2							#	 2
		

		self.Config = [self.StockstoBacktrack, self.BacktrackDays, self.BacktrackBalance]

		self.DoubleBollinger = [self.DoubleBollingerPrecentToInvest, self.BuyStreak, self.SellStreak]
