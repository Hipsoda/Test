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

#3. decoration
import time
def time_cnt(func):
    def wrapper(*argc, **kwargv):
        start = time.time()
        res = func(*argc, **kwargv)
        end = time.time()
        print("The function takes " + str(end - start) + " second")
        return res
    return wrapper

