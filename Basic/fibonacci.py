def fibona(n):
	a=0
	b=1
	for i in range(n): 
		print(a,end=" ")
		a,b=b,a+b                #0,1,1,2,3,5,8

	

fibona(5)
