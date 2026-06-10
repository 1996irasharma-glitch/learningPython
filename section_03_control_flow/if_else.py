#control flow statements
# if statement
# else statement
# elif statement

#indentation is important in python
if 3>2:
    print("3 is greater than 2") 

#or you can provide a condition to the if statement
hungry = True
if hungry:    
        print("I am hungry")
# else statement
hungry = False
if hungry:    
        print("I am hungry")
else:
    print("I am not hungry")

    #if and else need to be indented at the same level

location = "school"

if location == "school":
      print('I am at school')
else:
      print('I do not know where I am')

#elif statement
#elif is used to check multiple conditions
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
