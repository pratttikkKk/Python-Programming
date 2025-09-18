
class Grandpa:
    def __init__(self, grandfather):
        self.grandfather = grandfather

class Father(Grandpa):
    def __init__(self, fathername, grandfather):
        self.fathername = fathername
        
        Grandpa.__init__(self, grandfather)

class Son(Father):
    def __init__(self, sonname, fathername, grandfather):
        self.sonname = sonname
        
        Father.__init__(self, fathername, grandfather)

    def name(self):
        print('Grandfather name :', self.grandfather)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)


s1 = Son('fy', 'sy', 'ty')
print(s1.grandfather)
s1.name()