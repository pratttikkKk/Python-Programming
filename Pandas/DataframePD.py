import pandas as pd
mydata= {
	'Car':["farari","thar","lambourgini","roles royles"],
	'Cost':[1000000,1600000,20000000,40000000],
	'Color':["red","black","blue","white"]

}

mycar = pd.DataFrame(mydata)
print(mycar)

print(mycar.loc[1])                                  #used for access specific row loc