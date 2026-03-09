import matplotlib.pyplot as p

x=[1,1,1,1,1,1,2,2,1]
y=[1,2,3,4,5,6,6,4,4]
p.plot(x,y, marker='o')

p.xlabel("x axis")
p.ylabel("y axis")
p.title("simple line")

p.show()