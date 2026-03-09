class father:
 def father(self):
  print("i am father")
 

class mother:
 def mother(self):
  print("i am mother")

class child(mother,father):
 def child(self):
  print("i am child")

o=child()
o.father()
o.mother()
o.child()