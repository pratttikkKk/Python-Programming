class cal:
 def add(self,a=None,b=None,c=None):
  if a is not None and b is not None and c is not None:
   return a + b + c
  elif a is not None and b is not None:
   return a+b
  elif a is not None:
   return a
  else:
   return 0

c=cal()
print(c.add(10,20,30))
print(c.add(10,20))
print(c.add(10))
print(c.add())