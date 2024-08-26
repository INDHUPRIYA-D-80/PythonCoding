def is_armstrong(number):
    # Convert the number to a string to easily get each digit
    digits = [int(digit) for digit in str(number)]
    # Get the number of digits
    num_digits = len(digits)
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(digit ** num_digits for digit in digits)
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
