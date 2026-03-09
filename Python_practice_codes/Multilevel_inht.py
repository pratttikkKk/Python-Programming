class grandfather:
 def grandfather(self):
  print("i am grandfather")
 

class father(grandfather):
 def father(self):
  print("i am father")

class child(father):
 def child(self):
  print("i am child")

o=child()
o.grandfather()
o.father()
o.child()