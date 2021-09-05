# Tuples are very similar to list.But there are some basic difference, like tuples are immutable means you can't change
# any value in a tuple

# example for a tuple

from typing import Tuple


number = (1, 2, 3)

print(number)
print(number[0])
print('\n')

# not possible to assign a number to tuple
# number[1] = 28    it does't work. Becouse, tupple has not allow it

# But tuple allow repetation of same value like below
number2 = (1, 2, 3, 4, 5, 6, 1, 1, 1, 2, 3, 5)
print('tuple allow repetation of same number')
print(number2)
print('\n')

# Tuple allows various type of data

name = ('apple', 'banana', 'tomato')
boo = (True, False, True, False)
print('tuple allows vrious type of data')
print(name)
print(boo)
print('\n')

# tuple allows to mixe various data type
a = ('a', True, 33)
print(a)
print('\n')

# check type of a value
print(type(a))
print(type(a[0]))
print('\n')

