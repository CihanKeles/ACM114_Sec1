# Programming Exercise 1

# Local variables
day = 0
month_num = 0
month_name = ''
date_string = ''
month_list = ['January', 'February','March',
            'April', 'May','June', 'July',
            'August', 'September', 'October',
            'November', 'December']
    
# Get the date in mm/dd/yyyy format as input from the user.
date_string = input('Enter a date in the format mm/dd/yyyy: ')

# Split date_string.
date_list = date_string.split('/')

# Obtain month and day numbers.
month_num = int(date_list[0])
day = date_list[1]
year = date_list[2]

# Get month_name.
month_name = month_list[month_num - 1]

# Create string for long date format.
long_date = month_name + ' ' + day + ', ' + year

# Display long date format.
print(long_date)
