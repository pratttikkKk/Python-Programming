import os  

srcc = input("enter: ")  

if os.path.exists(srcc):  
    print("success") 
   
    with open(srcc, "r") as src, open("destination.txt", "w") as dest:
        for line in src: 
            dest.write(line)  
else:
    print("no file is there") 
