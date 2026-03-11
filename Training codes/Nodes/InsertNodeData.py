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
			self.deleteFirst()
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
  
	def MaxValue(self):
		if self.head == None:
			print("no node available")
		
		else:
			t=self.head
			max=t.data
			while t!=None:
				if t.data > max:
					max= t.data
				t=t.next
		print("max is",max)

	def deleteNthNode(self, position):
		if self.head == None:
			print("no node available")
			return
		
		if position <= 0:
			print("Invalid position")
			return
		
		# Count total nodes
		count = 0
		t = self.head
		while t != None:
			count += 1
			t = t.next
		
		if position > count:
			print("Position out of range")
			return
		
		# Delete first node
		if position == 1:
			self.head = self.head.next
			return
		
		# Delete node at position
		t = self.head
		for i in range(1, position - 1):
			t = t.next
		t.next = t.next.next


	def EvenValue(self):
		if self.head == None:
			print("no node available")
			return
		t=self.head
		while t != None:
			if t.data%2==0:
				print(t.data)	
			t=t.next
	
	def OddValue(self):
		if self.head == None:
			print("no node available")
			return
		t=self.head
		while t != None:
			if t.data%2==1:
				print(t.data)	
			t=t.next

	def CountEven(self):
		if self.head == None:
			print("no node available")
		count=0
		t=self.head
		while t!= None:
			if t.data%2==0:
				count=count+1
			t=t.next
		print(count)
	
	def ReverseNode(self):
		if self.head == None:
			print("no node available")
		else:
			t=self.head
			li=[]
			while t!= None:
				li.append(t.data)
				t=t.next
			print(li[::-1])
# s.insertNOdeatFIrst()
# s.insertNOdeatFIrst()
# # s.insertNOdeatFIrst()
# # s.insertNOdeatFIrst()
# # s.insertNodeAtLast()
# # s.insertNodeAtLast()
# # s.deleteFirst()
# # s.CountNode()
# # s.CountSum()
# # # s.Display()
# # s.MinValue()
# # s.MaxValue()
# print("even number is: ")
# s.EvenValue()
# print("odd number is: ")
# s.OddValue()

s = singlyLinkedList()

while True:
	print("\nMenu:-")
	print("1.InsertNodeAtLast")
	print("2.InsertNodeAtFirst")
	print("3.DeleteFirst")
	print("4.DeleteLast")
	print("5.Display")
	print("6.countNode")
	print("7.CountSum")
	print("8.Minvalue")
	print("9.Maxvalue")
	print("10.evenvalue")
	print("11.Oddvalue")
	print("12.Delete Nth Node")
	print("13.even count")
	print("20.exit")
  
	choice = int(input("enter your choice"))
	match choice:
		case 1:
			s.insertNodeAtLast()
		case 2:
			s.insertNOdeatFIrst()
		case 3:
			s.deleteFirst()
		case 4:
			s.deleteLast()
		case 5:
			s.Display()
		case 6:
			s.CountNode()
		case 7:
			s.CountSum()
		case 8:
			s.MinValue()
		case 9:
			s.MaxValue()
		case 10:
			s.EvenValue()
		case 11:
			s.OddValue()
		case 12:
			pos = int(input("Enter position to delete: "))
			s.deleteNthNode(pos)
		case 13:
			s.CountEven()
		case 20:
			exit()

		