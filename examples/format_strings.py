




# Old Style String Formatting (% Operator)

name = "John"
age = 30
formatted_string = "Hello, %s. You are %d years old." % (name, age)
print(formatted_string)


# str.format() Method

name = "Jane"
age = 25
formatted_string = "Hello, {}. You are {} years old.".format(name, age)
print(formatted_string)

# With positional arguments
formatted_string = "Hello, {0}. You are {1} years old.".format(name, age)
print(formatted_string)


# Formatted String Literals (f-Strings, Python 3.6+)

name = "Alex"
age = 20
formatted_string = f"Hello, {name}. You are {age} years old."
print(formatted_string)

# With expressions
formatted_string = f"Hello, {name}. Next year, you will be {age + 1} years old."
print(formatted_string)

# Template Strings (from string module)

from string import Template

name = "Sam"
age = 35
template = Template("Hello, $name. You are $age years old.")
formatted_string = template.substitute(name=name, age=age)
print(formatted_string)

# Escape sequences
# To include special characters in strings, you use the backslash (\) to escape them, such as \', \", or \\.


print('He said, "Python is awesome!"')
print('It\'s a great day.')


# output
# He said, "Python is awesome!"
# It's a great day.

print("tot" + "ziens")  	        #   	⇒ totziens
print("tot " + "ziens")  	   		#       ⇒ tot ziens
print("tot" + " ziens")  	   		#       ⇒ tot ziens
print("tot" + " " + "ziens")        #   	⇒ tot ziens

text = "Ha"
print(text * 3) # HaHaHa
