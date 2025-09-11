class Name:
    def __init__(self):
        self.First_Name = "pratik"
        self.Last_Name = "farate"
        self.age = 23

    def __del__(self):
        print('Destructor called, Employee deleted.')
nm = Name()

print(nm.First_Name)
print(nm.Last_Name)
print(nm.age)
del nm
