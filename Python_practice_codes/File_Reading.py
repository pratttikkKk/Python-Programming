file_name=input("enter file name::")

try:
	with open (file_name,"r") as f:
		for line in f:
		 print(line, end="")

except FileNotFoundError:
		print("file not found try to search directory")