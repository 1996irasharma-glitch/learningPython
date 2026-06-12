#args and kwargs
#what *args does it allows you to pass n number of arguments without error
#for example
# example function (fixed syntax)
def myfunct(a,b):
    pass
#would only take two arguments so a third argument cannot be used but if *arg is used in its place this problem is solved

#kwargs or keyword arguments give out a dictionary

def myfruit(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

x = (myfruit(fruit='apple', veggie='lettuce'))
#this code return the given tupple in the form of a dictionary
# you can use both of these at the same time as well
def myfunc(*args,**kwargs)
#they have to follow the same order in the tuple given to us


#map filter and lambda functions
#map function basically iterates a function through a list without having to use a large block of code
def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

#output
#1
#4
#9
#16
#25

#or
list(map(square,my_nums))
#[1, 4, 9, 16, 25]
#while using the function name with map,do not use brackets


#filter basically returns only those items in the list which satisfy the conditions of the function
def check_even(num):
    return num%2 == 0
mynums = [0,1,2,3,4,5,6]

list(filter(check_even,mynums))
#[0, 2, 4, 6]


#if u want to use a function only one time u can use a lambda function
#so instead of 
def check_even(num):
    return num%2 == 0
#u can write it as
square =lambda num: num**2
square(5)
#25

#to use it with map and filter, we can
list(map(lambda num:num**2,mynums))
list(filter(lambda num:num%2 ==0,mynums))

#to find first letters of the given list
names = ['Ira','Sanvi','Vasu']
map(lambda x : x[0],names)
