
def factorial(n):
 if n==0 or n==1:
  return 1
 else:
  return n*factorial(n-1)      #5 4 3 2 1 1

print(factorial(5))