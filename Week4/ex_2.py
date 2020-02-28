list_1 = [1, '2', 7.5, "ali", 'elif', 'a', 'bbb']
print("Current lenght of the list: ", len(list_1))
lengthOfList = int(input("Enter the limit of length: "))
if len(list_1) <= lengthOfList:
    a = input("Enter a new list member: ")
    list_1.append(a)
print("New length of the list: ", len(list_1))
print(list_1)
