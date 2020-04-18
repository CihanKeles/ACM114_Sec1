# Define a function
def world():
    import time, random, math
    time.sleep(2)
    print("Hello, World!")
    time.sleep(2)
    print("Coding in Python is exciting!")
    time.sleep(2)
    name = input("Enter a name: ")
    time.sleep(2)
    n = random.randint(1,10)
    for i in range(1, n+1):
        print("Hello", name)
    return 'The ant {0} is in the restricted area as {1:.3f} cm^2'.format(name, math.pi * n ** 2)

# Define a variable
ant = "Rocky"

# Define a class
class Car:

    def __init__(self, name, model, color):
        self.color = color
        self.model = model
        self.name = name

    def tell_me_about_the_car(self):
        print(self.name + " is the brand name of car.")
        print("The car's model is " + self.model + ". What a nice car!")
        print("This car is " + self.color + ".")
