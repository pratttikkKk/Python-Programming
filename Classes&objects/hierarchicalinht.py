
class Parent:
    def func1(self):
        print("parent class.")
1
class Child1(Parent):
    def func2(self):
        print("child class 1.")

class Child2(Parent):
    def func3(self):
        print("child class 2.")

o1 = Child1()
o2 = Child2()

o1.func1()
o1.func2()
o2.func1()
o2.func3()