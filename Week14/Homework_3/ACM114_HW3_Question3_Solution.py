def frequency(sentence, freq = {}):   # frequency of words in text
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1

    words = list(freq.keys())
    words.sort()
    
    for i in words:
        print("%s: %d" % (i, freq[i]))
    
    print()
    return tuple("%s: %d" %(i, freq[i]) for i in words)

def freq(line):
    str_1 = line.split()
    # split words are stored and sorted as a set
    words = sorted(set(str_1))  

    for i in words:
        print("{0}: {1}".format(i, str_1.count(i)))
    
    print()
    return list("{0}: {1}".format(i, str_1.count(i)) for i in words)

def freq_2(line, dict_1 = {}):
    s = line.split()
    for i in s:
        # setdefault() function takes key & value to set it as dictionary.
        i = dict_1.setdefault(i, s.count(i))
        
    # items() function returns both key & value of dictionary as a list
    # and then sorted. The sort by default occurs in order of 1st -> 2nd key
    dict_1 = sorted(dict_1.items())         
                                          
    for i in dict_1:
        print("%s: %d" % (i[0], i[1]))
    
    print()
    return set("%s: %d" % (i[0], i[1]) for i in dict_1)

def freq_3(line_1):
    s_1 = line_1.split()
    # sets dictionary as i -> split word & s_1.count(i) -> total occurrence of i in s_1
    # items() function returns both key & value of dictionary as a list
    # and then sorted. The sort by default occurs in order of 1st -> 2nd key
    dict_2 = {i:s_1.count(i) for i in s_1}
    for key, value in enumerate(dict_2.items()):
        print(key, value)
    print()
    for key, value in dict_2.items():
        print(key, "\t", value)
    print()
    print(dict_2)
    print()
    dict_2 = sorted(dict_2.items())
    print(dict_2)
    print()
                                    
    for i in dict_2:
        print("%s: %d" % (i[0], i[1]))
    
    print()
    return list("%s: %d" % (i[0], i[1]) for i in dict_2)

line = input("Enter a sentence: ")
print()
print(frequency(line))
print()
print(freq(line))
print()
print(freq_2(line))
print()
print(freq_3(line))