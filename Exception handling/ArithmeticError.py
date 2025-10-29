
try:
  div=10/0
  print(div)
except ArithmeticError:
  print("Error in calculation")
  
except:
  print("Something else went wrong")

finally:
  print("code run successfull ")