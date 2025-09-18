class Teacher:
	def __init__(self,fname,lname):
		self.fname=fname
		self.lname=lname

	def print_name(self):
		print("my name is "+ self.fname +" and surname is "+ self.lname)


class Student(Teacher):
	pass

x=Student("pratik", "farate")

x.print_name()
