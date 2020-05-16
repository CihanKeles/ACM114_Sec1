def file_analysis(file1, file2):
    # Create set containing the unique words of the first file
    f_1 = open(file1, 'r')
    text1 = f_1.read()
    f_1.close()
    words1 = text1.split()
    set1 = set(words1)

    # Get input text of second file and create set containing its 
    # unique words
    f_2 = open(file2, 'r')
    text2 = f_2.read()
    f_2.close()
    words2 = text2.split()
    set2 = set(words2)

    # Obtain the union of the sets and print the items in it
    union = set1.union(set2)
    print('These are the unique words that are ' \
          'contained in both files:')
    for item in union:
        print(item)
    print()

    # Obtain the intersection of the sets and print the items in it
    intersection = set1.intersection(set2)
    print('These are the words that appear both files:')
    for item in intersection:
        print(item)
    print()

    # Obtain the difference between set1 and set2 and 
    # print the items in it
    difference1 = set1.difference(set2)
    print('These are the words that appear in the first file' \
          ' but do not appear in the second file:')
    for item in difference1:
        print(item)
    print()

    # Obtain the difference between set2 and set1 and 
    # print the items in it
    difference2 = set2.difference(set1)
    print('These are the words that appear in the second file' \
          ' but do not appear in the first file:')
    for item in difference2:
        print(item)
    print()

    # Obtain the symmetric difference between set1 and set2 
    # and print the items in it
    sym_diff = set1.symmetric_difference(set2)
    print('These are the words that appear in the first' \
          ' file or the second file but do not appear in' \
          ' the both files:')
    for item in sym_diff:
        print(item)
    print()

# Get the name of the first file as a first input.  
first_file_name = input('Enter the name of the first input file: ')

print()

# Get the name of the second file as a second input.
second_file_name = input('Enter the name of the second input file: ')

print()

# Call the file_analysis function.
file_analysis(first_file_name, second_file_name)
