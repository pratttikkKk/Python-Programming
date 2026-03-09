import numpy as np

arr= np.array([10,20,30,40])

print("original array:",arr)

print("arr 0 to 2:", arr[:3])

print("adding 5:", arr+5)

print("multiplication 2:", arr*2)

matrix = np.array([[10,20,30],[40,50,60]])
print(matrix)

reshaped= matrix.reshape(6,1)
print(reshaped)