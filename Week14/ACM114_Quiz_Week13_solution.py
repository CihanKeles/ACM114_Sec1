import random

# The main function.
def main():

    # Initialize an empty dictionary.
    number_dict = dict()

    # Repeat 100 times.
    for i in range(100):
        # Generate a random number between 1 and 9.
        random_number = random.randint(1, 9)

        # Establish or increment the number in the dictionary.
        if random_number not in number_dict:
            number_dict[random_number] = 1            
        else:
            number_dict[random_number] += 1

    # Display the results.
    print('Number\tFrequency')
    print('------  ---------')

    # The "sorted" function produces a sorted version of
    # the list of key-value pairs from the "items" method.
    for number, frequency in sorted(number_dict.items()):
        print(number, frequency, sep='\t')
         

# Call the main function.
main()
