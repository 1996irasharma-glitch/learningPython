#range is a built-in function that generates a sequence of numbers. It can be used in for loops to iterate over a sequence of numbers.
#The syntax for range is: range(start, stop, step)
#start is the number to start from (inclusive), stop is the number to stop at (exclusive), and step is the amount to increment by (default is 1).
#Example of using range in a for loop:
for i in range(5):
    print(i)
#This will output:
#0
#1
#2
#3
#4

#You can also specify a different start and step:
for i in range(1, 10, 2):
    print(i)
#This will output:
#1
#3
#5
#7
#9

#The range function is useful for iterating a specific number of times or generating a sequence of numbers for various purposes, such as indexing or creating lists.
#You can also convert the range to a list if you want to see all the numbers at once:
numbers = list(range(5))
print(numbers)
#This will output:
#[0, 1, 2, 3, 4]


#enumerate is a built-in function that adds a counter to an iterable and returns it as an enumerate object. It is often used in for loops to get both the index and the value of each item in a list.
#The syntax for enumerate is: enumerate(iterable, start=0)
#iterable is the collection you want to iterate over, and start is the number to start the counter from (default is 0).
#Example of using enumerate in a for loop:
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
#This will output:
#0 apple
#1 banana
#2 cherry

#You can also specify a different starting index:
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
#This will output:
#1 apple
#2 banana
#3 cherry


#zip is a built-in function that takes multiple iterables and returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables. It is often used to combine two or more lists into a single list of tuples.
#The syntax for zip is: zip(*iterables)
#iterables are the collections you want to combine.
#Example of using zip to combine two lists:
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = zip(names, ages)
print(list(combined))
#This will output:
#[('Alice', 25), ('Bob', 30), ('Charlie', 35)]

#You can also zip more than two lists:
cities = ['New York', 'Los Angeles', 'Chicago']
combined = zip(names, ages, cities)
print(list(combined))
#This will output:
#[('Alice', 25, 'New York'), ('Bob', 30, 'Los Angeles'), ('Charlie', 35, 'Chicago')]

#zip is also useful for unzipping a list of tuples back into separate lists:
combined = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
names, ages = zip(*combined)
print(names)
print(ages)
#This will output:
#('Alice', 'Bob', 'Charlie')
#(25, 30, 35)
#using loops with zip:

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
#This will output:
#Alice is 25 years old.
#Bob is 30 years old.

#simpler example of using zip in a loop:
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
for num, letter in zip(mylist1, mylist2):
    print(num, letter)
#This will output:
#1 a
#2 b
#3 c

#if one list is shorter than the other, zip will stop at the end of the shorter list:
mylist1 = [1, 2, 3, 4]
mylist2 = ['a', 'b']
for num, letter in zip(mylist1, mylist2):
    print(num, letter)
#This will output:
#1 a
#2 b

list(zip(mylist1, mylist2))
#This will output:
#[(1, 'a'), (2, 'b')]


#in can be used to check if a value is present in a list, tuple, or string. It returns True if the value is found and False otherwise.
#Example of using in with a list:
mylist = [1, 2, 3, 4, 5]
print(3 in mylist)  # This will output: True
print(6 in mylist)  # This will output: False

#Example of using in with a string:
mystring = "Hello, world!"
print("Hello" in mystring)  # This will output: True
print("hi" in mystring)  # This will output: False

#Example of using in with a tuple:
mytuple = (1, 2, 3, 4, 5)
print(3 in mytuple)  # This will output: True
print(6 in mytuple)  # This will output: False

3 in [1, 2, 3, 4, 5]  # This will output: True
"Hello" in "Hello, world!"  # This will output: True            

#The in operator is also useful for checking if a key is present in a dictionary:
mydict = {'a': 1, 'b': 2, 'c': 3}
print('a' in mydict)  # This will output: True
print('d' in mydict)  # This will output: False

#min and max are built-in functions that return the smallest and largest item in an iterable, respectively. They can also take multiple arguments and return the smallest or largest among them.
#Example of using min and max with a list:
mylist = [3, 1, 4, 1, 5]
print(min(mylist))  # This will output: 1
print(max(mylist))  # This will output: 5


#to import other useful functions you can use a library
from random import shuffle
mylist = [3, 1, 4, 1, 5]
shuffle(mylist)
print(mylist)
#shuffle functions just shuffles the contents of a list
#shuffle is an inplace function meaning you would have to use print to see results

#randint grabs a random integer, you will have to import this function also
from random import randint
randint(0,79)
#the output I got after running was 31, so a randomass integer

#input function allows the end user to put whatever value they want
name= input('What is your name? ')

#list comprehensions
mystring ='hello'
mylist=[]
for letter in mystring:
    mylist.append(letter)
    print(mylist)

#there is a shorter way of doing the same thing
mylist = [x for x in 'myword']
print(mylist)
#output ['m','y','w','o','r','d']

#u can use this in a lot of ways
mynum = [x for x in range(0,11)]
print(mynum)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mynum = [ x**2 for x in range (0,11)]
print(mynum)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#you can also use if statement alongside
mylist = [x for x in range (0,11) if x%2==0]
print(mylist)
#[0, 2,4,6,8,10] even numbers are recieved

#you can also perform complex maths
#celcius to farehenhiet conversion
celcius = [0,10,20,34.5]
farahenhiet = [((9/5)*x +32) for x in celcius]
print(farahenhiet)
#[32.0, 50.0, 68.0, 94.1] output

#using for loop for the same thing
farahenhiet =[]
for x in celcius:
    farahenhiet.append(((9/5)*x +32))
print(farahenhiet)
#[32.0, 50.0, 68.0, 94.1]

