# The dectionaries are used to store data value in the key value pairs
# Dectionary stores value in a pair of keys and value

# How to write a dictionary in python?  Eg:
# Every type of values are possible to add to dictionary like string, intiger, list, tuple, etc.
MyDectionary = {
    'name':'Abdhu',
    'nationality':'India',
    'age':20,
    'is Tall':False,
    'Friends':['a', 'b', 'c', 'd'],
    'hobby':('traval', 'reading', 'learn')
}
print(MyDectionary)
print('\n')

# How to print aspecial key value from Dectionary
print(MyDectionary['name'])
print('\n')

# Dectionary not allows to write two keys with same name
# Eg:
eg = {
    "name":"Abdhu",
    "name":"Jhone"
}
print(eg)
print('\n')

# len function is avilable here
print(len(MyDectionary))
print('\n')

# possible to assing a dictionary value to a new name like below

x = MyDectionary['name']
print(x +'\n')