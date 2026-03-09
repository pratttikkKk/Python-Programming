"""
class student_i:
 def get_info(self):
  self.name=input("enter your name:")
  self.age=int(input("enter your age:"))

class student_o(student_i):
 def display_info(self):
  print("your name:" ,self.name)
  print("your age:",self.age)

obj=student_o()

obj.get_info()
obj.display_info()
"""
class student_i:
 def get_info(self):
  print("i am the king")  

class student_o(student_i):
 def display_info(self):
  print("i am the queen ")
  
obj=student_o()

obj.get_info()
obj.display_info()