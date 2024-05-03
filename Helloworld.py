#Grammar Sugar in Python

#1. swap two numbers

x = 1
y = 2
x, y = y, x#this helps swap two numbers
print(x, y)


#2. List Comprehesion
list1 = range(1, 4)
list2 = [i*i for i in list1]
print(list2)

