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
			while t.next != None:
				t=t.next
			t.next=Node(int(input("enter the data")))

	def Display(self):
		t=self.head
		if t==None:
			pass
		while t!= None:
			print(t.data)
			t=t.next

	def insertNOdeatFIrst(self):
		data = int(input("enter data"))
		n = Node(data)
		n.next = self.head
		self.head = n
  
	def deleteFirst(self):
		if self.head == None:
			print("no node available")
		else:
			t = self.head
			self.head = self.head.next
			t = None

	def deleteLast(self):
		if self.head == None:
			print("no node available")
		elif self.head.next==None:
			s.deleteFIrst()
		else:
			t=self.head
			while t.next.next!=None:
				t=t.next
			t.next=None
	def CountNode(self):
		if self.head == None:
			print("no node available")
		count=0
		t=self.head
		while t!= None:
			t=t.next
			count=count+1
		print("total count",count)

	def CountSum(self):
		if self.head == None:
			print("no node available")
		sum=0
		t=self.head
		while t!= None:
			sum=sum+t.data
			t=t.next
			
		print("total sum",sum)

	def MinValue(self):
		if self.head == None:
			print("no node available")
		
		else:
			t=self.head
			min=t.data
			while t!=None:
				if t.data < min:
					min = t.data
				t=t.next
		print("min is",min)

	 
s=singlyLinkedList()
s.insertNOdeatFIrst()
s.insertNOdeatFIrst()
# s.insertNOdeatFIrst()
# s.insertNOdeatFIrst()
# s.insertNodeAtLast()
# s.insertNodeAtLast()
# # s.deleteFirst()
# s.CountNode()
# s.CountSum()
# s.Display()
s.MinValue()

