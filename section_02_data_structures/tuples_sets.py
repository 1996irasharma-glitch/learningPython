#tuples()
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
my_tuple = (1, 2, 3, 4, 5)
len(my_tuple)  # Output: 5
#you can access tuple values by index just like you do with lists
my_tuple[2]  # Output: 3
#but unlike lists, tuples are immutable, meaning you cannot change their contents after creation
#my_tuple[0] = 10  # This will raise a TypeError because tuples do not support item assignment

type(my_tuple)  # Output: <class 'tuple'>
#you can also have tuples with mixed data types
mixed_tuple = (1, 'hello', 3.14, [1, 2, 3])
#you can also have nested tuples
nested_tuple = (1, 2, (3, 4), 5)
#to access the nested tuple, you can use multiple indices
nested_tuple[2]  # Output: (3, 4)
nested_tuple[2][1]  # Output: 4

t=('a','a','b','c')
t.count('a')  # Output: 2
t.index('b')  # Output: 2
t.index('a')  # Output: 0
#if you try to use index for a repeated value, it will return the index of the first occurrence of that value in the tuple. In this case, since 'a' appears twice in the tuple, t.index('a') will return 0, which is the index of the first 'a' in the tuple. If you want to find the index of the second occurrence of 'a', you can use the start parameter of the index method to specify where to start searching for 'a' after the first occurrence. For example, t.index('a', 1) will return 1, which is the index of the second 'a' in the tuple.
# count counts how many times a specific value appears in the tuple, while index returns the index of the first occurrence of a specific value in the tuple.

t[0] = 'z'  # This will raise a TypeError because tuples do not support item assignment

#tuples are often used to group related data together, especially when the data should not be changed after creation. They can also be used as keys in dictionaries or elements of sets, since they are immutable.



#sets {}
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
my_set = {1, 2, 3, 4, 5}
len(my_set)  # Output: 5
#you cannot access set values by index like you do with lists or tuples, since sets are unordered and unindexed
#but you can check if a value is in a set using the in keyword
3 in my_set  # Output: True
6 in my_set  # Output: False

#sets are mutable, meaning you can add or remove elements from a set after creation
my_set.add(6)  # Output: {1, 2, 3, 4, 5, 6}
my_set.remove(2)  # Output: {1, 3, 4, 5, 6}
#all values in a set must be unique, meaning that if you try to add a duplicate value to a set, it will not be added and the set will remain unchanged
my_set.add(3)  # Output: {1, 3, 4, 5, 6}

#sets are often used to store unique values and to perform mathematical set operations like union, intersection, and difference. They can also be used to remove duplicates from a list by converting the list to a set and then back to a list.
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)  # Output: {1, 2, 3, 4, 5}
unique_list = list(unique_set)  # Output: [1, 2, 3, 4, 5]
#this is how you convert a list to a set to remove duplicates and then convert it back to a list to get a list of unique values. Note that the order of the unique values may not be preserved since sets are unordered collections.


#booleans
#booleans are a data type that can only have two values: True or False. They are often used in conditional statements and logical operations to control the flow of a program. In Python, the boolean values are represented by the keywords True and False, which are case-sensitive.
# you need to capitalize the first letter of True and False when using them in your code, otherwise they will be treated as undefined variables and will raise a NameError. For example, if you write true instead of True, you will get a NameError because true is not defined as a boolean value in Python. Similarly, if you write false instead of False, you will also get a NameError for the same reason. Therefore, it is important to use the correct capitalization when working with boolean values in Python.
is_raining = True
type(is_raining)  # Output: <class 'bool'>
1 == 1  # Output: True
1 == 2  # Output: False
1> 2  # Output: False
1 < 2  # Output: True
#booleans can also be used in logical operations with the and, or, and not operators to combine or negate boolean values. For example:
