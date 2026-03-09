class Node:
	def createmember(self,d,next=None):
		self.data = d
		self.next=next

n1=Node()
n1.createmember(10)
print(n1.data)


n2=Node()
n2.createmember(5)
print(n2.data)
