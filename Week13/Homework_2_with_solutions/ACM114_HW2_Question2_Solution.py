num = 0     # The starting number of organisms
avg = 0.0   # The average daily increase
days = 0    # The number of days to multiply

# Get a valid value for the starting number of
# organisms from the user.
while num <= 0:
    num = int(input('Starting number of organisms: '))

# Get a valid value for the average daily
# increase from the user.
while avg <= 0:
    avg = float(input('Average daily increase: '))

# Get a valid value for the number of days
# to multiply from the user.
while days <= 0:
    days = int(input('Number of days to multiply: '))

# Determine if the average daily increase was
# input as a whole number; if so, divide by
# 100 to format the value as a percentage.
if avg >= 1.0:
    avg /= 100.0

# Calculate and print amount of increase each day.
print ('Day Approximate\t\t Population')
print ('-----------------------------------')

for day in range(days):
    # Apply the increase after the first day.
    if (day > 0):
        num += (num * avg)
    print ((day + 1), '\t\t\t', num)
