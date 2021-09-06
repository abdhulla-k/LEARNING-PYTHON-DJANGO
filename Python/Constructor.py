class Main:                # created class here

    def __init__(self, name, age, place):         # this is the constructor of class main
        self.name = name
        self.age = age
        self.place = place

p1 = Main('abdhu', 20, 'Kerala')     # passing argument to constructor or class
print(p1.name)
print(p1.age)
print(p1.place)
print('\n')


# goin to input data from user

name = input('Enter your name: ')
age = input('Enter your age: ')
place = input('Enter your place: ')
p2 = Main(name, age, place)

print(p2.name)
print(p2.age)
print(p2.place)
print('\n')

# how to delete a object from a class ?
del p2
print(p2)                          # The reason for the error is this line.becouse already deleted the p2
print('\n')