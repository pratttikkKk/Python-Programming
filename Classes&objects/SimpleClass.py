class Student:
	def __init__(self,name,age):
		self.nm=name
		self.ag=age
	def myfunction(self):
		print("my name is:"+self.nm)

x=Student("pratik","21")
print("student name is: "+x.nm)
print("student age is: "+x.ag)

print(x)

x.myfunction()