## Write a function that takes a name as input and returns a personalised greeting
name = str(input("Please add your name: "))
logger.info(f"Hello! {name}, Welcome!!")

## Implement a solution to convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_c = int(input("Please add temperature in celcius: "))
temp_f = celsius_to_fahrenheit(temp_c)
logger.info(f"{temp_c} C is {temp_f} F")

#Create a function that takes a list of numbers and returns their average.

def average(numbers):
    if not numbers:
        return 0 # or raise error based on use case
    return sum(numbers)/len(numbers)

list_of_numbers = [9,5,1,2,7]
avg = average(list_of_numbers)
logger.info(f"Avg of numbers is {avg}")

## Create a menu-driven calculator using functions for add, subtract, multiply, and divide
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def calculator():
    while True:
        print("\n--- Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)

            print(f"Result: {result}")
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Run the calculator
calculator()
