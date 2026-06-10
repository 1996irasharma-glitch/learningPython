#Comparison operators are used to compare values. They return a boolean value (True or False) based on the comparison.
#Here are some common comparison operators in Python:
# == (equal to)
# != (not equal to)
# < (less than)
# > (greater than)
# <= (less than or equal to)
# >= (greater than or equal to)
#Example usage:
a = 5
b = 10
print(a == b)  # False
print(a != b)  # True
print(a < b)   # True

'bYE'=='bye'  # False, because string comparison is case-sensitive
print('bYE'=='bye')  # False

'2' == 2  # False, because they are of different types (string vs integer)
print('2' == 2)  # False

#logical operators can be used to combine multiple comparison operators. The logical operators are:
# and (logical AND)
# or (logical OR)
#Example usage:
x = 5
y = 10
print(x < 10 and y > 5)  # True, because both conditions are true
print(x < 10 or y < 5)   # True, because at least one condition is true

100==1 or 100==100  # True, because the second condition is true
print(100==1 or 100==100)  # True

#not (logical NOT) can be used to negate a comparison operator. It returns True if the condition is False, and False if the condition is True.
print(not (x < 10))  # False, because x is less than 10
print(not (y > 5))   # False, because y is greater than 5


#practice
#1. Check if a number is positive, negative, or zero.
num = -5
if num>0:
    print("The number is positive.")
elif num<0:
    print("The number is negative.")
else:
    print("The number is zero.")



