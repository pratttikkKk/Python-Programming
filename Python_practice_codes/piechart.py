import matplotlib.pyplot as plt
 
parties=["congress","bjp","shivsena","ncp","mns","swabhimani","aap"]
votes=[250,200,150,150,150,50,50]
plt.pie(votes,labels=parties, autopct='%1.1f%%')

plt.title('Indian election 2029')
plt.show()