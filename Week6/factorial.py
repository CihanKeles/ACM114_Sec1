# Python code to demonstrate naive method 
# to compute factorial 
n = int(input("Enter a number to calculate its factorial: "))
fact = 1

if n < 0:
    print("Please enter a valid positive integer!")
    print("Factorial is not defined for negative values!")
    n = int(input("Enter a positive number to calculate its factorial: "))
    for i in range(1,n+1): 
        fact = fact * i 
    print("The factorial of", n, "is: ",end='')
    print(fact)

elif n == 0:
    print("The factorial of %d is: %d" %(n, fact))

else:
    for i in range(1,n+1): 
        fact = fact * i 
    print("The factorial of", n, "is: ",end='')
    print(fact)


m = int(input("Enter number: "))
fact = 1
while(m > 0):
    fact = fact * m
    m = m - 1
print("Factorial of the number is: ", end='')
print(fact)


# Python code to demonstrate math.factorial() 
# Exceptions ( Non-Integral number ) 
  
from math import *
# import math
# import math as m

k = int(input("Enter a positive number: "))

print("--> The factorial of", k, "is: ",end='')
print(factorial(k))
