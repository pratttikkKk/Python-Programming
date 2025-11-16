import matplotlib.pyplot as plt

cricketers =["Rohit","Virat","MSD","Sachin","Hardik"]
scores=[264,183,183,200,119]

plt.barh(cricketers,scores)
plt.xlabel("cricketers")
plt.ylabel("scores")
plt.title("crick info")

plt.show()