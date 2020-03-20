data = input('Please give me a string: ')
data = data.lower()
vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowelCount = 0
consonantCount = 0


for string in data:
    for i in vowels:
        if string == i:
            vowelCount += 1
    for i in consonants:
        if string == i:
            consonantCount += 1

print('Your string contains %s vowels and %s consonants.' %(vowelCount, consonantCount))
