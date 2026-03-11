class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.prev=None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def InsertNodeAtFirst(self):
		if self.head==None:
			self.head=Node(int(input("Enter data : ")))

		else:
			t=Node(int(input("Enter data : ")))

			t.next= self.head
			self.head=t

	def display(self):
		t=self.head
		while t!=None:
			print(t.data)
			t=t.next
	
	def insertNodeAtLast(self):
		if self.head == None:
			self.head = Node(int(input("enter the data:")))
		else:
			t=self.head
			while t.next != None:
				t=t.next
			t.next=Node(int(input("enter the data:")))
			t.next.prev=t

	def deleteFirst(self):
		if self.head == None:
			print("no node available")
		else:
			self.head=self.head.next
			if self.head!= None:
				self.head.prev=None

	def deleteLast(self):
		if self.head == None:
			print("no node available")
    
		else:
			t=self.head
			while t.next.next!=None :
				t=t.next
			t.next=None

c1 = DoublyLinkedList()
c1.InsertNodeAtFirst()
c1.InsertNodeAtFirst()
c1.InsertNodeAtFirst()
# c1.insertNodeAtLast()
# c1.deleteFirst()
c1.deleteLast()
c1.display()