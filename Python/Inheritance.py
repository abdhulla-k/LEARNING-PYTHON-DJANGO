class Base():
    name = 'Abdhu'
    age = 20
    gender = 'Male'

# it is the method of inheritance
class Sub(Base):           # the all content from Base class is available in Subclass.Becouse of Inheritance
    pass          # use pass to privent error

p1 = Sub()
print(p1.name)

# multylevel Inheritance and Multipple inheritnce are possible in python