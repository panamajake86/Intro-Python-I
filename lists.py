#create a list
l = []

#create list with numbers
num_list = [1, 2, 3, 4]

#add element to empty list
l.append(77)

#print all values in num_list
for element in num_list:
    print(element)

#if you want the index of the element, use enumerate to access
for (i, elem) in enumerate(num_list):
    print(f'Element {i} is {elem}')

#how you loop through a certain number of times
for x in range(1, 10):
    print(x)

