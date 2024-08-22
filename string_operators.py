# Define strings
str1 = "Hello"
str2 = "World"
str3 = "Python"
char = "o"

# 1. Concatenation (+)
concatenated = str1 + " " + str2
print("Concatenation: ", concatenated)  # Output: "Hello World"

# 2. Repetition (*)
repeated = str1 * 3
print("Repetition: ", repeated)  # Output: "HelloHelloHello"

# 3. Membership (in, not in)
is_in = char in str1
is_not_in = char not in str2
print(f"Is '{char}' in '{str1}'? ", is_in)        # Output: True
print(f"Is '{char}' not in '{str2}'? ", is_not_in)  # Output: False

# 4. String slicing ([:])
sliced = str3[1:4]  # Extracts characters from index 1 to 3
print("Slicing: ", sliced)  # Output: "yth"

# 5. String length (len())
length = len(str3)
print("Length of str3: ", length)  # Output: 6

# 6. String comparison (==, !=, >, <, >=, <=)
is_equal = str1 == str2
is_not_equal = str1 != str3
is_greater = str1 > str2
print("Is str1 equal to str2? ", is_equal)  # Output: False
print("Is str1 not equal to str3? ", is_not_equal)  # Output: True
print("Is str1 greater than str2? ", is_greater)  # Output: False

# 7. String formatting (%)
formatted_str = "Welcome to %s!" % str3
print("Formatted String: ", formatted_str)  # Output: "Welcome to Python!"

# 8. String formatting (f-strings)
f_str = f"{str1}, {str2}! Welcome to {str3}."
print("Formatted String (f-string): ", f_str)  # Output: "Hello, World! Welcome to Python."
