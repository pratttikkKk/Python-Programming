class father:
 def father(self):
  print("i am a father")

class son(father):
 def son(self):
  print("i am a son")

class daughter(father):
 def daughter(self):
  print("i am a daughter")

s=son()
s.son()

d=daughter()
d.daughter()
