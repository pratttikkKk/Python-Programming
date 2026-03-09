class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

head=Node(5)
head.next=Node(10)
head.next.next=Node(15)
head.next.next.next=Node(25)
head.next.next.next.next=Node(30)
head.next.next.next.next.next=Node(35)

while head!= None:
	print(head.data)
	head=head.next