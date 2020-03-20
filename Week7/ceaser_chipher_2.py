import time
arr = "abcdefghijklmnopqrstuvwxyz"
plain = input("Enter your text: ")
key = int(input("Enter key for encryption: "))
time.sleep(0.5)
print("Encrypting...")
encypher = ""

for c in plain:
    if c.isalpha():
        encypher += arr[(arr.index(c) + key) % 26]
    else:
        encypher += c

time.sleep(1)
print(encypher)

print("Decrypting...")
dcypher = ""

for c in encypher:
    if c.isalpha():
        dcypher += arr[(arr.index(c) - key) % 26]
    else:
        dcypher += c
        
time.sleep(1)
print(dcypher)
