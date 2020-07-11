#using list comprehensions

#create a new list containing squares of all values in 'numbers'
numbers = [1, 2, 3, 4, 5]
print(numbers)

#long way round
#squares = []
#for num in numbers:
#    squares.append(num*num)

#list comprehension
squares = [num*num for num in numbers]
print(numbers)

#create new list containing only even values of 'numbers'
#long way
##evens = []
#for num in numbers:
#    if num % 2 == 0:
#        evens.append(num)

#list comprehension
evens = [num for num in numbers if num % 2 == 0]

#create a new list containing only the names that start with 's' so that they are properly capitalized (regardless of how the name originally appears)

names = ["Sarah", "Jorge", "sam", "bobby", "steph"]
s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)

##################################

