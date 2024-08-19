def list_operations():
    # Creating a list
    my_list = [10, 20, 30, 40, 50]
    print("Initial list:", my_list)
    
    # Accessing elements
    print("First element:", my_list[0])
    print("Last element:", my_list[-1])
    
    # Modifying elements
    my_list[2] = 35
    print("List after modifying the third element:", my_list)
    
    # Adding elements
    my_list.append(60)  # Add element at the end
    my_list.insert(2, 25)  # Add element at a specific position
    print("List after adding elements:", my_list)
    
    # Removing elements
    my_list.remove(40)  # Remove the first occurrence of the value 40
    popped_element = my_list.pop()  # Remove and return the last element
    print("List after removing elements:", my_list)
    print("Popped element:", popped_element)
    
    # Iterating through the list
    print("Iterating through the list:")
    for item in my_list:
        print(item)
    
    # List slicing
    sliced_list = my_list[1:4]  # Get a sublist from index 1 to 3
    print("Sliced list (elements from index 1 to 3):", sliced_list)
    
    # List length
    list_length = len(my_list)
    print("Length of the list:", list_length)
    
    # Check if an element is in the list
    contains_element = 30 in my_list
    print("Is 30 in the list?", contains_element)
    
    # Sorting the list
    my_list.sort()
    print("Sorted list:", my_list)

# Call the function to perform list operations
list_operations()
