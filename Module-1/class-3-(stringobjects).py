#strings are indexed

name = "Abel Raju"
print(name[0])


#slicing

print(name[0:5])
print(name[::2])
print(name[4::-1])
print(name[::-1])
print(name[::])
print(len(name))


#functions

print(name.upper())
print(name.lower())
#string is immutabel you cannot modify an index

print(name.lower().count('a'))
print(name.split(' '))


#additonal fns

print('python'.replace('p','P'))

print("       abel is a pro        ")
print("       abel is a pro        ".rstrip())
print("       abel is a pro        ".lstrip())
print("       abel is a pro        ".strip())

print("124f".isdigit())
print("124f".isalnum())
print("abcd".isalpha())

print("     ".isspace())

print(name.startswith('A'))
print(name.endswith('ju'))


#extra

string4='vanshika\'s book' # to print 's
print(string4)
print(string4.capitalize())