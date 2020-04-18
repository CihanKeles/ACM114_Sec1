# Define a function
def helloworld():
    print("Hello, World!")

def cube(number):
    return "The cube of {0} is: {1}".format(number, number**3)

# Call function within module
helloworld()
print()
print("Enter an integer to calculate it's cube: ", end = '')
m = int(input())
print(cube(m))
