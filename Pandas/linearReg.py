from sklearn.linear_model import LinearRegression
model=LinearRegression()

x=[[500],[1000],[2000]]
y=[10,20,40]

model.fit(x,y)
print(model.predict([[1500]]))