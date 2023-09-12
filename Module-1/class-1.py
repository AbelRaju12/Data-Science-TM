multi_line_string = """
Hi. So this is am multi
line string
"""
 
#string va cannot start with a number and comb of (letter, digit, underscore)

print(type(multi_line_string))

complex_num = 234+64j
print(type(complex_num)) #j for complex number
print(complex_num + 5) 

imaginary = complex_num.imag
real = complex_num.real
print(imaginary, real)

print("python",str(3))