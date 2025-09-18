class Senior:
	def TY(self,name):
	  
	  # self.name=name

	  print("i am a senior student of third year "+name)

class junior(Senior):
	def FY(self):
		print("i am a junior of first year")

obj =junior()
obj.FY()
obj.TY("pratik")