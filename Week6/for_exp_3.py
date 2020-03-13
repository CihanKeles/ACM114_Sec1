numbers = list(range(0,52+1))
print(numbers)
print()

numbers=[]
for i in range(52+1):
    numbers.append(i)
print(numbers)
print()

str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs = 0
print(len(str1))
print()

for char in str1:
    numbs += 1

print(numbs)
print()

numbers = list(range(0,40+1))
print(numbers)
print()

print(sum(numbers))
print()

sum1 = 0
for i in numbers:
    sum1 += i
print(sum1)
print()

numbers = []
sum1 = 0
for i in range(41):
    numbers.append(i)
    sum1 += numbers[i]
print(numbers)
print()
print(sum1)
print()

s = "Python"
for idx in range(len(s)):
    print(s[idx % 2])

