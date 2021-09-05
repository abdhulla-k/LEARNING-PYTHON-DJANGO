# an example for if else

a = 1
b = 2
c = 3
d = 4

if a <= b:
    print(str(a) +' is in b \n')
else:
    print(" a is greater than b \n")
if b == c:
    print(str(b) +' is equalto c \n')
elif b < c:
    print(str(b)+ ' is less than c \n')
else:
    print(str(b)+ ' is greater than c \n')
if c <= d:
    print(str(c) +' is in b \n')

# an anothor example

def DataType(data):
    if type(data) == str:
        return(data + ' is a string \n')  
    elif type(data) == int:
        return(str(data)+ ' is a intiger \n')
    else:
        return(data + ' is a boolian \n')

print(DataType(input('Enter eny data which should be a string, intiger or a boolian \n')))

def CheckeWithFive(num):
    if num%5 == 0:
        print(str(num) + " can be devided by 5 \n")
    else:
        print(str(num) + " can not be devided by 5 \n")

CheckeWithFive(int(input("Enter a number")))