print('Create account now')
username = input('Enter username: ')
password = input ('Enter password: ')

def login():
    us = input('Enter username: ')
    pa = input('Enter password: ')
    if us == username and pa == password:
        print('Loged in successfully')
    else:
        print('Invalid Credntials')

print('Your account has been created successfully')
UserChoice = int(input('Enter 1 for login \nand 2 for exit'))
if UserChoice == 1:
    login()
elif UserChoice == 2:
    print('your choice is exit')
else:
    print('Your entered a wrong choice')