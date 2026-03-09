class Node:
	def __init__(self,data):
		self.data = data
		self.next=None

n1=Node(5)
n2=Node(10)
n3=Node(15)

n1.next=n2
n2.next=n3

print(n1.data)
print(n1.next.data)
print(n1.next.next.data)
