class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class circularLinkedList:
	head = None

	def InsertNodeAtLast(self):
		if self.head==None:
			self.head=Node(int(input("Enter data : ")))
			self.head.next=self.head
		else:
			t=self.head
			while t.next!=self.head:
				t=t.next
			t.next=Node(int(input("Enter data : ")))
			t.next.next=self.head

	def DisplayNode(self):
		if self.head == None:
			print("no node available")
		else:
			t=self.head
			while True:
				print(t.data,end= " ")
				t=t.next
				if t==self.head:
					break
	
	def InsertNodeAtFirst(self):
		if self.head==None:
			self.head=Node(int(input("Enter data : ")))
			self.head.next=self.head
		else:
			t=self.head

			while t.next!= self.head:
				t=t.next
			data = int(input("Enter data :"))
			n= Node(data)
			n.next=self.head
			self.head=n
			
			t.next= self.head

	def deletelastNode(self):
		if self.head == None:
			print("no node available")
		else:
			t = self.head
			while t.next.next != self.head:
				t=t.next
			t.next=self.head
			print("last node deleted")
	
	def countnode(self):
		t=self.head
		count=1
		while t.next!= self.head:
			
			t=t.next
			count=count+1
		print(count)


c1=circularLinkedList()
while True:
	print("\nMenu:-")
	print("1.InsertNodeAtLast")
	print("2.InsertNodeAtFirst")
	print("3.count")
	print("4.DeleteLast")
	print("5.Display")
	
	choice = int(input("enter your choice"))
	match choice:
		case 1:
			c1.InsertNodeAtLast()
		case 2:
			c1.InsertNodeAtFirst()
		case 3:
			c1.countnode()
		case 4:
			c1.deletelastNode()
		case 5:
			c1.DisplayNode()














# c1.InsertNodeAtLast()
# c1.InsertNodeAtLast()
# c1.InsertNodeAtLast()
# c1.InsertNodeAtLast()
# c1.InsertNodeAtLast()
# c1.InsertNodeAtFirst()
# c1.InsertNodeAtFirst()

# c1.InsertNodeAtFirst()

# c1.InsertNodeAtFirst()

# c1.DisplayNode()
# c1.deletelastNode()
# c1.DisplayNode()