class Node:
	def __init__(self,data):    #constructor is called automatically when object is created
		self.data = data
		self.next=None

n1=Node(10)
n2=Node(5)             #here we dont need to call object.
print(n1.data)
print(n2.data)