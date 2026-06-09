#dictionaries {}
#dictionaries are a collection of key-value pairs
#dictionaries are mutable, meaning they can be changed after they are created
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
len(my_dict)  # Output: 3

#you cannot access dictionary values by index like you do with lists, instead you use the keys to access the values
#you also cannot sort a dictionary like you do with lists, but you can sort the keys or values separately if needed
my_dict['name']  # Output: 'Alice'
my_dict['age']  # Output: 30
#dictionaries are unordered collections, meaning that the order of the key-value pairs is not guaranteed. However, starting from Python 3.7, dictionaries maintain the insertion order of the key-value pairs.
#dictionaries can store a variety of data types as values, including other dictionaries, lists, and even functions


dict_with_list = {'name': 'Bob', 'hobbies': ['reading', 'gaming', 'hiking']}
dict_with_dict = {'name': 'Charlie', 'address': {'street': '123 Main St', 'city': 'Los Angeles'}}

dict_with_list['hobbies'][2] # Output: 'hiking'
#you can access the list of hobbies using the key 'hobbies' and then access the specific hobby using its index in the list

dict_with_dict['address']['city'] # Output: 'Los Angeles'
#you can access the nested dictionary using the key 'address' and then access the specific value using its key in the nested dictionary

#to add a new key-value pair to a dictionary, you can simply assign a value to a new key
my_dict['email'] = 'alice@example.com'
my_dict  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': 'alice@example.com'}
#to update the value of an existing key, you can assign a new value to that key
my_dict['age'] = 31
my_dict  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

#to get a list of all the keys in a dictionary, you can use the keys() method
my_dict.keys()  # Output: dict_keys(['name', 'age', 'city', 'email'])

#to get a list of all the values in a dictionary, you can use the values() method
my_dict.values()  # Output: dict_values(['Alice', 31, 'New York', 'alice@example.com'])

#to get a list of all the key-value pairs in a dictionary, you can use the items() method
my_dict.items()  # Output: dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York'), ('email', 'alice@example.com')])

#if a value gets repeated in a dictionary, the last value assigned to that key will be the one that is stored in the dictionary
repeated_dict = {'key1': 'value1', 'key2': 'value2', 'key1': 'new_value'}
repeated_dict  # Output: {'key1': 'new_value', 'key2': 'value2'}
#in this example, the key 'key1' is repeated, and the last value assigned to 'key1' is 'new_value', which is the value that is stored in the dictionary. The previous value 'value1' is overwritten and lost.

