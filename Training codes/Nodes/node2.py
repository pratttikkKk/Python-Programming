class Node:
	def createmember(self):
		self.data = int(input("enter data : "))
		self.next=None

n1=Node()           #create a object of class node
n1.createmember()   #calling the function create memeber
print(n1.data)      #accessing the data variable from node class through n1 object


n2=Node()
n2.createmember()
print(n2.data)
