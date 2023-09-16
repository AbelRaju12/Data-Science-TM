#data structures are used to store data

#lists

list_1 = [1, 2, 4, [5, 6, 7], 5+7j, True, 'abel', {1: 'A', 2: 'B'}, (1, 4, 3), {7, 9, 10, 9}]
print(list_1)
print(list_1[3])
print(list_1[3][1])

print( list_1[::-1])
print(list_1[-3:-1]) #elements are numbered from -n to -1 just like it is numbered from 0 to n => 3:10 = -2:-9

list_1[6] = 'Professional'
print(list_1)


#tuples

tuple_1 = (1, 3, [4, 6, 7], 'abel', (1, 3, 4), {3, 5, 6})

# supports all indexing and slicing 

# tuple_1[1] = 3 # returns error

tuple_1 = list(tuple_1)
tuple_1[1] = 4  #no error

tuple_1 = tuple(tuple_1)


#sets

set_1 = {1, 4, 1, 5, 4, 5, 7, (1, 4, 5)}

#set cannot contain list or dictionaries
#no indexing or slicing

print(set_1)


#dictionaries

dict_1={'apple':343,2:'pro',True:[3,4,5,6],45:(5,3,4,5),(6,5,6):'abel'}

print(dict_1)
print(dict_1['apple'])

print(dict_1.values())
print(dict_1.keys())
print(dict_1.items())

dict_1={'apple':343,2:'pro',True:[3,4,5,6],45:(5,3,4,5),(6,5,6):'abel', 'apple': 434} #key: apple will get overriden with the last value and printed in the intial positon
print(dict_1)
