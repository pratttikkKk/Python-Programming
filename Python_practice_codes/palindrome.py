n=int(input("enter a number::"))

rev = int(str(n)[::-1])         #Convert number to string, reverse it ([::-1]), and compare.

if n==rev:
	print("it is a plaindrome")
else:
	print("it is not palindrome")