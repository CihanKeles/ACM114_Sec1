def upper_lower_case(word):
    upper, lower = 0, 0
    for i in word:
        if 'a' <= i and i <= 'z' :
            lower += 1
        if 'A' <= i and i <= 'Z':
            upper += 1
    print("UPPER CASE: {0}\nLOWER CASE: {1}".format(upper, lower))
    return word, "Upper case --->", upper, "Lower case --->", lower

def upperLower(s):
    upper, lower = 0, 0
    for i in s:
        lower += i.islower()
        upper += i.isupper()
    print("UPPER CASE: ", end = '')
    print(upper)
    print("LOWER CASE: ", end = '')
    print(lower)
    return s, "Upper case ***", upper, "Lower case ***", lower

def comp_Func_Upper_Lower(string):
    upper = sum(1 for i in string if i.isupper())  # sum function cumulatively sum up 1's 
    lower = sum(1 for i in string if i.islower())  # if the condition is True
    print("UPPER CASE: %d\nLOWER CASE: %d" %(upper, lower))
    return string, "Upper case +++", upper, "Lower case +++", lower

def upper_lower_func(str_1):
    upper = 0
    lower = 0
    for x in str_1:
        if x.isupper() == True:
            upper += 1
        if x.islower() == True:
            lower += 1
    print("UPPER CASE:", upper)
    print("LOWER CASE:", lower)
    return str_1, "Upper case ---", upper, "Lower case ---", lower

def upper_lower_dict(str_2):
    dict_1 = {"UPPER CASE":0, "LOWER CASE":0}
    for char in str_2:
        if char.isupper():
            dict_1["UPPER CASE"]+=1
        elif char.islower():
            dict_1["LOWER CASE"]+=1
        else:
            pass
    return "UPPER CASE: {0}\nLOWER CASE: {1}".format(dict_1["UPPER CASE"], dict_1["LOWER CASE"])

word = input("Enter a word: ")
print(upper_lower_case(word))
print()
print(upperLower(word))
print()
print(comp_Func_Upper_Lower(word))
print()
print(upper_lower_func(word))
print()
print(upper_lower_dict(word))
