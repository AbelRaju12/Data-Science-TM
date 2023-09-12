# for loop - when no.of iterations is known
# while loop - when no.of iterations in unknown

# iterables >>> list, tuple, dictionary, string

for char in "techmaghi":
    print(char, end=" ")
print("\n")
for i in range(5):
    print(i, end = " ")

print("\n")

dict1 = {}

# for i in range(10):
#     key, value = int(input()), input()
#     dict1[key] = value

print(dict1)

list_1 = ['red', 'oramge', 'blue', 'yellow', 'pink', 'black', 'white']

for c in list_1:
    if c == 'oramge':
        continue
    print(c)
    if c == 'pink':
        break
    
i = 1    
while i <=10:
    print(i * 5)
    i += 1