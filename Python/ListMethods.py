# Going to learn about list functions or methods

list1 = [1, 2, 3, 4, 5]
list2 = ['banana', 'apple', 'orenge', 'tomato']
list3 =  ['banana', 'apple', 'orenge', 'apple', 'tomato', 'apple']
list4 = [2, 1, 4, 3, 5, 6]

# how to print this together

list1.extend(list2)
print('extednded list2 to list1')
print(list1)
print('\n')

# how to add a new name to list2

list2.append('coconut')
print('count values containing list2 is: ')
print(list2)
print('\n')

# how to put a value in between two values

list2.insert(2, 'mango')
print('added mango to list2. possitionis 2')
print(list2)
print('\n')

# how to remove a value

list2.remove('apple')
print('removed apple from list2')
print(list2)
print('\n')

# how to delete all of the values fro list2

list2.clear()
print('cleared all data from list2')
print(list2)
print('\n')

# how to find the index number of a value

print('index number of apple in list3 is: ')
print(list3.index('apple'))
print('\n')

# how to checke a value that howmany times repeated in a list

print('how to check a value that howmany times repered in list3')
print(list3.count('apple'))
print('\n')

# how to print a scattered number list in order
list4.sort()
print('packed the list4')
print(list4)
print('\n')

# how to print a list as revers

list3.reverse()
print('reveselly packed the list3')
print(list3)
print('\n')

# how to coppy and past a list to a nwl list

NewList = list3.copy()
print('copy of list3 is pasted to newList')
print(NewList)
print('\n')

# how to remove last value from a list

NewList.pop()
print('removed last value from NewList :')
print(NewList)
print('\n')

# how to remove a specific value from a list using index number

NewList.pop(1)
print('removed second value from list New: ')
print(NewList)
print('\n')

# how to delete a value fro a list

del NewList[0]
print('deleted 0the position fro NewList')
print(NewList)
del NewList                              #.remove() will remove all data from the list.but the list will avilabe at that 
print('deleted Newlist')                 # time. but 'del' will delete both data and list
#print(NewList)
