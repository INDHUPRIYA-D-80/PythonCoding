#1.NUMBERS: int,float,bool (non sequence)

#PROBLEM STATEMENT:Calculate factorials.N!=!*2*3*4....*N
N =int(input("Enter the number: "))
#WORKING ON INT
factorial = 1
for i in range(1,N+1):
    factorial=factorial*i
print(factorial)

#PROBLEM  STATEMENT Take inputs a,b,c and tell the roots of ax^2+bx+c

#WORKING ON DECIMAL
# print("TO FIND THE ROOTS OF THE EQUATION ax^2+b+c")

a=int(input("\nEnter the value of a: "))
b=int(input("\nEnter the value of b: "))
c=int(input("\nEnter the value of c: "))

d=(b**2-4*a*c)**0.5
root1=(-b+d)/2*a

root2=(-b-d)/2*a

print("\nRoot 1:",root1)
print("\nRoot 2: ",root2)

#2. STRINGS=sequence datatype

a= "indhu"
print(a)

# #OUTPUT INTENDED

# #SLICING: string[start:end:jump]
print(a[:4])    #output:indh
print(a[2])     #output:d
print(a[:3])    #output:ind
print(a[::2])   #output:idu


# #PS:Check if the input is Palindrome or not.

string  =input("CHECK FOR PALINDROME:")
print(string==string[::-1])

#OPERATIONS WITH STRINGS
fname="indhu"
lname="priya "
fullname = fname +""+ lname # '+' with strings, mean concatenation
print(fullname)

print(fullname*3) # '*' with strings, mean repeat it that many times

#OBJECT ORIENTED way of calling functions."Any string" is an object. 
print("indhu".upper())
print("01-07-2004".split("-")) #it splits the string at every occurence of - ( u can use any rather than -)

#3. LISTS =sequence datatype
#list must be in [],no need of data types,no need of size
squares_1 = [1,4,9,16,25]
squares_2 =[36,49,64,81,100]
 
#intended output :squares =[1,....,100]
squares = squares_1 + squares_2 #ADDING TWO LISTS

squares.append(121) #append the element at last
print(squares)

squares.pop() #delete the element at last
print(squares)

#slicing on lists
print(squares[1::2])
#reverse the list
print(squares[::-1])

#clearing the lists
squares.clear()
print(squares)

print(squares,len(squares))


#4.TUPLES=sequence datatype
#WHEN ITS ABOUT LISTS
elements = [34,7,91,9,1,20,10] #you can edit the elements at the same array
elements[2] = 98 # lists are mutable
print(elements)

#WHEN ITS ABOUT TUPLES
elements2= (34,7,91,9,1,20,10)#you cannot edit the elements after a tuple is made
print(elements2)
print(sorted(elements2)) #sorted tuple will be given output as list

#elements2[2] = 98 # Tuples are mutable it throws an error
print(elements2)

#5.SETS=sequence datatype

names = ["sagar","vishnu","hari","sagar","hari","sagar","vishnu","hrishikesh"]

#problem statement: tell me how many unique names are there in the list?
 
print(set(names),len(set(names)))

name ="sagar"

#problem statement: how many unique character 
print(set(name),len(set(name)))

set1={1,2,3,3,2,} #set prints only the unique characters
set2={3,4,5,3}

print(set1)
print(set2)

#set operation
print(set1 | set2) #union
print(set1 & set2) #intersection
print(set1 - set2) #Left difference
print(set2 - set1) #Right difference

#6.DICTIONARIES=sequence datatype

# till now, in lists/arrays you have done indexing like this.
array=[9,81,3,14,1,73,1,61,2,71]
#[gravity,pi,root_3,golden_ratio,euler_number]
print(array)
print(array[1])

# #can i do this ?array["pi"]

capitals={
    "India":"Delhi",
    "Germany":"Berlin",
    "USA":"Washington DC",
    "Australia":"Camberra"
}  
#"key":"value" pair  ==>items=>both keys:values

print(capitals["Germany"])
constants={
    "pi":3.14,
    "golden+ratio":1.61,
    "gravity":9.81
}
print(constants["gravity"])


exam_marks={
    "indhu":{
      "maths":98,
      "physics":80,
      "chemistry":80
    },
    "priya":{
      "maths":98,
      "physics":80,
      "chemistry":80
    },
}


print(exam_marks["indhu"]["maths"])
print(exam_marks.keys())
print(exam_marks.values())
print(exam_marks.items())
print(len(exam_marks))

