squares = {x: x*x for x in range(6)}

# Output_1: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)

squares = {} 	# This code has same attributes as in above.

for x in range(6):
   squares[x] = x*x

print(squares)

odd_squares = {x: x*x for x in range(10) if x%2 == 1}

# Output_2: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(odd_squares)

print(sorted(squares))
print(sorted(odd_squares))
