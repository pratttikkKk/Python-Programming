class b1:
  def cricket(self):
    print("i am a cricket")
    
class d1(b1):
  def bat(self):
    print("i am a bat of cricket")
    
class d2(b1):
  def ball(self):
    print("i am s ball of cricket")
    
class d3(d1,d2):
  def player(self):
    print(" i am playing with bat and ball")
    
obj = d3()
obj.ball()