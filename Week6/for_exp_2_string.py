max = int(input('Maximum value:'))   # The maximum number

# Initialize an accumulator variable.
total = 0.0
s = ', '
list_1 = []
   
# Explain what we are doing.
print('This program calculates the sum of')
print(max, 'numbers you will enter.')

# Get the numbers and accumulate them.
for counter in range(max):
    number = int(input('Enter a number: '))
    list_1.append(str(number))
    print(s.join(list_1))
    print(' - '.join(list_1))
    total = total + number

# Display the total of the numbers.
print('The total is', total)
