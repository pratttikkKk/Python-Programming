class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class singlyLinkedList:
	def __init__(self):
		self.head = None
	
	def insertNodeAtLast(self):
		if self.head == None:
			self.head = Node(int(input("enter the data")))
		else:
			t=self.head
			while t.next.head !=None:
				t=t.next
			t.next=Node(int(input("enter the data")))

	def Display(self):
		t=self.head
		if t==None:
			
		while t!= None:
			print(t.data)
			t=t.next