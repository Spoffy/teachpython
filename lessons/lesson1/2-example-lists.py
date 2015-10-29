"""
Lists
##########

Lists are another type. 
They consist of lots of different items of data of any type.

Each item in the list can be retrieved by its position.
Retrieving values from a list is slightly odd.
The index (position) of the first item in a list is 0.

Lists can have things appended onto the end and removed, as well as lots of other
things we won't go into here!

The full list of things lists can do can be found here:

https://docs.python.org/3.4/library/stdtypes.html#sequence-types-list-tuple-range
"""

#Creating an empty list.
#Both of these are identical.
empty_list = []
empty_list = list()

#Creating a list containing just integers
just_integers = [1, 2, 3, 4, 3, 2, 1, 99, 13]

#Creating a list of mixed types
mixed_types = [1, 2, "Hello", 1, "Banana", "Coconut", 3.0, True]

#Let's create a list to work with to demo things!
my_list = [1, 2, 3]

print("My list:", my_list)

#Appending to a list.
#Don't worry too much about the syntax for now, just know you need to put:
#   .append( some_value ) after the name of the list variable!
my_list.append(4)
my_list.append(10)

print("My list after append:", my_list)


#Retrieving the first item, assigning to the variable first_item:
first_item = my_list[0]

#Retrieving the third item
my_list[2]

#You can also change the item in a list at a specific position!
my_list[2] = "Now there's text here!"

print("My list after substitution:", my_list)