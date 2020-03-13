n = int(input("Enter n:"))
list1 = [n for i in range(0,n)]
sub_list = [list1 for i in range(0,n)]
print(list1)
print()
print(sub_list)

print()

L1 = []
sub_L1 = []
for i in range(0,n):
    L1.append(n)
    sub_L1.append(L1)
print(L1)
print(sub_L1)

print()

i = 0
list2 = list(range(1,6))
for l in list2:
    print(i, l)
    i += 1

print()

for i, val in enumerate(list2):
    print(i, val)

print()

string = 'Python'
list3 = list(string)
print(list3)

for idx, ch in enumerate(string):
    print("index is %d and character is %s:" %(idx, ch))
    

print()

j = 0
for ele in list3:
    print("index is {}, character is {}:".format(j, ele))
    print()
    print("index is {0}, character is {1}:".format(j, ele))
    j += 1
    print()



