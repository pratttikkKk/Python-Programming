file_name=input("enter file name:")
D_file_name=input("eneter destination file name:")

with open (file_name,"r") as s_file:
	data=s_file.read()

with open (D_file_name,"w") as d_file:
	d_file.write(data)
	print("data moved successfullly")