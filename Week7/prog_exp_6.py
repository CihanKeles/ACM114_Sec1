while(True):
    phrase = input('Enter phrase you wish to count vowels: ')
    if phrase == 'end': #This will to be used to end the loop 
        quit() #You may use break command if you don't wish to quit

    lower = str.lower(phrase) #Will make string lower case
    convert = list(lower) #Convert sting into a list
    a = convert.count('a') #This will count letter for the letter a
    e = convert.count('e')
    i = convert.count('i')
    o = convert.count('o')
    u = convert.count('u')

    vowel = a + e + i + o + u #Used to find total sum of vowels

    print ('Total vowels = ', vowel)
    print ('a = ', a)
    print ('e = ', e)
    print ('i = ', i)
    print ('o = ', o)
    print ('u = ', u)
