mark_up = 2.5  # The markup percentage
another = 'y'  # Variable to control the loop.

while another == 'y' or another == 'Y':
	wholesale = float(input("Enter the item's " + \
                            "wholesale cost: "))
	retail = wholesale * mark_up
	print('Retail price: $', format(retail, ',.2f'), sep='')
	another = input('Do you have another item? ' + \
                    '(Enter y for yes): ')
