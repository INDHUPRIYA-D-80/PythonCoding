def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    sum_of_powers = sum([d**power for d in digits])
    return sum_of_powers == number

def factorial(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

def is_perfect(number):
    divisors_sum = sum([i for i in range(1, number) if number % i == 0])
    return divisors_sum == number

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def reverse_list(arr):
    length = len(arr)
    for i in range(length // 2):
        arr[i], arr[length - i - 1] = arr[length - i - 1], arr[i]
    return arr

def check_number_properties(number):
    print("Number:", number)
    print("Armstrong:", "Yes" if is_armstrong(number) else "No")
    print("Factorial:", factorial(number))
    print("Perfect Number:", "Yes" if is_perfect(number) else "No")

def process_two_numbers(a, b):
    print("Number 1:", a)
    print("Number 2:", b)
    print("GCD:", gcd(a, b))

def process_list(arr):
    print("Original List:", arr)
    print("Reversed List:", reverse_list(arr[:]))

# Example usage
number = int(input("Enter a number: "))
check_number_properties(number)

a, b = map(int, input("Enter two numbers separated by spaces: ").split())
process_two_numbers(a, b)

arr = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
process_list(arr)
