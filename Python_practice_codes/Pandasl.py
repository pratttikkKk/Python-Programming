import pandas as pd

data={

 "name":["pratik","rohit","virat"],
 "age":[21,22,23],
 "marks":[87,66,78]
}

df=pd.DataFrame(data)

print(df)

print("first two rows:\n",df.head(2))
print(":\n",df.describe())

print("age:\n",df["age"])

df["grade"]=["A","A+","A++"]
print(df)