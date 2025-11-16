class Bankacc():
	def __init__(self,owner,bl=0):
		self.balance=bl
		self.owner=owner

	def Deposit(self,amount):
		print("current balance is:",self.balance)
		self.balance +=amount
		print("updated balance is :",self.balance)
	
	def Withdraw(self,amount):
		if amount<=self.balance:
			print("current balance is:",self.balance)
			self.balance-=amount
			print("reduced updataed balance :",self.balance)
		else:
			print("insufficient balance")

acc=Bankacc("farate",1000)
acc.Deposit(800)
acc.Withdraw(800)