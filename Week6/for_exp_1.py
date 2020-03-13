print('This program displays a list of numbers')
print('and their squares.')
start = int(input('Enter the starting number: '))
end = int(input('How high should I go? '))
   
print()
print('Number\tSquare')
print('--------------')

for number in range(start, end + 1):
    square = number**2
    print(number, '\t', square)
