# Programming Exercise 3

# Local variables
digit_list = ['2','3','4','5','6','7','8','9']
alpha_phone_number = ''
num_phone_number = ''

# Get the string as input from the user.
alpha_phone_number = input('Enter the telephone ' \
                        'number in the format' \
                        ' XXX-XXX-XXXX: ')

# Step through the string finding the index number
# from the digit list for each character. Build the
# string, and display the digits.
for ch in alpha_phone_number:
    # Determine if the character is a letter.
    if ch.isalpha():
        # If so, convert the character to uppercase.
        ch = ch.upper()
        # Determine the index number for the character
        # from the digit list.
        if ch == 'A' or ch == 'B' or ch == 'C':
            index = 0
        elif ch == 'D' or ch == 'E' or ch == 'F':
            index = 1
        elif ch == 'G' or ch == 'H' or ch == 'I':
            index = 2
        elif ch == 'J' or ch == 'K' or ch == 'L':
            index = 3
        elif ch == 'M' or ch == 'N' or ch == 'O':
            index = 4
        elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
            index = 5
        elif ch == 'T' or ch == 'U' or ch == 'V':
            index = 6
        elif ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z':
            index = 7
        # Set the character to a digit from the list.
        ch = digit_list[index]
            
    # Concatenate the digit to the string.
    num_phone_number = num_phone_number + ch

# Display the phone number's digits.
print('The phone number is', num_phone_number)

