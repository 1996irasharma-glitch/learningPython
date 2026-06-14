#writing an entire python code includes the following
#grab user input
#manipulate a avriable based on input
#return back adjusted variable


#displaying information
#to carry out this specific task, we can use print function 
x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
print (x)
print(y)
print(z)
#output
#>>> print (x)
#[1, 2, 3]
#>>> print(y)
#[4, 5, 6]
#>>> print(z)
#[7, 8, 9]

#but instead of using print again and again, we can create a function
def display(*arg):
    print(arg)
    
display(x,y,z)
#([1, 2, 3], [4, 5, 6], [7, 8, 9])

#we can also just update out lists and then print
y[1]=0
display(x,y,z)
#([1, 2, 3], [4, 0, 6], [7, 8, 9])


#accepting user input
#you can use input to accept value from the user
input("Please enter a value: ")
#the default of the values that are input are strings, sometimes you may need to convert this datatypes into other datatypes
#eg:
result = input("Please enter a value: ")
type(result)
#<class 'str'>
#to change this into an integer
result_int = int(result)
type(result_int)
#<class 'int'>
result_float = float(result)
type(result_float)
#<class 'float'>

#validating user input
#when an input is asked to the user and it is not provided, we cannot work with anything else untill that input is provided
#this problem needs to be rectified by employing a while lopp which would keep asking the user for an input until an appropriate one is not provided
#lets take an example
def user_choice():
    choice = input("Please enter a number (0-10): ")
    return int(choice)
#the problem with this function is that it would not follow the constraints we would want it o follow
#if I enter 100, this would work when I dont want it too
#so we need to check whether our given input is the correct dataype or not and then whether it adheres with the constraints provided
#lets fix the above example

def user_choice():
    choice = 'Wrong'
    while choice.isdigit()==False:
        choice = input("Please enter a number (0-10):")
    return int(choice)
user_choice()

#this code here will keep asking u for input if the given input does not abide by the set constraints
#now we will add our range of acceptable inputs


def user_choice():
    acceptable_range = range(0, 11)
    
    while True:
        choice = input("Please enter a number (0-10): ")
        
        if choice.isdigit() == False:
            print("Sorry, this is not a digit")
        elif int(choice) not in acceptable_range:
            print("Sorry, you are out of the acceptable range (0-10)")
        else:
            return int(choice)

user_choice()
 
#lets put everything together and make a game
#the program will display a list, have a user choose an index position with an input value
#and then replace previous value of index with new value
#we need a display function
#a position choice function
#a replacement function
#a gameon function,ie whether or not u want to keep playing



def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


def position_choice():
    acceptable_range = ['0','1','2']  # also fixed the typo: 'accpetable'
    
    while True:
        choice = input("Pick a position (0, 1, 2): ")

        if choice.isdigit() == False:
            print("Sorry, this is not a digit")
        elif choice not in acceptable_range:
            print("Your choice does not lie in the acceptable range")
        else:
            return int(choice)



def replacement_choice(game_list,position):
    replacement = input("Type a string to place at chosen position")
    game_list[position] = replacement
    return game_list




def gameon_choice():
    choices = ['Y', 'N']
    
    while True:
        x = input("Do you want to continue this game: (Y or N) ")
        
        if x not in choices:
            print("Sorry, please choose between Y or N")
        elif x == 'Y':
            return True
        else:
            return False


game_on = True
game_list = [4,5,6]

while game_on == True:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list,position)
    display_game(game_list)
    game_on = gameon_choice()


     

