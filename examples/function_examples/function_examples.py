# User-Defined Functions
def bereken(getal1, getal2):
    if getal1 > getal2:
        resultaat = getal1 * 2
    else:
        resultaat = getal2 * 3
    return resultaat

def print_bereken(a, b):
    print(a ** 3 + b ** 2)


def add_numbers(a, b):
    return a + b


# A anonymous function
add = lambda a, b: a + b




# Function calls

a = 5
b = 7


c = bereken(a, b)

# Built-in Function call
print(c)  # Output: 21


print_bereken(5,8) ## Output: 189

 
x = 20
y = 15

z = bereken(x, y)  

# Built-in Function call
print(z) # Output: 40


sum_result = add_numbers(10, 15)
print(sum_result)  # Output: 25


print(add(50, 15))  # Output: 25
