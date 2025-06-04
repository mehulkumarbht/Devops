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
# color = "red"
# color = "blue"
# print(color)

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