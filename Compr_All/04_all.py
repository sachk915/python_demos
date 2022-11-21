'''

#List
# Constructing output list WITHOUT
# Using List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_list = []

# Using loop for constructing output list
for var in input_list:
    if var % 2 == 0:
        output_list.append(var)

print("Output List using for loop:", output_list)


## Using List comprehensions
# for constructing output list

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]


list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:",
      list_using_comp)

'''
'''
#----------------------2
#Suppose we want to create an output list which contains squares of all the numbers from 1 to 9. Let’s see how to do this using for loops and list comprehension.
# Constructing output list using for loop
output_list = []
for var in range(1, 10):
    output_list.append(var ** 2)

print("Output List using for loop:", output_list)

# Constructing output list
# using list comprehension
list_using_comp = [var**2 for var in range(1, 10)]

print("Output List using list comprehension:",
							list_using_comp)

'''

#Dictionary

#1: Suppose we want to create an output dictionary which
# contains only the odd numbers that are present in the input
# list as keys and their cubes as values. Let’s see how to do
# this using for loops and dictionary comprehension.

input_list = [1, 2, 3, 4, 5, 6, 7]

output_dict = {}

# Using loop for constructing output dictionary
for var in input_list:
    if var % 2 != 0:
        output_dict[var] = var**3

print("Output Dictionary using for loop:", output_dict)
# Using Dictionary comprehensions
# for constructing output dictionary

input_list = [1,2,3,4,5,6,7]

dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:",
										dict_using_comp)

#2: Given two lists containing the names of
# states and their corresponding capitals, construct
# a dictionary which maps the states with their respective
# capitals. Let’s see how to do
# this using for loops and dictionary comprehension
'''
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']


output_dict = {}

# Using loop for constructing output dictionary
for (key, value) in zip(state, capital):
	output_dict[key] = value

print("Output Dictionary using for loop:",
							output_dict)

# Using Dictionary comprehensions
# for constructing output dictionary

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

dict_using_comp = {key:value for (key, value) in zip(state, capital)}

print("Output Dictionary using dictionary comprehensions:",
										dict_using_comp)


# Set
#only even number
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

output_set = set()

# Using loop for constructing output set
for var in input_list:
	if var % 2 == 0:
		output_set.add(var)

print("Output Set using for loop:", output_set)

# compre
# Using Set comprehensions
# for constructing output set

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_using_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:",
							set_using_comp)
#generator compre
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_gen = (var for var in input_list if var % 2 == 0)

print("Output values using generator comprehensions:", end = ' ')

for var in output_gen:
	print(var, end = ' ')


'''