# Function to calculate the sum of two numbers
def add_numbers(a, b):
    return a + b

# Function to calculate the difference between two numbers
def subtract_numbers(a, b):
    return a - b

# Function to calculate the product of two numbers
def multiply_numbers(a, b):
    return a * b

# Function to divide two numbers
def divide_numbers(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

# Function to check if a number is even or odd
def is_even(number):
    return number % 2 == 0

# Function to perform bitwise AND operation
def bitwise_and(x, y):
    return x & y

# Function to perform bitwise OR operation
def bitwise_or(x, y):
    return x | y

# Function to compare two numbers
def compare_numbers(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{a} is less than {b}"
    else:
        return f"{a} is equal to {b}"

# Function to perform logical AND operation
def logical_and(a, b):
    return a and b

# Function to perform logical OR operation
def logical_or(a, b):
    return a or b

# Example usage of the functions
a = 10
b = 20

print("Sum:", add_numbers(a, b))
print("Difference:", subtract_numbers(a, b))
print("Product:", multiply_numbers(a, b))
print("Division:", divide_numbers(a, b))

number = 15
print(f"{number} is even:", is_even(number))

x = 5
y = 3
print("Bitwise AND:", bitwise_and(x, y))
print("Bitwise OR:", bitwise_or(x, y))

print("Comparison:", compare_numbers(a, b))

print("Logical AND:", logical_and(True, False))
print("Logical OR:", logical_or(True, False))
