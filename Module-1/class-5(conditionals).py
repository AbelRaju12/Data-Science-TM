num1 = 45
num2 = 93

if num2 > num1:
    print(f"{num2} is greater")
else:
    print(f"{num1} is greater")
    
color = 'red'
shape = 'round'

if color == 'orange' and shape == 'round':
    print("It is an orange")
elif color == 'yellow' and shape == 'round':
    print("It is a tennis ball")
else:
    print("It is something else")
    

print ('The color is red') if color == 'red' else print("Not red")

print ('It is a tomato ig') if color == 'red' and shape == 'round' else(print('It is tennis ball') if color == 'yellow' and shape == 'round' else print('Its somethig else') )