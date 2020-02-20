currentYear = int(input("Enter the year: "))
month = int(input("Enter the month: "))
if ((currentYear % 4) == 0 and (currentYear % 100) != 0 or (currentYear % 400) == 0):
	print ("Leap Year")
	if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
		print ("There are 31 days in this month.")
	elif (month == 4 or month == 6 or month == 9 or month == 11):
        	print("There are 30 days in this month.")
	elif (month == 2):
		print("There are 29 days in this month.")
	else:
		print("Invalid month!")

elif ((currentYear % 4) != 0 or (currentYear % 100) != 0 or (currentYear % 400) != 0):
	print ("Non Leap Year")
	if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
		print ("There are 31 days in this month")
	elif (month == 4 or month == 6 or month == 9 or month == 11):
		print("There are 30 days in this month")
	elif (month == 2):
		print("There are 28 days in this month")
	else:
		print("Invalid month!")
else:
	print("Invalid Year!")