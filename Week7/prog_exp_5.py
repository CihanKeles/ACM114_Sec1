sentence = input("Sentence: ")
# Sentence: this is a sentence
counts = {i:0 for i in 'aeiouAEIOU'}
for char in sentence:
    if char in counts:
        counts[char] += 1

for k,v in counts.items():
    print(k, v)
