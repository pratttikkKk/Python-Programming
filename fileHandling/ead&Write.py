with open("input.txt","r") as source_file:
	content=source_file.read()

with open("output.txt","w") as destination_file:
	destination_file.write(content)

print("successfull")