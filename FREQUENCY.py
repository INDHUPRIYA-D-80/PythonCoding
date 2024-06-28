/*Input format :
The first line of the input consists of the number of names.

#The next input is the user names.

#The last input is the user name to be searched.

#Output format :
#The output prints the frequency of the searched element.

#Sample test cases :
#Input 1 :
#5
#alice
#bob
#ankit
#alice
#prajit
#alice

#Output 1 :
#2
# Read the number of names
n = int(input())

# Initialize a list to store the user names
user_names = []

# Read the user names and add them to the list
for i in range(n):
    name = input().strip()
    user_names.append(name)

# Read the user name to be searched
search_name = input().strip()

# Count the frequency of the search_name in the list
frequency = user_names.count(search_name)

# Print the frequency
print(frequency)
