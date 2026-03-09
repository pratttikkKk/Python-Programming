# num=int(input("enter:"))
# fact =1

# for i in range(1,num+1):
# 	fact=fact*i

# print(fact)


def factorial(n):
	if n==1 or n==0:
		return 1
	else:
		return n*factorial(n-1)

print(factorial(5))