from loguru import logger

#1: Create a variable named user_age and assign your age to it. Print the variable.

user_age = 35

logger.info(f"{user_age}")

#2: Assign the value 3.14159 to a variable called pi and print its type using type().

pi = 3.14159

logger.info(type(pi))

#3: Declare two variables width = 5 and height = 10. Calculate the area of a rectangle and store the result in area. Print it.

width = 5

height =10

area = width * height

logger.info(f"{area}")

#4: Create a variable name and assign it your name. Then print:"Hello, my name is <your name>!"

my_name = "sarah"

logger.info(f"Hello, my name is {my_name}")

#5: What happens if you assign a new value to an existing variable? Try this:
* color = "red"
* color = "blue"
* print(color)

color = "red"

color = "blue"

logger.info(f"{color}") # Variable assigned with new value

#6: Swap the values of two variables a = 5 and b = 10 without using a third variable.

a=5 

b=10

a,b = b,a 

print(a)

print(b)

#7: Convert a string variable year = "2024" into an integer and print its type after conversion.

year = "2024"

year = int(year)

print(type(year))

#8: Create variables num1 = 7, num2 = 3. Perform and print:Addition, Subtraction, Multiplication, Division, Integer division, Modulo

num1 = 7

num2 = 3

Addition = num1 + num2

Substraction = num1 - num2

Multiplication = num1 * num2

Division = num1 /num2

Integer_division = num1 // num2

Modulo = num1 % num2

print (Addition)

print (Substraction)

print (Division)

print (Integer_division)

print (Modulo)

#9: Assign None to a variable called data and check if the variable is None using an if condition.

data = None

if data is None:

    print(data)

#10: Explain the difference between global and local variables in a function using a short code example.

x = "awesome"

def myfunc():

    global x

    x = "fantastic"

myfunc()

logger.info(f"Python is {x}")

#when x is global and local variable

x = "awesome"

def myfunc():

    x = "fantastic"

    logger.info(f"Python is {x}")

myfunc()

logger.info(f"Python is {x}")


# #11:What type is assigned?
x = 42
y = "42"
z = 42.0
print(type(x))
print(type(y))
print(type(z))

#12: Create a variable is_valid and assign a Boolean value (True or False). Print its type
is_valid = True
print(type(is_valid))

#13: number =100, Convert it to an int, then a float, then back to str. Print each result with its type.
number ='100'
number_int = int(number)
print(number_int)
print(type(number_int))

number_fl = float(number)
print(number_fl)
print (type(number_fl))

number_st = str(number)
print(number_st)
print(type(number_st))

#14:Use the isinstance() function to check if 3.14 is a float, and "hello" is a string.
print(isinstance(3.14, float))
print(isinstance("hello", str))

#15: What is the result of this expression:
result = 10 / 2
print(result, type(result))

#16: Assign a complex number (like 2 + 3j) to a variable. Print its type and real/imaginary parts.
num = 2+3j
print(type(num))
print(num.real)
print(num.imag)

#17: What happens if you try to add a string and an integer?
a = "Age: "
b = "25"
print(a + b)

#18: Create a variable called names and assign a list of three strings. Then print the type and length of the list
names = ["Roy", "Vance", "John"]
print(type(names), len(names))

#19: Use a tuple to store three values: a name, an age, and a country. Print each element using indexing.
value = ("John", 29, "Spain")
print(value[0])
print(value[1])
print(value[2])

#20: Create a dictionary called employee with keys: name, age, and department. Assign appropriate values and print the dictionary and the type of employee.
employee = {"name": "john", "age": 29, "department": "Finance" }
print(employee, type(employee))
