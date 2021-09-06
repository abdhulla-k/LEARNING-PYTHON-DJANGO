# Example for a while loop
i = 1
while i < 10:
    print(i)
    i += 1

print('========================================================================================')

# Example for a for loop:
for letter in 'HelloWorld':
    print(letter)

print('========================================================================================')


# What is nested loop ?
MyLIst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print('from nested loop')
for lists in MyLIst:
    for row in lists:
        print(row)