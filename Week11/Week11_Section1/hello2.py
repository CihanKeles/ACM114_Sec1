# Define a function
def world():
    print("Hello, World!")

def root(number):
    return "The square root of %d is: %.2f" %(number, number**0.5)

# Call function within module
world()
print()
print("Enter an integer to calculate it's square root: ", end = '')
n = int(input())
print(root(n))
