class Student:
 school_name= "D Y PATIL"
 
 def __init__(self,name,age,grades):
  self.name=name
  self.age=age
  self.grades=grades

 def average(self):
  return sum(self.grades)/len(self.grades)

 def Display(self):
  print("name of the school:",self.school_name)
  print("name of the student:",self.name)
  print("age of the student:",self.age)
  print("avg of the student:",self.average())

s1=Student("pratik",18,grades=[10,20,30])

s2=Student("djbk",18,grades=[100,80,90,90,80,100])

s3=Student("dyp",18,grades=[10,20,30])

print("\nstudent details:\n")
print("student1 details:")

s1.Display()
print("\nstudent2 details:")
s2.Display()
print("\nstudent3 details:")
s3.Display()