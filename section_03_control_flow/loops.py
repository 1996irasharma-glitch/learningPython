#iteration is the process of repeating a block of code multiple times. In Python, we can use loops to achieve this. There are two main types of loops in Python: for loops and while loops.
#FOR LOOPS
#syntax:

#my_iterable = [1, 2, 3]
#for item in my_iterable:
    #do something with item 
    #print(item)

mylist =[1,2,3,4,5,6,7,8,9,10]
for x in mylist:
    print(x)
#this prints each item in the list on a new line. We can also use the range() function to generate a sequence of numbers. For example:
for x in mylist:
    print('hello')
#this will print 'hello' for each item in the list. We can also use an if statement inside the for loop to filter the items we want to print. For example:
for x in mylist:
    if x % 2 ==0:
        print(x)
    else:
        print('odd number: {}'.format(x))
#this will print the even numbers from the list. We can also use the range() function

a=0
for x in mylist:
    a = a + x
    print(a)
#this will print the cumulative sum of the numbers in the list. We can also use the
#if you only want to see the last value of a, you can print it after the loop is finished. For example:
a=0
for x in mylist:
    a = a + x
print(a)

#working with strings in for loops
mystring = 'hello world'
for x in mystring:
    print(x)
#this will print each character in the string on a new line. We can also use the

#for tuples in for loops. For example:
mytuple = (1,2,3,4,5)
for x in mytuple:
    print(x)
#this will print each item in the tuple on a new line. We can also use the

#for tuples inside tuples. For example:
mytuple = (1,2,3,(4,5))
for x in mytuple:
    print(x)
#this will print each item in the tuple on a new line. The last item is a tuple itself, so it will be printed as a tuple. We can also use the range() function to generate a sequence of numbers. For example:

#tuple unpacking in for loops. For example:
mylist = [(1,2),(3,4),(5,6)]
for a,b in mylist:
    print(a)
    print(b)
#this will print the first and second item in each tuple on a new line. We can also use the range() function to generate a sequence of numbers. 
#you can do this for any iterable, not just lists. For example, you can use a for loop to iterate over a string, a tuple, or even a dictionary. 

#dictionaries in for loops. For example:
mydict = {'a':1,'b':2,'c':3}
for x in mydict:
    print(x)
#this will only print the keys of the dictionary on a new line. We can also use the items() method to get both the keys and values. For example:
mydict = {'a':1,'b':2,'c':3}
for x,y in mydict.items():
    print(x)
    print(y)

#you can also use mydict.values() to get only the values of the dictionary. For example:
mydict = {'a':1,'b':2,'c':3}
for x in mydict.values():
    print(x)

#and you can use mydict.keys() to get only the keys of the dictionary. For example:
mydict = {'a':1,'b':2,'c':3}
for x in mydict.keys():
    print(x)


for x in range(0,11):
    print(x)
#this will print the numbers from 0 to 10. We can also specify a step value in the range() function. For example:
#in cases like such you do not need to define a list or any other iterable, you can just use the range function to generate the sequence of numbers you want to iterate over.

for x in range(0,11,2):
    print(x)
#this will print the even numbers from 0 to 10. We can also use a for loop to iterate over a string. For example:



#WHILE LOOPS
#syntax:
#while some_boolean_condition:
    #do something
    #print('hello')
#the difference between a for loop and a while loop is that a for loop is used to iterate over a sequence of items, while a while loop is used to repeat a block of code as long as a certain condition is true. For example:
#else is used in conjunction with while loops to execute a block of code when the condition in the while loop becomes false. For example:
x = 0
while x < 5:
    print(x)
    x = x + 1
#else block will be executed when the while loop condition becomes false. For example:
x = 0
while x < 5:
    print(x)
    x = x + 1
else:
    print('x is no longer less than 5')

#you can also use a while loop to iterate over a string. For example:
mystring = 'hello world'
x = 0
while x < len(mystring):
    print(mystring[x])
    x = x + 1

#you can also use a while loop to iterate over a list. For example:
mylist = [1,2,3,4,5]
x = 0
while x < len(mylist):
    print(mylist[x])
    x = x + 1

#what you have to do comes after the print statement in the while loop, otherwise you will get an infinite loop.

#break, continue, pass
#pass is a null statement in Python. It is used when you want to write a block of code that does nothing. For example:
x = 0
while x < 5:
    pass
#this will do nothing and will not print anything.
#if pass is not used in a block of code, you will get an error. because Python expects an indented block of code after the while statement. For example:
x = 0
while x < 5:
    #this will give an error because there is no indented block of code after the while statement.

#continue is used to skip the current iteration of a loop and move on to the next iteration. For example:
x = 0
while x < 5:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1
#this will print the numbers from 0 to 4, except for 3. When x is equal to 3, the continue statement will be executed, which will skip the print statement and move on to the next iteration of the loop.

#break is used to exit a loop prematurely. For example:
x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x = x + 1 
#this will print the numbers from 0 to 2. When x is equal to 3, the break statement will be executed, which will exit the loop and stop the execution of the code inside the loop.
#all these commands are used after the if statement in the loop, otherwise you will get an error. because Python expects an indented block of code after the if statement. 

#you can also use a for loop with break, continue, and pass. For example:
mylist = [1,2,3,4,5]
for x in mylist:
    if x == 3:
        break
    print(x)

#if u ever get a while loop that is running indefinitely, you can use the break statement to exit the loop. For example:
x = 0
while True:
    print(x)
    x = x + 1
    if x == 5:
        break


