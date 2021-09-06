# exaple for file operation
# going to write a function in file test.py

text = open("test.py","w+")
text.write("def sum():\n")
text.write("        print(2+3)\n")
text.write("sum()")
text.close()

# How to read
x = open("test.py","r")
print(x.readline())    # function 'readline' can print first line of the file only
print(x.readlines())   # function 'readlines' can print evrithing from th file. But that will be like a list
x.close()
print("==================================\n")


# possible to print all values as tht file

y = open("test.py","r")
for files in y.readlines():
    print(files)
y.close()
