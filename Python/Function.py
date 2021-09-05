# how to define a function?
# going to create a sum function

def sum(num1, num2):
    print('Welcome to sum function \nsum is below:')
    return int(num1) + int(num2)

print(sum(num1 = input('Enter two numbers'), num2 = input()))
print('\n')

# how to pass unlimitted arguments to a function? 
# write a '*' before like below

def greetings_function(*names):
    print('Welcome '+names[1])

greetings_function('abdhu', 'tomy', 'tim', 'm')