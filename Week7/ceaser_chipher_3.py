realText = input("Enter the text that you want to encrypt: ")
step = int(input("Enter the key value for encryption: "))
inText = list(realText)
outText = []
cryptText = []
	
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
extend = [' ', '!','?','.',',',';','+','^','%','&','/','(',')','=','*','\\','-','_','#','$','{','[',']','}','`',':','<','>','|','"']

for eachLetter in inText:
    if eachLetter in extend:
        outText.append(' ')
    elif eachLetter in uppercase:
        index = uppercase.index(eachLetter)
        crypting = (index + step) % 26
        cryptText.append(crypting)
        newLetter = uppercase[crypting]
        outText.append(newLetter)
    elif eachLetter in lowercase:
        index = lowercase.index(eachLetter)
        crypting = (index + step) % 26
        cryptText.append(crypting)
        newLetter = lowercase[crypting]
        outText.append(newLetter)

print()
str_1 = ''.join(outText)
print(str_1)
print()
