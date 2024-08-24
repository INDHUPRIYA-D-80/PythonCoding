def is_palindrome(number):
    return str(number) == str(number)[::-1]

def is_even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_fibonacci(limit):
    fib_series = [0, 1]
    while fib_series[-1] + fib_series[-2] <= limit:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

def find_max_min(arr):
    max_value = arr[0]
    min_value = arr[0]
    for num in arr[1:]:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return max_value, min_value

def arrange_in_ascending(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def arrange_in_descending(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def check_number_properties(number):
    print("Number:", number)
    print("Palindrome:", "Yes" if is_palindrome(number) else "No")
    print("Even or Odd:", is_even_or_odd(number))
    print("Prime or Non-Prime:", "Prime" if is_prime(number) else "Non-Prime")
    print("Fibonacci Series up to", number, ":", generate_fibonacci(number))

def process_list(arr):
    print("Original List:", arr)
    max_value, min_value = find_max_min(arr)
    print("Maximum Value:", max_value)
    print("Minimum Value:", min_value)
    print("Ascending Order:", arrange_in_ascending(arr[:]))
    print("Descending Order:", arrange_in_descending(arr[:]))

# Example usage
number = int(input("Enter a number: "))
check_number_properties(number)

arr = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
process_list(arr)
