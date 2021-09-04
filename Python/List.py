# going to work with list
# basics of list

countries = ['India', 'United Kingdom', 'Ghana', 'France', 'Switzerland', 'Norway']
print(countries)
print('zero\'th value of list countries is: ' + countries[0])       # it will print the 0th position containing value

# How to print a letter from 'France

print('First letter of France is: ' + countries[3][0])

# How to print all data after 'United Kingdom' or limitted data

print(countries[2:])
print(countries[3:5])

# how to find the type

print(type(countries))

# how to change a value from a list
# going to change 'United Kingdom' to 'United States'

countries[1] = 'United States'
print(countries)

# how to find lingth of a list

print(len(countries))

# possible to add different data types to a list

list2 = ['abdhu', 'omy', 2, 3, 5, True]
print(list2)
print(type(list2[5]))


                                     # An another method of list  

list3 = list(('United States', 3, False))
print(list3)