# The function of writing process.
def write(file, word_count):
    
    # Open output file.
    with open(file, 'w') as f:
  
        # Write specified number of random numbers to the file.
        for counter in range(1, word_count + 1):
            # Get a word.
            print('Word', counter, 'of', word_count, '- ', end='')
            word = input('Enter a word: ')

            # Write the word to the file.
            f.write(word + '\n')

        # Close the file.
        f.close()

# The function of reading and inserting processes.
def read_and_append(file):
    # Local variables
    counter = 0
    total_length = 0
    shortest_word = ''
    longest_word = ''
    temp = 1000

    # Open input file.
    with open(file, 'r') as f_1:

        # Read numbers from the file while keeping count 
        # and a running total.
        for word in f_1:
            # Strip line break from end of word and get its length.
            word = word.rstrip('\n')
            word_length = len(word)

            # Add length to total length and increment the counter.
            total_length += word_length
            counter += 1
        
            # Check for shortest word.
            if word_length < temp:
                shortest_word = word
                temp = word_length
            
            # Check for longest word.
            if word_length > len(longest_word):
                longest_word = word

        # Close the file.
        f_1.close()

        # Determine average length.
        average_length = total_length / counter
    
        # Display the results.
        print()
        print('Number of Words:', counter)
        print('Shortest Word:', shortest_word)
        print('Longest Word:', longest_word)
        print('Average Word Length:', round(average_length))
    
    # Open the same file (words.txt) to append the results.
    with open(file, 'a') as f_2:
    
        # Insert the results to the words.txt file.
        f_2.write('\n')
        f_2.write('Number of Words: ' + str(counter) + '\n')
        f_2.write('Shortest Word: ' + str(shortest_word) + '\n')
        f_2.write('Longest Word: ' + str(longest_word) + '\n')
        f_2.write('Average Word Length: ' + str(round(average_length)))
    
        # Close the file (words.txt) again.
        f_2.close()

# Give the name of output file.
outfile = input('Enter the name of the file to be created: ')

# Get the number of words to write to the file.
number_of_words = int(input('Enter number of words to write: '))

# Call the write function to end writing process.
write(outfile, number_of_words)

# Call the read_and_append function to end reading and 
# inserting processes of the same file.
read_and_append(outfile)
