sentence = input("Enter a sentence: ").upper()
#create two lists
vowels = ['A','E',"I", "O", "U"]
num = [0,0,0,0,0]

#loop through every char
for i in range(len(sentence)):
#for every char, loop through vowels
  for v in range(len(vowels)):
    #if char matches vowels, increase num
      if sentence[i] == vowels[v]:
        num[v] += 1

for i in range(len(vowels)):
  print(vowels[i],":", num[i])
