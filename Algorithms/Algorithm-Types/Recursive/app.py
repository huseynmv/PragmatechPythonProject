def factorial(x):
    if x == 1:
        return x 
    else :
        return (x * factorial(x-1))

num = 7
print("The factorial of", num, "is", factorial(num))   