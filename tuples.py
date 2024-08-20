#Tuple Creation: Multiple tuples are created, containing different types of elements.
#Accessing Elements: Elements are accessed using indices.
#Concatenation (+): Two tuples are concatenated to form a new tuple.
#Repetition (*): A tuple is repeated multiple times.
#Membership Test (in): Checks if an element is present in a tuple.
#Length (len): The length of a tuple is determined.
#Slicing: A part of a tuple is sliced and returned as a new tuple.
#Tuple Unpacking: Elements of a tuple are unpacked into individual variables.
#Nested Tuples: A tuple containing other tuples as elements.
#Single Element Tuple: Demonstrates how to create a tuple with a single element.
#Comparison: Tuples are compared element by element.
#Maximum and Minimum: Finds the maximum and minimum values in a tuple (if applicable).




# Tuple Creation
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 2, 3, 'a', 'b', 'c')

# Accessing Elements
print("First element of tuple1:", tuple1[0])
print("Last element of tuple2:", tuple2[-1])

# Concatenation
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# Repetition
repeated_tuple = tuple2 * 3
print("Repeated tuple:", repeated_tuple)

# Membership Test
is_present = 2 in tuple1
print("Is 2 present in tuple1?", is_present)

# Length of Tuple
length = len(tuple3)
print("Length of tuple3:", length)

# Slicing
sliced_tuple = tuple3[2:5]
print("Sliced tuple (elements from index 2 to 4):", sliced_tuple)

# Tuple Unpacking
a, b, c, d = tuple1
print("Unpacked values from tuple1:", a, b, c, d)

# Nested Tuples
nested_tuple = (tuple1, tuple2)
print("Nested tuple:", nested_tuple)

# Tuple with a single element (note the comma)
single_element_tuple = (10,)
print("Single element tuple:", single_element_tuple)

# Tuple Comparison
tuple4 = (1, 2, 3)
tuple5 = (1, 2, 4)
comparison = tuple4 < tuple5
print("Is tuple4 less than tuple5?", comparison)

# Maximum and Minimum (if elements are of the same type)
max_value = max(tuple1)
min_value = min(tuple1)
print("Maximum value in tuple1:", max_value)
print("Minimum value in tuple1:", min_value)
