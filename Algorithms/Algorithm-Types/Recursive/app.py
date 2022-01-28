# def factorial(x):
#     if x == 1:
#         return x 
#     else :
#         return (x * factorial(x-1))
    
    
# num = 7
# print("The factorial of", num, "is", factorial(num))   

def recursion(k):
  if(k > 0):
    result = k + recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
recursion(6)