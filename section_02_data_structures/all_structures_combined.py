# lists []


#they are ordered sequences that can hold a variety of objects and support indexing and slicing
my_list = [1, 2, 3, 4, 5]
len(my_list)  # Output: 5
my_list[2]  # Output: 3

mylist = [1, 'hello', 3.14, [1, 2, 3]]
mylist + my_list  # Output: [1, 'hello', 3.14, [1, 2, 3], 1, 2, 3, 4, 5]

#unlike strings, lists are mutable, meaning you can change their contents after creation
my_list[0] = 10
my_list  # Output: [10, 2, 3, 4, 5]


my_list.append(6)  # Output: [10, 2, 3, 4, 5, 6]
#what append does is it adds an element to the end of the list
my_list.append([7, 8])  # Output: [10, 2, 3, 4, 5, 6, [7, 8]]
#what append does is it adds the entire list [7, 8] as a single element to the end of my_list

#pop removes and returns the last item from the list
my_list.pop()  # Output: [7, 8]
my_list  # Output: [10, 2, 3, 4, 5]
#you can also specify an index to pop a specific element
my_list.pop(0)  # Output: 10
my_list  # Output: [2, 3, 4, 5]
popped_item = my_list.pop()  # Output: 5
my_list  # Output: [2, 3, 4]
#if there is no index specified, pop will remove and return the last item in the list. If an index is specified, it will remove and return the item at that index.

new_list = ['a','x','e','b','c']
num_list = [4,1,3,2,5]
#sort will sort the list in place, meaning it will modify the original list
new_list.sort()  # Output: ['a', 'b', 'c', 'e', 'x']
num_list.sort()  # Output: [1, 2, 3, 4, 5]
#you can also sort in reverse order by passing the reverse=True argument
# a common mistake made is assuming that sort returns a new sorted list, but it actually modifies the original list and returns None
sorted_list = new_list.sort()  # Output: None
#but you can use it the following way to get a sorted list without modifying the original
sorted_list = sorted(new_list)  # Output: ['a', 'b', 'c', 'e', 'x']

#reverse will reverse the order of the list in place
new_list.reverse()  # Output: ['x', 'e', 'c', 'b', 'a']
#works similarly to sort, it modifies the original list and returns None
reversed_list = new_list.reverse()  # Output: None

#like strings, lists also support slicing to create sublists
my_list = [1, 2, 3, 4, 5]
sublist = my_list[1:4]  # Output: [2, 3, 4]
#you can also use negative indices to slice from the end of the list
sublist = my_list[-4:-1]  # Output: [2, 3, 4]

#end
#1. How do I index a nested list? For example if I want to grab 2 from [1,1,[1,2]]?

#You would just add another set of brackets for indexing the nested list, for example: my_list[2][1] 