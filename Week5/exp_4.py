marks = {}.fromkeys(['Math','English','Science'], 0)

# Output_1: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():    
	print(item)

# Output_2: ['English', 'Math', 'Science’]
print(list(sorted(marks.keys())))
