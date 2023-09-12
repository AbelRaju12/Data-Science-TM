#same naming convention as variables
def addition(a,b,c):
    """This fucntions adds three numbers"""
    return a+b+c

sum = addition(1,2,3)
print(sum)

help(addition)

#arbtrary arguments

def func(*items):
    return items
    
print(func(5))
print(func('abel','raju'))
print(func('abel','raju', [1,2,4]))


#arguments are sequentially assigned

def details(name, age):
    print("name:",name)
    print("age:", age)
    
details('Abel',21)
details(21, 'Abel')

details(age=21, name='Abel') #specfying the keys


#arbtrary keyword args

def details_1(**items):
    print(items)
    
details_1(name = 'Abel', age=21, job = 's/w developer')
details_1(name = 'Abel', age=21, job = 's/w developer', passion = 'videogames')


