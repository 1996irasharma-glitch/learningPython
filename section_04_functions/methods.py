#methods
#methods are essentially functions that are built into objects
mylist = [1,2,3]
mylist.append(4)
print(mylist)
#add 4 to the list

mylist.insert(3,5)
print(mylist)
# you can explore different methods by clicking dot and scrolling through the list of functions available
#you can know the function of each method by using help() and putting the function inside the brackets


#functions
#functions allow us to create blocks of code that can be easily executed many times without having to actually rewrite the code again
#creating a function requires a very specific syntax and correct indentation
#def is used to define a function
#syntax: def_name_of_function():
#            what you want the function to do
#so now whenever u use the name of the function the task woul automatically be executed
def say_hello():
    print("hello")

say_hello()
#this prints hello


def say_hello(name):
    print('Hello{}'.format(name))
say_hello('Ira')
#output: say_hello('Ira')
#        HelloIra

#if while executing the function you forget to add something in the bracket when required, it is going to produce an error
#to fix this we can add a default value while defining function, so that when brackets are accidently left empty, the default value is used

def say_hello(name='Default'):
    print(f'Hello{name}')
say_hello()
#output:HelloDefault


#return
#return allows you to basically save stuff as variable rather than just printing them

def add_num(num1,num2):
    return num1+num2

add_num(10,20)
#30

#the basic difference between print and result is result allows u to save stuff as variables, eg:
def add_num(num1,num2):
    return num1+num2

result = add_num(10,20)
print(result)
#here I am able to save my function in result and ask to print result to see an output
#whereas in print you wont be able to save it as result and then ask to print result, eg:
def add_num(num1,num2):
    print(num1+num2)

result = add_num(10,20)
print(result)
#this block of code returns none

#if u ant both these functionalities at the same time you can use both functions simultaneously
#not super common to use
#make sure u are inputting the right data type to avoid potential bugs

#using logic alongside functions
#even number checker
def even_check(number):
    result = number % 2  == 0
    return result
even_check(21)
even_check(20)
#you get true and false accordingly

#return true if any number is even inside a list
def check_even_list(num_list):
    for x in num_list:
        if x % 2 == 0:
            return True
        else:
            pass
        
check_even_list([1,2,3,4,5,6])
#this code reurns true as there are even elements present in the list
#if you use return False after else, it would return an error as the code would only check the first element of letter only and end the code
#instead you can just change the indentation such that all the elements in the list are iterated before assuming it to be false

def check_even_list(num_list):
    for x in num_list:
        if x % 2 == 0:
            return True
    return False

check_even_list([3,9,11])
#this would give false as an answer

#return all even numbers in a list
#always have a placeholder datatype in such cases
def return_even_list(num_list):
    even_nos = []
    for x in num_list:
        if x % 2 == 0:
            even_nos.append(x)
    return even_nos

return_even_list([1,2,3,4])
#2 and 4 are returned

#working with tuples
my_tup = [(1,'a'),(2,'b'),(3,'c')]
for item in my_tup:
    print(item)

#this prints out all items and if u want to unpack the tuple
my_tup = [(1,'a'),(2,'b'),(3,'c')]
for x, y in my_tup:
    print(x)
    print(y)

 #interactics between functions
 #shuffling game 
 #lets get to know of the shuffle function

example = [1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)
print(example)
#[1, 3, 7, 2, 4, 6, 5] 

#because shuffle doesnt return anything being an inplace function, we need to create a new function
def shuff(my_list):
    shuffle(my_list)
    return my_list
result = shuff([0,1,2,3,4,5,6])
print(result)
#function created


#we need to create a game where among the three elements in a list where two are empty strings and one is 0, user needs to guess where the 0 is
listy = ['',0,'']
result = shuff(listy)
# now we need to create a guessing function
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Pick a position (0,1,2): ')
    return int(guess)

# play the game
player_choice = player_guess()
if result[player_choice] == 0:
    print('Correct!')
else:
    print('Incorrect!')