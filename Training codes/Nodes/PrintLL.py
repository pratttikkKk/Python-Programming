class Node:
	def __init__(self,r,n):
		self.roll =r

		self.name =n
		self.next=None

head=Node(5,"pratik")
head.next=Node(10,"ruturaj")
head.next.next=Node(15,"abhi")

print(head.roll,head.name)
print(head.next.roll,head.next.name)
print(head.next.next.roll,head.next.next.name)
