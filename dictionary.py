# Creating a dictionary
student_scores = {
    'John': 85,
    'Emma': 92,
    'Oliver': 78,
    'Sophia': 88
}

# Accessing values using keys
print("Emma's score:", student_scores['Emma'])

# Adding a new key-value pair
student_scores['Mia'] = 95
print("Updated dictionary:", student_scores)

# Updating an existing value
student_scores['John'] = 90
print("Dictionary after updating John's score:", student_scores)

# Removing a key-value pair
del student_scores['Oliver']
print("Dictionary after removing Oliver:", student_scores)

# Checking if a key exists
if 'Sophia' in student_scores:
    print("Sophia's score is present in the dictionary.")

# Iterating through the dictionary
print("\nAll student scores:")
for name, score in student_scores.items():
    print(f"{name}: {score}")

# Finding the maximum score
max_score = max(student_scores.values())
print("\nHighest score:", max_score)

# Finding the corresponding student(s) with the maximum score
top_students = [name for name, score in student_scores.items() if score == max_score]
print("Top student(s):", ", ".join(top_students))
