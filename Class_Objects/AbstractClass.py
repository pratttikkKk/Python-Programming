from abc import ABC,abstractmethod

class Animal(ABC):
	@abstractmethod
	def Sound(self):
		pass

class Dog(Animal):
	def Sound(self):
		return "bark"
	
# an=Animal()
# print(an.Sound())     #this will gives type error 
	
dog =Dog()
print(dog.Sound())