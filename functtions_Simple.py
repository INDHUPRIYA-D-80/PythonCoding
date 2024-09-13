# Function to check if a number is palindrome
def is_palindrome(number):
    return str(number) == str(number)[::-1]

# Function to check if a number is even or odd
def is_even(number):
    return number % 2 == 0

# Function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Function to generate Fibonacci series up to 'n' terms
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Main function
def main():
    number = int(input("Enter a number: "))
    
    # Check palindrome
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")
    
    # Check even or odd
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    
    # Check prime
    if is_prime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")
    
    # Generate Fibonacci series
    n = int(input("Enter the number of terms for the Fibonacci series: "))
    print(f"Fibonacci series up to {n} terms: {fibonacci(n)}")

# Run the main function
if __name__ == "__main__":
    main()
