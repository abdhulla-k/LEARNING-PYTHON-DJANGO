# how to print specific letter of a string
name = 'abdhu'

print(name[0]+name[3])

# how to add new line

print("use \\n to add new line. for example \n is this")

# how to convert to uppercase

print(name.upper())     # use function 'lower()' for convert to lower case

# how to add defferent functions together
# I am going to checkes is the letters of aname is uppercase?

print(name.isupper())
print(name.upper().islower())
print(name.upper().isupper())

# how to get the length of a string

print(len(name))

# how to find an index number of a letter or position of a letter. i am going to print the index number of 'd'

print(str(name.index('d')) + ' is the index number of  d')

# how to replace a letter

print('replaced a to A   :' + name.replace('a', 'A'))



"""There are a lot of string fucnctions in python"""