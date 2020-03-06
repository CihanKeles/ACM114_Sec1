counts = dict()
print('Enter a line of text:')
line = input('')
print()

words = line.split()

print('Words:', words)
print()

print('Counting...')
print()

for word in words:
    counts[word] = counts.get(word,0) + 1
    
print('Counts', counts)
