import numpy as np
arr = np.array([1,2,3,4,5])

np.savetxt("data.txt",arr)

loaded_data= np.loadtxt("data.txt")
print(loaded_data)