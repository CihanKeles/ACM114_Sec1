TAX_FACTOR = 0.0065   # Represents the tax factor.
print('Enter the property lot number')
print('or enter 0 to end.')
lot = int(input('Lot number: '))
while lot != 0:
     value = float(input('Enter the property value: '))
     tax = value * TAX_FACTOR
     print('Property tax: $', format(tax, ',.3f'), sep='')
     print('Enter the next lot number or')
     print('enter 0 to end.')
     lot = int(input('Lot number: '))
