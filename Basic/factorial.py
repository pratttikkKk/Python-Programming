def factorial(n):
	fact=1
	for i in range(1, n+1):
		fact =fact*i  
	return fact    
		
print(factorial(5))		              
                                            #1*1=1
		                                     #1*2=2
											 #2*3=6
											 #6*4=24
											 #24*5=120

def factorial2(n):
	if n==0 or n == 1:
		return 1
	else:
		return n* factorial2(n-1)         #5*4*3*2*1

print(factorial2(5))
