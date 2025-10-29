import pandas as pd

a=[1,2,3]
myvar = pd.Series(a)
print("pandas series with defualt indexing:")
print(myvar)

print("pandas series with provided indexing:")
b=[7,8,9,10]
myvar3 = pd.Series(b,index=["w","x","y","z"])
print(myvar3)


print("pandas series with dictionary:")
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar2 =pd.Series(calories)
print(myvar2)


